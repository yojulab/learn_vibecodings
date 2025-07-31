# Gemini Project Context

# PRD (Product Requirements Document): Vibe Coding Blog

이 문서는 'vibe coding' 블로그 프로젝트의 기능 요구사항을 정의합니다. 애자일 원칙에 따라 점진적으로 업데이트됩니다.

## 1. 글(Post) 관리 기능

### 1.1. 글 작성 (Create Post)

- **API Endpoint:** `POST /posts`
- **사용자 스토리:** "관리자(admin)로서, 새로운 글을 작성하여 블로그에 콘텐츠를 추가할 수 있다."

#### **요구사항 (Requirements):**

1.  **인증 (Authentication):**
    *   오직 `admin` 권한을 가진 사용자만 글을 작성할 수 있습니다.
    *   요청 시 `Authorization: Bearer <JWT>` 헤더를 통해 인증 토큰을 전달받아 유효성을 검증해야 합니다.

2.  **데이터 모델 (Data Model):**
    *   `Post`는 다음 필드를 포함해야 합니다.
        *   `id`: (자동 생성) 고유 식별자 (MongoDB `_id`)
        *   `title`: (String, 필수) 글 제목
        *   `content`: (String, 필수) 글 내용 (Markdown 형식)
        *   `createdAt`: (Date, 자동 생성) 생성 일시
        *   `updatedAt`: (Date, 자동 생성) 최종 수정 일시

3.  **유효성 검사 (Validation):**
    *   `title` 필드는 비어있을 수 없습니다. (최대 255자)
    *   `content` 필드는 비어있을 수 없습니다.

#### **API 응답 (API Response):**

*   **성공 (201 Created):**
    *   글 작성이 성공하면, HTTP 상태 코드 `201 Created`와 함께 생성된 글의 전체 JSON 객체를 반환합니다.
    ```json
    {
      "id": "60d21b4667d0d8992e610c85",
      "title": "새로운 글 제목",
      "content": "## 마크다운 내용입니다.",
      "createdAt": "2025-07-31T10:00:00.000Z",
      "updatedAt": "2025-07-31T10:00:00.000Z"
    }
    ```
*   **실패:**
    *   **400 Bad Request:** `title` 또는 `content`가 누락된 경우
    *   **401 Unauthorized:** 인증 토큰이 없거나 유효하지 않은 경우

#### **검증 기준 (Acceptance Criteria):**

1.  `admin` 사용자가 유효한 `title`과 `content`를 담아 `POST /posts`를 요청하면, 새로운 글이 데이터베이스에 저장되어야 한다.
2.  요청 성공 시, 응답으로 상태 코드 `201`과 생성된 글의 정보가 반환되어야 한다.
3.  `title`이나 `content` 없이 요청하면, 상태 코드 `400`과 함께 오류 메시지가 반환되어야 한다.
4.  인증되지 않은 사용자가 요청하면, 상태 코드 `401`이 반환되어야 한다.
5.  Playwright를 이용한 E2E 테스트: 관리자가 로그인 후, 글쓰기 페이지로 이동하여 제목과 내용을 입력하고 '저장' 버튼을 눌렀을 때, "글이 성공적으로 등록되었습니다."와 같은 피드백을 받고, 작성된 글로 이동하거나 글 목록에서 확인할 수 있어야 한다.

---