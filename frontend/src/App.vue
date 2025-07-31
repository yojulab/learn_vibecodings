<template>
  <div id="app">
    <div class="container">
      <div class="form-section">
        <h1>{{ isEditing ? '블로그 글 수정' : '블로그 글 작성' }}</h1>
        <form @submit.prevent="submitPost">
          <div>
            <label for="title">제목:</label>
            <input type="text" id="title" v-model="post.title" required />
          </div>
          <div>
            <label for="content">내용 (Markdown):</label>
            <textarea id="content" v-model="post.content" required></textarea>
          </div>
          <button type="submit">{{ isEditing ? '업데이트' : '저장' }}</button>
          <button type="button" v-if="isEditing" @click="cancelEdit">취소</button>
        </form>
        <p v-if="message" data-testid="message-paragraph">{{ message }}</p>
      </div>

      <div class="list-section">
        <h2>글 목록</h2>
        <ul>
          <li v-for="p in posts" :key="p._id">
            <span>{{ p.title }}</span>
            <div class="buttons">
              <button @click="editPost(p)">수정</button>
              <button @click="deletePost(p._id)">삭제</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Post {
  _id: string;
  title: string;
  content: string;
}

const API_URL = 'http://localhost:3000/posts';

const post = ref({
  _id: '',
  title: '',
  content: '',
});

const posts = ref<Post[]>([]);
const message = ref('');
const isEditing = ref(false);

const fetchPosts = async () => {
  try {
    const response = await axios.get(API_URL);
    posts.value = response.data;
  } catch (error) {
    console.error('글 목록을 불러오는 데 실패했습니다.', error);
  }
};

const resetForm = () => {
  post.value = { _id: '', title: '', content: '' };
  isEditing.value = false;
};

const submitPost = async () => {
  try {
    if (isEditing.value) {
      // Update
      const { _id, ...updateData } = post.value;
      const response = await axios.patch(`${API_URL}/${_id}`, updateData);
      message.value = `글이 성공적으로 수정되었습니다. (ID: ${response.data._id})`;
    } else {
      // Create
      const response = await axios.post(API_URL, { title: post.value.title, content: post.value.content });
      message.value = `글이 성공적으로 등록되었습니다. (ID: ${response.data._id})`;
    }
    resetForm();
    await fetchPosts();
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      message.value = `오류 발생: ${JSON.stringify(error.response.data.message)}`;
    } else {
      message.value = '알 수 없는 오류가 발생했습니다.';
    }
    console.error(error);
  }
};

const editPost = (p: Post) => {
  isEditing.value = true;
  post.value = { ...p };
  message.value = '';
};

const cancelEdit = () => {
  resetForm();
  message.value = '';
};

const deletePost = async (id: string) => {
  if (!confirm('정말로 이 글을 삭제하시겠습니까?')) return;
  try {
    await axios.delete(`${API_URL}/${id}`);
    message.value = '글이 성공적으로 삭제되었습니다.';
    await fetchPosts();
  } catch (error) {
    message.value = '글 삭제 중 오류가 발생했습니다.';
    console.error(error);
  }
};

onMounted(() => {
  fetchPosts();
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin: 60px;
}
.container {
  display: flex;
  gap: 40px;
}
.form-section, .list-section {
  width: 50%;
}
form div {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
}
input[type="text"],
textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
textarea {
  height: 200px;
}
button {
  padding: 10px 15px;
  border: none;
  cursor: pointer;
  margin-right: 5px;
}
button[type="submit"] {
  background-color: #42b983;
  color: white;
}
button[type="button"] {
  background-color: #ccc;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px;
  border-bottom: 1px solid #ccc;
}
.buttons button {
  padding: 5px 10px;
}
</style>