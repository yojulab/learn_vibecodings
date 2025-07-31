<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Create New Post</h1>
    <PostForm @submit="createPost" />
    <p v-if="error" class="text-red-500 mt-4">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import PostForm from '@/components/PostForm.vue';
import { postsApi, type PostCreate } from '@/api/posts';

const router = useRouter();
const error = ref<string | null>(null);

async function createPost(postData: PostCreate) {
  try {
    const response = await postsApi.createPost(postData);
    router.push({ name: 'PostDetail', params: { id: response.data._id } });
  } catch (err) {
    error.value = 'Failed to create post.';
    console.error(err);
  }
}
</script>
