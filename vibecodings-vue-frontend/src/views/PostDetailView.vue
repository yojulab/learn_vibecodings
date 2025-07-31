<template>
  <div class="container mx-auto p-4">
    <div v-if="loading">Loading...</div>
    <div v-if="error" class="text-red-500">{{ error }}</div>
    <div v-if="post">
      <h1 class="text-4xl font-bold mb-2">{{ post.title }}</h1>
      <p class="text-gray-500 mb-4">Category: {{ post.category }}</p>
      <div class="prose max-w-none">
        {{ post.content }}
      </div>
      <div class="mt-8">
        <router-link :to="{ name: 'PostEdit', params: { id: post._id } }" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Edit
        </router-link>
        <button @click="deleteCurrentPost" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 ml-2">
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { postsApi, type Post } from '@/api/posts';

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
    error.value = 'Failed to fetch post.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});

async function deleteCurrentPost() {
  if (!post.value) return;
  if (confirm('Are you sure you want to delete this post?')) {
    try {
      await postsApi.deletePost(post.value._id);
      router.push({ name: 'PostList' });
    } catch (err) {
      error.value = 'Failed to delete post.';
      console.error(err);
    }
  }
}
</script>
