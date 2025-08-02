# Project Rules and Reference (rules.md)

## 1. 프로젝트 구조
- **backend/**: Python FastAPI 기반 백엔드
  - `app/`: FastAPI 앱 루트
    - `main.py`: FastAPI 엔트리포인트
    - `models/`: 데이터 모델 정의
    - `routes/`: API 라우트 정의
    - `services/`: 서비스 로직
- **frontend/**: React + Vite + Tailwind 기반 프론트엔드
  - `src/`: React 소스
  - `public/`: 정적 파일

## 2. 개발 규칙
- **백엔드**
  - FastAPI 표준 구조 준수 (`app/main.py`, `app/models/`, `app/routes/`, `app/services/`)
  - 라우트는 `routes/`에, 데이터 모델은 `models/`에, 비즈니스 로직은 `services/`에 분리
  - Pydantic 모델 사용 권장
  - 라우트 함수에는 타입 힌트 명확히 작성
- **프론트엔드**
  - React 함수형 컴포넌트 사용
  - 스타일링은 Tailwind CSS 우선 적용
  - 상태 관리는 useState, useEffect 등 React 내장 훅 우선
  - 컴포넌트/에셋은 `src/` 하위에 정리

## 3. 커밋 및 작업 흐름
- Taskmaster 기반 태스크 관리 (tasks.json, subtasks, status 등)
- 구현 전 task 세부 내용/계획을 태스크에 기록 (update_subtask 등 활용)
- 구현 후 규칙/패턴 발견 시 rules.md 갱신
- 커밋 메시지: feat/fix/chore 등 Conventional Commits 스타일 권장

## 4. 기타 참고사항
- .env, .taskmaster/config.json 등 민감 정보는 git에 커밋하지 않음
- PRD 기반 태스크 생성 및 관리 권장
- 반복되는 코드 패턴, 에러, 베스트프랙티스 발견 시 rules.md에 추가

---

> 본 파일은 프로젝트 구조, 개발 규칙, 작업 흐름, 반복 패턴 등 구현에 참조할 내용을 정리합니다. 새로운 규칙이나 패턴 발견 시 이 파일을 업데이트하세요.
