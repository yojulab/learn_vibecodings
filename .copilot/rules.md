# Copilot AI 코드 작성 및 협업 규칙

## 공통 규칙
- 모든 코드, 문서, 커밋 메시지는 명확하고 일관성 있게 작성합니다.
- 코드 변경 시 관련 문서(README, 주석 등)도 함께 최신화합니다.
- 민감 정보(비밀번호, API 키 등)는 코드에 직접 작성하지 않고 환경 변수(.env)로 관리합니다.

## 백엔드(Python)
- PEP8 스타일 가이드 준수
- 라우터, 모델, DB, 유틸리티는 각 디렉터리(app/routers, app/models 등)로 분리
- 함수, 변수, 클래스명은 snake_case, PascalCase 등 Python 컨벤션 준수
- 테스트 파일은 test_*.py 네이밍

## 프론트엔드(Vue)
- 컴포넌트는 PascalCase로 작성, 1파일 1컴포넌트 원칙
- 뷰(View)는 페이지 단위, 컴포넌트는 재사용 단위로 구분
- API 호출은 services/api.js에서만 처리
- 상태 관리는 stores/에서 관리
- 스타일은 Tailwind CSS 사용, 전역 스타일은 assets/main.css에 작성

## 기타
- 로그, 캐시, 환경설정 등 불필요한 파일은 .gitignore에 추가
- 컨테이너 환경(Dockerfile) 및 환경설정 파일은 루트에 위치
- README, LICENSE, 문서화 파일 유지

---

> 본 규칙은 Copilot AI 및 모든 개발자가 항상 참고해야 하며, 변경 시 팀원과 협의 후 업데이트합니다.
