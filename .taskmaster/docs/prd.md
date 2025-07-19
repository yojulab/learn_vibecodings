# learn_vibecodings

Starting interactive model setup...

🎯 Interactive Model Setup
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Navigation tips:
   • Type to search and filter options
   • Use ↑↓ arrow keys to navigate results
   • Standard models are listed first, custom providers at bottom
   • Press Enter to select

✔ Select the main model for generation/updates: gemini-cli/gemini-2.5-pro
✔ Select the research model: gemini-cli/gemini-2.5-pro
✔ Select the fallback model (optional): gemini-cli/gemini-2.5-pro

## 1차 프롬프트
'''markdown
연구소 소개 웹 PRD문서를 전문가 수준으로 작성

## 요구사항

﻿﻿헤더와 푸터가 없는 원페이지 랜딩페이지

메뉴 : 연구소 소개, 주요 서비스

﻿﻿모던한 UI/UX

﻿﻿생동감있는 트랜지션 효과

﻿﻿TailwindCSS사용

## 메뉴 주요 내용

연구소 소개 : 우주 존재하는 모든 것들을 위한 연구

주요 서비스 : 노년 연금 보험 자동 설계, 독서 돕는 도움 플랫폼, 강의 계획 자동 작성
'''

### 2차 프롬프트
'''markdown
작성한 PRD 내용을 아래 형식 맞게 수정

---------
.taskmaster/templates/example_prd.txt 내용
'''