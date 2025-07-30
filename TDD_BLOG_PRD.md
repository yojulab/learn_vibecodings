# PRD: 블로그 게시물 관리 (TDD 접근법)

> 작성자: 켄트 벡 (TDD 컨설턴트)
>
> 이 문서는 '실패하는 테스트'를 먼저 정의하고, 그 테스트를 통과시키는 방식으로 기능을 완성해나가는 TDD(Test-Driven Development) 방법론에 따라 작성되었습니다. 모든 요구사항은 검증 가능한 테스트 시나리오 형태로 기술됩니다.

---

### **1. Vision & Core Feature**

- **Vision:** 사용자가 블로그 글을 등록하고 관리할 수 있는 안정적인 시스템을 구축한다.
- **Core Feature:** 게시물(Posts)에 대한 CRUD(Create, Read, Update, Delete) 기능을 제공하는 `/posts` API 및 관련 UI.

### **2. 기술 스택 (Tech Stack)**

- **Frontend:** Vue.js, 전체 스택을 TypeScript로 구성
- **Database:** MongoDB
- **UI E2E Test:** Playwright

---

### **3. API 테스트 시나리오 **

TDD 사이클: `Red` -> `Green` -> `Refactor` 를 각 시나리오에 적용합니다.

#### **Step 1: 가장 간단한 것부터 시작 - 목록 조회 (Read)**

- **User Story:** As a user, I want to see a list of all posts.
- **Scenario 3.1: 게시글이 하나도 없을 때**
  - **Test (Red):** `GET /posts`를 요청한다.
  - **Expected (Green):**
    - **Status Code:** `200 OK`
    - **Response Body:** `[]` (빈 JSON 배열)

#### **Step 2: 첫 기능 구현 - 생성 후 조회 (Create & Read)**

- **User Story:** As a user, I want to create a new post and see it in my list.
- **Scenario 3.2: 첫 게시글 생성**
  - **Test (Red):** `POST /posts`를 요청한다.
    - **Request Body:** `{"title": "첫 글", "content": "내용입니다"}`
  - **Expected (Green):**
    - **Status Code:** `201 Created`
    - **Response Body:** 시스템이 생성한 고유 `id`가 포함된 게시글 객체.
      ```json
      {
        "id": "unique_system_generated_id_1",
        "title": "첫 글",
        "content": "내용입니다"
      }
      ```
- **Scenario 3.3: 생성된 게시글 목록에서 확인**
  - **Test (Red):** (Scenario 3.2 성공 후) `GET /posts`를 다시 요청한다.
  - **Expected (Green):**
    - **Status Code:** `200 OK`
    - **Response Body:** 방금 생성한 게시글이 포함된 배열.
      ```json
      [
        {
          "id": "unique_system_generated_id_1",
          "title": "첫 글",
          "content": "내용입니다"
        }
      ]
      ```

#### **Step 3: 실패 시나리오 정의 - 유효성 검사 (Validation)**

- **User Story:** As a system, I want to reject invalid post submissions to ensure data integrity.
- **Scenario 3.4: 필수 필드(title) 누락 시**
  - **Test (Red):** `POST /posts`를 요청한다.
    - **Request Body:** `{"content": "내용만 있습니다"}`
  - **Expected (Green):**
    - **Status Code:** `422 Unprocessable Entity`
    - **Response Body:** `{"detail": "Title is a required field"}` (또는 유사한 명확한 에러 메시지)

#### **Step 4: 나머지 기능 정의 - 수정 및 삭제 (Update & Delete)**

- **User Story:** As a user, I want to be able to edit and remove my posts.
- **Scenario 3.5: 게시글 수정**
  - **Test (Red):** `PUT /posts/{existing_id}`를 요청한다.
    - **Request Body:** `{"title": "수정된 제목", "content": "수정된 내용"}`
  - **Expected (Green):**
    - **Status Code:** `200 OK`
    - **Response Body:** 수정된 내용이 반영된 전체 게시글 객체.
- **Scenario 3.6: 존재하지 않는 게시글 수정 시도**
  - **Test (Red):** `PUT /posts/{non_existent_id}`를 요청한다.
  - **Expected (Green):**
    - **Status Code:** `404 Not Found`
- **Scenario 3.7: 게시글 삭제**
  - **Test (Red):** `DELETE /posts/{existing_id}`를 요청한다.
  - **Expected (Green):**
    - **Status Code:** `204 No Content` (또는 `200 OK`와 성공 메시지)
- **Scenario 3.8: 삭제된 게시글 확인**
  - **Test (Red):** (Scenario 3.7 성공 후) `GET /posts/{existing_id}`를 다시 요청한다.
  - **Expected (Green):**
    - **Status Code:** `404 Not Found`

---

### **4. UI E2E 테스트 시나리오 (Playwright)**

사용자 관점의 End-to-End 시나리오입니다.

#### **Scenario 4.1: 새 글 작성부터 목록 확인까지 (Happy Path)**

- **Test (Red):**
  1. 사용자가 웹사이트에 접속하여 '글쓰기' 페이지로 이동한다.
  2. `title` 입력란에 "UI 테스트 제목"을 입력한다.
  3. `content` 입력란에 "UI 테스트 내용"을 입력한다.
  4. '저장' 버튼을 클릭한다.
- **Expected (Green):**
  1. 페이지가 게시글 목록('/')으로 리다이렉트된다.
  2. "게시글이 성공적으로 등록되었습니다." 와 같은 성공 메시지가 화면에 표시된다.
  3. 게시글 목록 최상단에 "UI 테스트 제목"을 가진 게시글이 보인다.

#### **Scenario 4.2: 목록에서 상세 페이지로 이동**

- **Test (Red):**
  1. 사용자가 게시글 목록 페이지에 접속한다.
  2. 특정 게시글의 제목("UI 테스트 제목")을 클릭한다.
- **Expected (Green):**
  1. 해당 게시글의 상세 페이지(`/posts/{id}`)로 이동한다.
  2. 페이지에 "UI 테스트 제목"과 "UI 테스트 내용"이 올바르게 표시된다.
