<template>
  <div class="border rounded-lg p-4 shadow-md hover:shadow-lg transition-shadow">
    <h2 class="text-xl font-semibold mb-2">{{ post.title }}</h2>
    <p class="text-gray-600 mb-2">Category: {{ post.category }}</p>
    <p class="text-gray-800 truncate">{{ post.content }}</p>
    <router-link :to="{ name: 'PostDetail', params: { id: post._id } }" class="text-blue-500 hover:underline mt-4 inline-block">
      Read More
    </router-link>
  </div>
</template>

<script setup lang="ts">
import type { Post } from '@/api/posts';

defineProps<{
  post: Post;
}>();
</script>
