<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Blog Posts</h1>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-if="error" class="text-red-500 text-center">{{ error }}</div>
    <div v-if="posts.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <PostCard v-for="post in posts" :key="post._id" :post="post" />
    </div>
    <div v-else-if="!loading" class="text-center text-gray-500">
      No posts found.
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { postsApi, type Post } from '@/api/posts';
import PostCard from '@/components/PostCard.vue';

const posts = ref<Post[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await postsApi.getPosts();
    posts.value = response.data;
  } catch (err) {
    error.value = 'Failed to fetch posts.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>
