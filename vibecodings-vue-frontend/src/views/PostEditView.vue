<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Edit Post</h1>
    <div v-if="loading">Loading...</div>
    <div v-if="error" class="text-red-500">{{ error }}</div>
    <PostForm v-if="post" :post="post" @submit="updatePost" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import PostForm from '@/components/PostForm.vue';
import { postsApi, type Post, type PostUpdate } from '@/api/posts';

const route = useRoute();
const router = useRouter();
const post = ref<Post | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

const postId = route.params.id as string;

onMounted(async () => {
  try {
    const response = await postsApi.getPost(postId);
    post.value = response.data;
  } catch (err) {
    error.value = 'Failed to fetch post details.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});

async function updatePost(postData: PostUpdate) {
  try {
    const response = await postsApi.updatePost(postId, postData);
    router.push({ name: 'PostDetail', params: { id: response.data._id } });
  } catch (err) {
    error.value = 'Failed to update post.';
    console.error(err);
  }
}
</script>
