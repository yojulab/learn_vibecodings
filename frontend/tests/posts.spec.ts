import { test, expect } from '@playwright/test';

const FRONTEND_URL = 'http://localhost:5173';
const API_URL = 'http://localhost:3000/posts';

test.describe('Posts CRUD Operations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(FRONTEND_URL);
    await page.waitForSelector('h1');
  });

  test('should allow a user to create, edit, and delete a post', async ({ page }) => {
    const uniqueTitle = `새로운 테스트 글 ${Date.now()}`;
    const updatedTitle = `수정된 테스트 글 ${Date.now()}`;
    const content = '이것은 테스트 내용입니다.';

    // ** 1. 글 작성 (Create) **
    await page.fill('input[id="title"]', uniqueTitle);
    await page.fill('textarea[id="content"]', content);
    
    const createResponsePromise = page.waitForResponse(response => 
      response.url().startsWith(API_URL) && response.status() === 201
    );
    await page.click('button[type="submit"]');
    await createResponsePromise;

    await expect(page.locator('[data-testid="message-paragraph"]')).toContainText('성공적으로 등록되었습니다');
    // 목록에 특정 li 요소가 나타날 때까지 대기
    await expect(page.locator('li', { hasText: uniqueTitle })).toBeVisible();

    // ** 2. 글 수정 (Update) **
    const postListItem = page.locator('li', { hasText: uniqueTitle });
    await postListItem.locator('button', { hasText: '수정' }).click();

    await expect(page.locator('input[id="title"]')).toHaveValue(uniqueTitle);
    await expect(page.locator('textarea[id="content"]')).toHaveValue(content);

    await page.fill('input[id="title"]', updatedTitle);
    
    const updateResponsePromise = page.waitForResponse(response =>
      response.url().includes(API_URL) && response.request().method() === 'PATCH' && response.status() === 200
    );
    await page.click('button[type="submit"]');
    await updateResponsePromise;

    await expect(page.locator('[data-testid="message-paragraph"]')).toContainText('성공적으로 수정되었습니다');
    // 수정된 제목을 가진 li가 보이는지 확인
    await expect(page.locator('li', { hasText: updatedTitle })).toBeVisible();
    // 이전 제목을 가진 li는 보이지 않는지 확인
    await expect(page.locator('li', { hasText: uniqueTitle })).not.toBeVisible();

    // ** 3. 글 삭제 (Delete) **
    const updatedPostListItem = page.locator('li', { hasText: updatedTitle });
    
    page.on('dialog', dialog => dialog.accept());

    const deleteResponsePromise = page.waitForResponse(response =>
      response.url().includes(API_URL) && response.request().method() === 'DELETE' && response.status() === 200
    );
    await updatedPostListItem.locator('button', { hasText: '삭제' }).click();
    await deleteResponsePromise;

    await expect(page.locator('[data-testid="message-paragraph"]')).toContainText('성공적으로 삭제되었습니다');
    // 삭제된 제목을 가진 li가 더 이상 보이지 않는지 확인
    await expect(page.locator('li', { hasText: updatedTitle })).not.toBeVisible();
  });
});
