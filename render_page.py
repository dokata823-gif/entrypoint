# -*- coding: utf-8 -*-
import json

with open("sentences.json", "r", encoding="utf-8") as f:
    sentences = json.load(f)

with open("qa_data.json", "r", encoding="utf-8") as f:
    qa = json.load(f)

# generate 187 list html
s_rows = []
for s in sentences:
    row = f"""<div class="sent-row">
  <div class="sent-num">#{s['id']} <span class="sent-tag">{s['tag']}</span></div>
  <div class="sent-ko">{s['ko']}</div>
  <div class="sent-en">{s['en']}</div>
</div>"""
    s_rows.append(row)

sentences_html = "\n".join(s_rows)

def make_card(item_id, item):
    return f"""
      <div class="q-card">
        <div class="q-card-header">
          <div>
            <span class="q-category">{item['cat']}</span>
            <div class="q-name">{item['name']}</div>
          </div>
          <span class="time-badge">{item['time']}</span>
        </div>

        <div class="prompt-box">
          <div class="prompt-label">❓ 사진 상황 / 질문 (문제)</div>
          <div class="prompt-text">{item['prompt']}</div>
        </div>

        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 187 만능 문장 조합 [한글 답안지]</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{item['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 모범 답안 (English Model Answer)</div>
            <div class="en-text">{item['en_ans']}</div>
          </div>
        </div>

        <div class="mapping-box">
          <div class="mapping-title">🎯 활용된 만능 문장 번호</div>
          {item['mapping']}
        </div>
      </div>
"""

p2_html = make_card("p2_1", qa["p2_1"]) + make_card("p2_2", qa["p2_2"]) + make_card("p2_3", qa["p2_3"])

p3_html = f"""
      <div class="q-card">
        <div class="q-card-header">
          <div>
            <span class="q-category">쇼핑 / 스마트폰 테마</span>
            <div class="q-name">세트 1. 온라인 쇼핑과 스마트폰 구매 습관</div>
          </div>
          <span class="time-badge">15초 / 15초 / 30초</span>
        </div>

        <!-- Q5 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q5 - 15초] 질문</div>
          <div class="prompt-text">{qa['p3_1_q5']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q5] 정해진 한글 답안</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p3_1_q5']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q5 Answer)</div>
            <div class="en-text">{qa['p3_1_q5']['en_ans']}</div>
          </div>
        </div>

        <!-- Q6 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q6 - 15초] 질문</div>
          <div class="prompt-text">{qa['p3_1_q6']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q6] 정해진 한글 답안</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p3_1_q6']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q6 Answer)</div>
            <div class="en-text">{qa['p3_1_q6']['en_ans']}</div>
          </div>
        </div>

        <!-- Q7 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q7 - 30초] 심화 질문</div>
          <div class="prompt-text">{qa['p3_1_q7']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q7] 30초 완성 한글 답안지</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p3_1_q7']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q7 Answer)</div>
            <div class="en-text">{qa['p3_1_q7']['en_ans']}</div>
          </div>
        </div>

        <div class="mapping-box">
          <div class="mapping-title">🎯 활용된 만능 문장 번호</div>
          {qa['p3_1_q7']['mapping']}
        </div>
      </div>

      <div class="q-card">
        <div class="q-card-header">
          <div>
            <span class="q-category">여가 / 힐링 / 장소 테마</span>
            <div class="q-name">세트 2. 여가 활동 및 새로운 장소 방문</div>
          </div>
          <span class="time-badge">15초 / 15초 / 30초</span>
        </div>

        <div class="prompt-box">
          <div class="prompt-label">❓ [Q7 - 30초] 심화 질문</div>
          <div class="prompt-text">{qa['p3_2_q7']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q7] 30초 완성 한글 답안지</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p3_2_q7']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q7 Answer)</div>
            <div class="en-text">{qa['p3_2_q7']['en_ans']}</div>
          </div>
        </div>

        <div class="mapping-box">
          <div class="mapping-title">🎯 활용된 만능 문장 번호</div>
          {qa['p3_2_q7']['mapping']}
        </div>
      </div>
"""

