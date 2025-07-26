# learn_vibecodings

## 1차 프롬프트
'''markdown
연구소 소개 웹 PRD문서를 전문가 수준 작성
*  헤더와 푸터가 없는 원페이지 랜딩페이지
*  메뉴 : 연구소 소개, 주요 서비스  
* 모던한 UI/UX 구성과 생동감 있는 트랜지션 효과 

## 메뉴 주요 내용 
* 연구소 소개 : 우주 존재하는 모든 것들을 위한 연구  
* 주요 서비스 : 노년 연금 보험 자동 설계, 독서 돕는 도움 플랫폼, 강의 계획 자동 작성

## 기술 스팩
*  TailwindCSS사용
* 개발은 TDD 방식으로 playwright 사용
* FrontendVue 3 + Vite + TypeScriptComposition API, PiniaRouterVue RouterNavigation guards 활용
* Auth 관리Pinia + Axios Interceptor토큰 저장 및 재요청 처리
* MiddlewareVue Router Guard + 서버 미들웨어사용자 인증/권한 검사BackendVite + Fastify (or Express) + TypeScript백엔드도 Vite로 번들링 가능Auth 인증JWT (access/refresh)혹은 OAuth2 / 세션 등DBPostgreSQL / MySQLPrisma or TypeORM 사용ORMPrisma (Type-safe)DB 마이그레이션 포함
'''

### 2차 프롬프트
'''markdown
작성한 PRD 내용을 아래 형식 맞게 수정

---------
.taskmaster/templates/example_prd.txt 내용
'''

## task master Commands
```bash
~# tm init
~# tm parse-prd
~# tm list
~# tm show [number]
~# tm analyze-complexity
~# tm list
~# tm complexity-report
~# tm  expand --all
~# tm list --with-subtasks
~# tm next
```