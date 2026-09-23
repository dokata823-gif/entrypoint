import os
import re
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
import yfinance as yf
import pandas as pd
import numpy as np

app = Flask(__name__, static_folder=".")

def format_ticker(ticker: str) -> str:
    """티커 문자열을 yfinance 규격에 맞게 표준화"""
    t = ticker.strip().upper()
    # 한국 6자리 종목코드 (예: 005930 -> 005930.KS)
    if re.match(r"^\d{6}$", t):
        return f"{t}.KS"
    # KRX 접두사 제거 (예: KRX:005930 -> 005930.KS)
    if t.startswith("KRX:"):
        code = t.replace("KRX:", "")
        return f"{code}.KS" if re.match(r"^\d{6}$", code) else code
    # 일본 주식 번호 (예: 186A -> 186A.T)
    if t.endswith(".T") or t.endswith(".KS") or t.endswith(".KQ"):
        return t
    return t

def detect_currency(ticker: str):
    """티커에 따른 통화 및 로케일 결정"""
    t = ticker.upper()
    if t.endswith(".KS") or t.endswith(".KQ") or re.match(r"^\d{6}$", t):
        return "₩", "ko-KR", True, False
    if t.endswith(".T"):
        return "¥", "ja-JP", False, True
    return "$", "en-US", False, False

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/entry_point.html")
def entry_point():
    return send_from_directory(".", "entry_point.html")

@app.route("/api/stock", methods=["GET"])
def get_stock_data():
    """
    HTML 프론트엔드로부터 티커를 전달받아
    yfinance로 실시간/히스토리 데이터를 수집하고 5단계 하락 타점 및 MA를 계산하여 반환
    """
    raw_ticker = request.args.get("ticker", "MU").strip()
    formatted_ticker = format_ticker(raw_ticker)
    currency_symbol, locale, is_krw, is_jpy = detect_currency(formatted_ticker)

    try:
        # yfinance 데이터 수집 (최근 1년치 일봉)
        stock = yf.Ticker(formatted_ticker)
        df = stock.history(period="1y", interval="1d")

        if df.empty:
            # 보조 시도: 6개월치
            df = stock.history(period="6mo", interval="1d")

        if df.empty:
            return jsonify({
                "success": False,
                "error": f"티커 '{raw_ticker}'의 주가 데이터를 찾을 수 없습니다."
            }), 404

        # 캔들 데이터 가공 (Lightweight Charts 포맷: time, open, high, low, close)
        candles = []
        for index, row in df.iterrows():
            date_str = index.strftime("%Y-%m-%d")
            c_open = float(row["Open"])
            c_high = float(row["High"])
            c_low = float(row["Low"])
            c_close = float(row["Close"])
            c_vol = int(row["Volume"]) if "Volume" in row else 0

            # 통화별 반올림
            if is_krw or is_jpy:
                c_open, c_high, c_low, c_close = round(c_open), round(c_high), round(c_low), round(c_close)
            else:
                c_open, c_high, c_low, c_close = round(c_open, 2), round(c_high, 2), round(c_low, 2), round(c_close, 2)

            candles.append({
                "time": date_str,
                "open": c_open,
                "high": c_high,
                "low": c_low,
                "close": c_close,
                "volume": c_vol
            })

        # 1. 최고점 (Peak / 52주 고가) 및 현재가 계산
        highest_price = float(df["High"].max())
        latest_price = float(df["Close"].iloc[-1])
        drop_from_peak = ((latest_price - highest_price) / highest_price) * 100

        # 2. 이동평균선(MA20, MA50) 계산
        df["MA20"] = df["Close"].rolling(window=20).mean()
        df["MA50"] = df["Close"].rolling(window=50).mean()

        ma20_data = []
        ma50_data = []
        for index, row in df.iterrows():
            date_str = index.strftime("%Y-%m-%d")
            if pd.notna(row["MA20"]):
                val20 = round(float(row["MA20"]), 0 if is_krw else 2)
                ma20_data.append({"time": date_str, "value": val20})
            if pd.notna(row["MA50"]):
                val50 = round(float(row["MA50"]), 0 if is_krw else 2)
                ma50_data.append({"time": date_str, "value": val50})

        # 3. 5단계 하락 타점 계산 (최고점 기준 -30%, -35%, -40%, -45%, -50%)
        def round_price(val):
            return round(val) if (is_krw or is_jpy) else round(val, 2)

        levels = [
            {
                "id": 1,
                "name": "1차 매수",
                "rate": 0.30,
                "label": "-30% (x0.70)",
                "price": round_price(highest_price * 0.70),
                "gap": round(((round_price(highest_price * 0.70) - latest_price) / latest_price) * 100, 2),
                "is_reached": bool(latest_price <= highest_price * 0.70),
                "color": "#3b82f6"
            },
            {
                "id": 2,
                "name": "2차 매수",
                "rate": 0.35,
                "label": "-35% (x0.65)",
                "price": round_price(highest_price * 0.65),
                "gap": round(((round_price(highest_price * 0.65) - latest_price) / latest_price) * 100, 2),
                "is_reached": bool(latest_price <= highest_price * 0.65),
                "color": "#06b6d4"
            },
            {
                "id": 3,
                "name": "3차 매수",
                "rate": 0.40,
                "label": "-40% (x0.60)",
                "price": round_price(highest_price * 0.60),
                "gap": round(((round_price(highest_price * 0.60) - latest_price) / latest_price) * 100, 2),
                "is_reached": bool(latest_price <= highest_price * 0.60),
                "color": "#10b981"
            },
            {
                "id": 4,
                "name": "4차 매수",
                "rate": 0.45,
                "label": "-45% (x0.55)",
                "price": round_price(highest_price * 0.55),
                "gap": round(((round_price(highest_price * 0.55) - latest_price) / latest_price) * 100, 2),
                "is_reached": bool(latest_price <= highest_price * 0.55),
                "color": "#f97316"
            },
            {
                "id": 5,
                "name": "5차 매수",
                "rate": 0.50,
                "label": "-50% (x0.50)",
                "price": round_price(highest_price * 0.50),
                "gap": round(((round_price(highest_price * 0.50) - latest_price) / latest_price) * 100, 2),
                "is_reached": bool(latest_price <= highest_price * 0.50),
                "color": "#ec4899"
            }
        ]

        # 종목 기본 정보
        stock_name = raw_ticker
        try:
            info = stock.info or {}
            stock_name = info.get("shortName") or info.get("longName") or raw_ticker
        except Exception:
            pass

        return jsonify({
            "success": True,
            "ticker": raw_ticker,
            "formatted_ticker": formatted_ticker,
            "stock_name": stock_name,
            "currency": currency_symbol,
            "is_krw": is_krw,
            "is_jpy": is_jpy,
            "highest_price": round_price(highest_price),
            "latest_price": round_price(latest_price),
            "drop_from_peak": round(drop_from_peak, 2),
            "candles": candles,
            "ma20": ma20_data,
            "ma50": ma50_data,
            "levels": levels
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"==================================================")
    print(f"🚀 Python Stock Analysis Server Running!")
    print(f"👉 Local URL: http://127.0.0.1:{port}")
    print(f"==================================================")
    app.run(host="0.0.0.0", port=port, debug=True)