p4_html = f"""
      <div class="q-card">
        <div class="q-card-header">
          <div>
            <span class="q-category">컨퍼런스 / 세미나 일정표</span>
            <div class="q-name">세트 1. 글로벌 마케팅 컨퍼런스 일정 안내</div>
          </div>
          <span class="time-badge">15초 / 15초 / 30초</span>
        </div>

        <div class="prompt-box" style="border-left: 4px solid var(--accent-purple);">
          <div class="prompt-label">📋 주어진 일정표 요약</div>
          <div class="prompt-text" style="font-size: 0.88rem; color: #cbd5e1;">
            • 행사명: 2026 글로벌 마케팅 컨퍼런스 (6월 20일 / 힐튼 호텔)<br>
            • 09:00 AM: 참가자 등록 및 모닝커피 (1층 로비)<br>
            • 12:00 PM: 점심 식사 제공 (무료 제공)<br>
            • 01:00 PM: [워크숍] SNS 마케팅 전략 (강사: Ray Kingston)<br>
            • 02:30 PM: [토론] 스포츠 팬 마케팅 공략법 (강사: Kevin Delmont)<br>
            • 05:00 PM: 세미나 전체 일정 종료
          </div>
        </div>

        <!-- Q8 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q8 - 15초] 일시/장소 문의</div>
          <div class="prompt-text">{qa['p4_1_q8']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q8] 정해진 한글 답안</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p4_1_q8']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q8 Answer)</div>
            <div class="en-text">{qa['p4_1_q8']['en_ans']}</div>
          </div>
        </div>

        <!-- Q9 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q9 - 15초] 오정보 확인 문의 (만능 반박 패턴)</div>
          <div class="prompt-text">{qa['p4_1_q9']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q9] 정해진 한글 답안 (만능 반박 공식)</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p4_1_q9']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q9 Answer)</div>
            <div class="en-text">{qa['p4_1_q9']['en_ans']}</div>
          </div>
        </div>

        <!-- Q10 -->
        <div class="prompt-box">
          <div class="prompt-label">❓ [Q10 - 30초] 공통 항목 전체 안내 문의</div>
          <div class="prompt-text">{qa['p4_1_q10']['prompt']}</div>
        </div>
        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 [Q10] 30초 완성 한글 답안지</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">{qa['p4_1_q10']['ko_ans']}</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Q10 Answer)</div>
            <div class="en-text">{qa['p4_1_q10']['en_ans']}</div>
          </div>
        </div>

        <div class="mapping-box">
          <div class="mapping-title">🎯 활용된 만능 문장 번호</div>
          {qa['p4_1_q10']['mapping']}
        </div>
      </div>

      <!-- P4-2: 돌발 질문 -->
      <div class="q-card">
        <div class="q-card-header">
          <div>
            <span class="q-category">취소/변경 & 수강/면접 유형</span>
            <div class="q-name">세트 2. 일정 변경 안내 및 강좌/면접 필수 공식</div>
          </div>
          <span class="time-badge">필수 만능 패턴</span>
        </div>

        <div class="answer-box">
          <div class="answer-top-bar">
            <div class="answer-label">💡 Part 4 돌발 질문 대비 만능 한글 공식</div>
            <button class="btn-toggle-en" onclick="toggleEn(this)">🇺🇸 영어 원문 보기</button>
          </div>
          <div class="answer-content">• <strong>일정 취소/연기 문의 시:</strong> "면접 일정이 잡혀 있었으나 사정상 취소되었습니다." 또는 "화요일 회의가 금요일로 일정 변경되었습니다."
• <strong>수강료/마감일 문의 시:</strong> "유화 페인팅 클래스 수강료는 20달러이며, 정회원이시라면 무료입니다. 1월 3일까지 사전 등록을 완료하셔야 합니다."
• <strong>지원자 경력/자격 문의 시:</strong> "그녀는 디자인 석사 학위를 취득했고, 편집장으로 5년 이상의 경력을 쌓았기 때문에 충분한 자격을 갖추었습니다."</div>
          <div class="en-box">
            <div class="en-label">🇺🇸 영어 원문 (Part 4 Key Patterns)</div>
            <div class="en-text">• Schedule Cancellation / Rescheduling:
"There was supposed to be an interview, but it has been canceled."
"There was supposed to be a meeting with Jane White on Tuesday, but it has been rescheduled to Friday."

• Tuition Fee / Deadline:
"You have to pay $20 for the oil painting class, but if you are a member, it's free of charge. You should register by January 3rd."

• Candidate Qualifications:
"She got a master's degree in design, and she has worked as a chief editor for five years, so I think she is well qualified."</div>
          </div>
        </div>

        <div class="mapping-box">
          <div class="mapping-title">🎯 활용된 만능 문장 번호</div>
          취소/연기/변경 <span class="sent-tag">116, 117, 118번</span> + 수강료/마감일 <span class="sent-tag">130, 132, 133, 134번</span> + 학력/경력/자격 <span class="sent-tag">119, 121, 122, 128번</span>
        </div>
      </div>
"""

