## 환경 설정
```bash
~# task-master init
~# vi .env
~# task-master
~# task-master parse-prd
~# task-master list
~# task-master analyze-complexity --threshold=10
~# task-master complexity-report
~# task-master set-status --id=1 --status=deferred
~# task-master expand --id=4
~# task-master list --with-subtasks
```

## 프롬프트 예시

### 1차 프롬프트
```prompt
애자일 방법론 으로 수정
- frontend : Vue3 + Vite + TailwindCSS 등 활용
- backend : fastapi + pydandic v2 등 활용
- TailwindCSS는 PostCSS 기반으로 구성되며, Vite는 ESM과 빠른 HMR을 지원하는 번들러로 사용
- TDD 방식은 제외

[ 기존 예시 ]
당신은 다양한 문제 해결 통찰을 가진 TDD 전문가 켄트벡입니다.

전문가로서 TDD 접근 과정에서 일반 개발자보다 세부적인 단계들이 있을 것입니다.

요구 사항을 분석해 TDD 기법으로 vibe coding 할 수 있는 PRD 를 작성하려고 합니다.

기능이나 앱 구현 시 TDD 전문가로서 step by step 으로 문답 형식으로 필요 사항을 채워 PRD를 완성해 주세요.

[요구 사항]
| 단계 | 대화 내용 | 결과물 |
|------|----------|--------|
| **Vision** | "사용자가 블로그 글을 등록하고 관리할 수 있도록 한다" | 요구사항 정의 |
| **Ideation** | "/posts API 설계, CRUD 명세 작성해줘" | API 명세서, ERD |
| **Build** | "FastAPI로 CRUD 작성, Vue로 폼 구성해줘, mongoDB 사용(호스트명 : db_mongodb)" | 실행 가능한 코드 |
| **Evaluation** | "Pytest로 테스트, 성능 최적화해줘, Playwright로 headless로 UI 테스트 후 배포" | 테스트 코드, 배포 준비 |

```

### 2차 프롬프트
```prompt
지금까지 정리한 사항을 아래 형식 맞게 작성

[ 형식 ]
<context>
# Overview  
[Provide a high-level overview of your product here. Explain what problem it solves, who it's for, and why it's valuable.]

# Core Features  
[List and describe the main features of your product. For each feature, include:
- What it does
- Why it's important
- How it works at a high level]

# User Experience  
[Describe the user journey and experience. Include:
- User personas
- Key user flows
- UI/UX considerations]
</context>
<PRD>
# Technical Architecture  
[Outline the technical implementation details:
- System components
- Data models
- APIs and integrations
- Infrastructure requirements]

# Development Roadmap  
[Break down the development process into phases:
- MVP requirements
- Future enhancements
- Do not think about timelines whatsoever -- all that matters is scope and detailing exactly what needs to be build in each phase so it can later be cut up into tasks]

# Logical Dependency Chain
[Define the logical order of development:
- Which features need to be built first (foundation)
- Getting as quickly as possible to something usable/visible front end that works
- Properly pacing and scoping each feature so it is atomic but can also be built upon and improved as development approaches]

# Risks and Mitigations  
[Identify potential risks and how they'll be addressed:
- Technical challenges
- Figuring out the MVP that we can build upon
- Resource constraints]

# Appendix  
[Include any additional information:
- Research findings
- Technical specifications]
</PRD>
```