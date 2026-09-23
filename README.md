# 📈 Pro Entry Point Chart Analyzer (MU Default)

전문가용 주식 기술적 분석 및 전고점(ATH) 대비 역추세 분할 매수 타점 분석 웹 대시보드입니다.

## 🚀 주요 기능
1. **기본 차트 로드**: 마이크론 테크놀로지 (`NASDAQ:MU`) 기본 제공 및 다른 티커 검색 지원
2. **TradingView 실시간 차트 연동**: 실시간 캔들 차트, 이평선, 보조지표(RSI 등) 제공
3. **전고점 기준 분할 매수 지점 자동 계산 및 표시**:
   - **전고점 (ATH)**: 사용자 입력 및 기본값 설정 ($157.50)
   - **1차 매수 지점**: 전고점 대비 **-30%** 하락 지점 (권장 비중 15%)
   - **2차 매수 지점**: 전고점 대비 **-35%** 하락 지점 (권장 비중 20%)
   - **3차 매수 지점**: 전고점 대비 **-40%** 하락 지점 (권장 비중 20%)
   - **4차 매수 지점**: 전고점 대비 **-45%** 하락 지점 (권장 비중 25%)
   - **5차 매수 지점**: 전고점 대비 **-50%** 하락 지점 (권장 비중 20%)
4. **시각화 오버레이 & 타점 명세서**:
   - TradingView 실시간 모드 & 타점 수평선 오버레이 뷰 지원
   - 총 투자금액에 따른 각 차수별 매수 수량 및 예산 분배 자동 계산
   - 타점 클립보드 원클릭 복사 및 인쇄/PDF 기능

## 📂 파일 구조
- `entry_point.html`: 메인 분석 대시보드 단일 HTML 파일
- `index.html`: GitHub Pages 및 웹 호스팅 루트 접근 시 리다이렉션
- `README.md`: 프로젝트 설명 및 사용 가이드

## 🌐 GitHub 업로드 및 배포 방법

### 1. 로컬에서 첫 커밋 생성
```bash
git add .
git commit -m "feat: add entry_point.html chart analysis dashboard"
```

### 2. GitHub 원격 저장소 연결 후 푸시
```bash
git remote add origin https://github.com/<사용자명>/<저장소이름>.git
git branch -M main
git push -u origin main
```

### 3. GitHub Pages로 무료 웹 배포 (선택 사항)
1. GitHub 저장소의 **Settings** > **Pages** 이동
2. **Build and deployment**의 Source를 `Deploy from a branch`로 선택
3. Branch를 `main` / `(root)`로 설정 후 저장
4. 몇 분 후 `https://<사용자명>.github.io/<저장소이름>/entry_point.html` 로 어디서나 접속 가능