p5_html = make_card("p5_1", qa["p5_1"]) + make_card("p5_2", qa["p5_2"]) + make_card("p5_3", qa["p5_3"])

full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>토익스피킹 한글 문제 & 만능 답안 마스터 (Part 2 ~ Part 5)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-body: #0f141c;
      --bg-card: #18202c;
      --bg-subcard: #222d3d;
      --border-color: #2e3c50;
      --text-main: #d0d7de;
      --text-bright: #ffffff;
      --text-muted: #8b9bb0;
      --accent-blue: #58a6ff;
      --accent-green: #3fb950;
      --accent-yellow: #f1e05a;
      --accent-orange: #ffa657;
      --accent-purple: #d2a8ff;
      --accent-cyan: #39c5bb;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.7;
      font-size: 15.5px;
      padding-bottom: 90px;
      word-break: keep-all;
    }}

    /* Header */
    header {{
      background: #18202c;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 16px 12px 16px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}

    .badge-wrap {{
      display: flex;
      gap: 6px;
    }}

    .badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(88, 166, 255, 0.15);
      color: var(--accent-blue);
      border: 1px solid rgba(88, 166, 255, 0.3);
    }}

    .badge.green {{
      background: rgba(63, 185, 80, 0.15);
      color: var(--accent-green);
      border-color: rgba(63, 185, 80, 0.3);
    }}

    .badge.purple {{
      background: rgba(210, 168, 255, 0.15);
      color: var(--accent-purple);
      border-color: rgba(210, 168, 255, 0.3);
    }}

    h1 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-bright);
      line-height: 1.35;
      margin-bottom: 4px;
    }}

    .subtitle {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Global Toggle Button in Header */
    .global-btn-wrap {{
      margin-top: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}

    .btn-global-toggle {{
      background: rgba(88, 166, 255, 0.18);
      color: var(--accent-blue);
      border: 1px solid rgba(88, 166, 255, 0.4);
      padding: 5px 12px;
      border-radius: 8px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }}

    .btn-global-toggle:hover, .btn-global-toggle:active {{
      background: var(--accent-blue);
      color: #000;
    }}

    /* Mobile Quick Navigation */
    .nav-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding: 0;
      scrollbar-width: none;
    }}

    .nav-bar::-webkit-scrollbar {{
      display: none;
    }}

    .nav-btn {{
      flex: 0 0 auto;
      background: var(--bg-subcard);
      color: var(--text-main);
      border: 1px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 16px;
      font-size: 0.8rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s ease;
    }}

    .nav-btn:hover, .nav-btn:active {{
      background: var(--accent-blue);
      color: #000;
      border-color: var(--accent-blue);
    }}

    /* Container */
    .container {{
      max-width: 860px;
      margin: 0 auto;
      padding: 14px;
    }}

    /* Guide Box */
    .guide-banner {{
      background: linear-gradient(135deg, #182333 0%, #151d2a 100%);
      border: 1px solid #2d405b;
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 20px;
    }}

    .guide-title {{
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--accent-blue);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .guide-desc {{
      font-size: 0.85rem;
      color: var(--text-main);
      line-height: 1.55;
    }}

    /* Part Sections */
    .part-section {{
      margin-bottom: 36px;
      scroll-margin-top: 150px;
    }}

    .part-header {{
      background: linear-gradient(90deg, #222d3d 0%, #18202c 100%);
      border-left: 5px solid var(--accent-blue);
      border-radius: 0 10px 10px 0;
      padding: 12px 14px;
      margin-bottom: 16px;
    }}

    .part-header.p2 {{ border-left-color: #ffa657; }}
    .part-header.p3 {{ border-left-color: #3fb950; }}
    .part-header.p4 {{ border-left-color: #d2a8ff; }}
    .part-header.p5 {{ border-left-color: #58a6ff; }}

    .part-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text-bright);
    }}

    .part-summary {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* Question Cards */
    .q-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 18px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }}

    .q-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 8px;
      gap: 8px;
    }}

    .q-category {{
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--accent-orange);
      background: rgba(255, 166, 87, 0.12);
      padding: 2px 7px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 4px;
    }}

    .q-name {{
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--text-bright);
    }}

    .time-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-yellow);
      background: rgba(241, 224, 90, 0.12);
      padding: 3px 7px;
      border-radius: 6px;
      white-space: nowrap;
    }}

    /* Question Prompt Box */
    .prompt-box {{
      background: #151c27;
      border: 1px solid #27364a;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 12px;
    }}

    .prompt-label {{
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--accent-yellow);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .prompt-text {{
      font-size: 0.92rem;
      font-weight: 600;
      color: #e2e8f0;
      line-height: 1.55;
    }}

    /* Answer Box */
    .answer-box {{
      background: #0f1c19;
      border: 1px solid #1c4035;
      border-left: 4px solid var(--accent-green);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 12px;
    }}

    .answer-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .answer-label {{
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--accent-green);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* Toggle Button */
    .btn-toggle-en {{
      background: #1e3a32;
      color: #a7f3d0;
      border: 1px solid #2d6a4f;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s ease;
    }}

    .btn-toggle-en:hover, .btn-toggle-en:active {{
      background: #2d6a4f;
      color: #ffffff;
    }}

    .btn-toggle-en.active {{
      background: var(--accent-blue);
      color: #000000;
      border-color: var(--accent-blue);
    }}

    .answer-content {{
      font-size: 0.95rem;
      color: #d1fae5;
      line-height: 1.75;
      font-weight: 500;
      white-space: pre-line;
    }}

    .step-badge {{
      display: inline-block;
      font-size: 0.76rem;
      font-weight: 800;
      color: #10b981;
      background: rgba(16, 185, 129, 0.15);
      padding: 1px 5px;
      border-radius: 4px;
      margin-right: 4px;
    }}

    /* English Original Text Box (Toggled) */
    .en-box {{
      display: none;
      background: #141c2b;
      border: 1px dashed var(--accent-blue);
      border-radius: 8px;
      padding: 12px 14px;
      margin-top: 10px;
      animation: fadeIn 0.25s ease-in-out;
    }}

    .en-box.show {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .en-label {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--accent-blue);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .en-text {{
      font-size: 0.9rem;
      color: #e2e8f0;
      line-height: 1.65;
      font-weight: 500;
      white-space: pre-line;
    }}

    /* Sentence Numbers Footnote / Mapping */
    .mapping-box {{
      background: var(--bg-subcard);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .mapping-title {{
      font-weight: 700;
      color: var(--accent-purple);
      margin-bottom: 3px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .sent-tag {{
      color: var(--accent-purple);
      font-weight: 700;
      background: rgba(210, 168, 255, 0.12);
      padding: 1px 5px;
      border-radius: 4px;
      margin: 0 2px;
      display: inline-block;
    }}

    /* Sticky Bottom Quick Index */
    .footer-nav {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(24, 32, 44, 0.96);
      border-top: 1px solid var(--border-color);
      padding: 8px 12px;
      display: flex;
      justify-content: space-around;
      z-index: 99;
      backdrop-filter: blur(8px);
    }}

    .f-nav-item {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.75rem;
      font-weight: 700;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }}

    .f-nav-item:active {{
      color: var(--accent-blue);
    }}

    /* Accordion Style for 187 List */
    details {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 12px 14px;
      margin-top: 16px;
    }}

    summary {{
      font-weight: 800;
      color: var(--accent-yellow);
      cursor: pointer;
      font-size: 0.92rem;
      outline: none;
    }}

    .sentence-mini-list {{
      margin-top: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .sent-row {{
      padding: 10px 12px;
      background: var(--bg-subcard);
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }}

    .sent-num {{
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--accent-blue);
      margin-bottom: 3px;
    }}

    .sent-tag {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-left: 6px;
    }}

    .sent-ko {{
      font-size: 0.94rem;
      font-weight: 700;
      color: #94d2bd;
      line-height: 1.45;
      margin-bottom: 2px;
    }}

    .sent-en {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-top">
      <div class="badge-wrap">
        <span class="badge">한글 눈독(目讀) 학습</span>
        <span class="badge green">187개 만능문장 공식</span>
        <span class="badge purple">영어 원문 토글 기능</span>
      </div>
      <span style="font-size: 0.75rem; color: var(--text-muted);">📱 모바일 원페이지</span>
    </div>
    <h1>토익스피킹 한글 문제 & 만능 답안지</h1>
    <p class="subtitle">질문 유형과 정해진 한글 답안 흐름을 눈으로 보며 통째로 익히는 암기노트</p>

    <!-- Global English Toggle & Nav -->
    <div class="global-btn-wrap">
      <div class="nav-bar">
        <a href="#p2" class="nav-btn">🖼️ Part 2</a>
        <a href="#p3" class="nav-btn">💬 Part 3</a>
        <a href="#p4" class="nav-btn">📊 Part 4</a>
        <a href="#p5" class="nav-btn">💡 Part 5</a>
        <a href="#sent-all" class="nav-btn">📚 187 문장</a>
      </div>
      <button class="btn-global-toggle" id="btn-toggle-all" onclick="toggleAllEn()">🇺🇸 전체 영어 보기</button>
    </div>
  </header>

  <!-- Main Container -->
  <main class="container">

    <!-- Guide Banner -->
    <div class="guide-banner">
      <div class="guide-title">📖 한글 눈독(目讀) 학습법</div>
      <div class="guide-desc">
        1. 질문 상황(문제)을 한글로 읽고 <strong>[187개 문장 조합 한글 답안지]</strong>를 눈으로 먼저 익힙니다.<br>
        2. 답안지 상단의 <strong>[🇺🇸 영어 원문 보기]</strong> 버튼을 누르면 영어 문장을 대조하며 학습할 수 있습니다.
      </div>
    </div>

    <!-- PART 2 -->
    <section id="p2" class="part-section">
      <div class="part-header p2">
        <div class="part-title">Part 2. 사진 묘사 (Q3 ~ Q4)</div>
        <div class="part-summary">준비 45초 / 답변 30초 | [장소] → [중심 인물] → [위치/동작] → [복장] → [주변/배경]</div>
      </div>
      {p2_html}
    </section>

    <!-- PART 3 -->
    <section id="p3" class="part-section">
      <div class="part-header p3">
        <div class="part-title">Part 3. 일상 대화 질문 응답 (Q5 ~ Q7)</div>
        <div class="part-summary">준비 0초 / 답변 Q5(15초), Q6(15초), Q7(30초) | [바쁜 직장인/예산 한계] + [가성비/시간절약] + [스마트폰 편리성]</div>
      </div>
      {p3_html}
    </section>

    <!-- PART 4 -->
    <section id="p4" class="part-section">
      <div class="part-header p4">
        <div class="part-title">Part 4. 제공된 정보 보고 답변하기 (Q8 ~ Q10)</div>
        <div class="part-summary">준비 45초 / 답변 Q8(15초), Q9(15초), Q10(30초) | [행사 일시/장소] → [잘못된 정보 정정] → [2개 세션 묶어 상세 안내]</div>
      </div>
      {p4_html}
    </section>

    <!-- PART 5 -->
    <section id="p5" class="part-section">
      <div class="part-header p5">
        <div class="part-title">Part 5. 1분 의견 제시하기 (Q11)</div>
        <div class="part-summary">준비 45초 / 답변 60초 | [입장 표명] → [본론 1: 핵심 근거 1] → [본론 2: 핵심 근거 2] → [결론]</div>
      </div>
      {p5_html}
    </section>

    <!-- 187 SENTENCES -->
    <section id="sent-all" style="margin-top: 30px;">
      <details>
        <summary>📚 187개 만능 한글 문장 전체 리스트 보기 (클릭하여 펼치기)</summary>
        <div class="sentence-mini-list" id="full-list-container">
          {sentences_html}
        </div>
      </details>
    </section>

  </main>

  <!-- Sticky Footer Navigation -->
  <div class="footer-nav">
    <a href="#p2" class="f-nav-item">
      <span style="font-size: 1.1rem;">🖼️</span>
      <span>Part 2</span>
    </a>
    <a href="#p3" class="f-nav-item">
      <span style="font-size: 1.1rem;">💬</span>
      <span>Part 3</span>
    </a>
    <a href="#p4" class="f-nav-item">
      <span style="font-size: 1.1rem;">📊</span>
      <span>Part 4</span>
    </a>
    <a href="#p5" class="f-nav-item">
      <span style="font-size: 1.1rem;">💡</span>
      <span>Part 5</span>
    </a>
    <a href="#sent-all" class="f-nav-item">
      <span style="font-size: 1.1rem;">📚</span>
      <span>187 문장</span>
    </a>
  </div>

  <!-- JavaScript for Toggle -->
  <script>
    // Toggle Single English Box
    function toggleEn(btn) {{
      const answerBox = btn.closest('.answer-box');
      const enBox = answerBox.querySelector('.en-box');
      if (!enBox) return;

      const isShowing = enBox.classList.contains('show');
      if (isShowing) {{
        enBox.classList.remove('show');
        btn.classList.remove('active');
        btn.innerText = '🇺🇸 영어 원문 보기';
      }} else {{
        enBox.classList.add('show');
        btn.classList.add('active');
        btn.innerText = '🔒 영어 원문 숨기기';
      }}
    }}

    // Toggle All English Boxes
    let allEnVisible = false;
    function toggleAllEn() {{
      allEnVisible = !allEnVisible;
      const allEnBoxes = document.querySelectorAll('.en-box');
      const allBtns = document.querySelectorAll('.btn-toggle-en');
      const globalBtn = document.getElementById('btn-toggle-all');

      allEnBoxes.forEach(box => {{
        if (allEnVisible) {{
          box.classList.add('show');
        }} else {{
          box.classList.remove('show');
        }}
      }});

      allBtns.forEach(btn => {{
        if (allEnVisible) {{
          btn.classList.add('active');
          btn.innerText = '🔒 영어 원문 숨기기';
        }} else {{
          btn.classList.remove('active');
          btn.innerText = '🇺🇸 영어 원문 보기';
        }}
      }});

      if (allEnVisible) {{
        globalBtn.innerText = '🔒 전체 영어 숨기기';
        globalBtn.style.background = 'var(--accent-blue)';
        globalBtn.style.color = '#000';
      }} else {{
        globalBtn.innerText = '🇺🇸 전체 영어 보기';
        globalBtn.style.background = 'rgba(88, 166, 255, 0.18)';
        globalBtn.style.color = 'var(--accent-blue)';
      }}
    }}
  </script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

with open("entry_point.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated index.html and entry_point.html with English toggle buttons successfully!")
