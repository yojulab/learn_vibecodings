<template>
  <div id="app" class="bg-gray-100 min-h-screen">
    <nav class="bg-white shadow-md">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center py-4">
          <router-link to="/" class="text-2xl font-bold text-gray-800">VibeCodings Blog</router-link>
          <div>
            <router-link to="/" class="text-gray-600 hover:text-gray-800 px-3 py-2">Home</router-link>
            <router-link to="/post/new" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 ml-4">
              New Post
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script>

<style>
/* 전역 스타일을 여기에 추가할 수 있습니다. */
</style>
