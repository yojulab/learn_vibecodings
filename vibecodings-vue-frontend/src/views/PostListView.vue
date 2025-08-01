<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const posts = ref([])
const categories = ref([])
const selectedCategory = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchPosts = async () => {
  loading.value = true
  error.value = null
  try {
    const params = selectedCategory.value ? { category: selectedCategory.value } : {}
    const response = await api.get('/posts', { params })
    posts.value = response.data

    // Extract unique categories from all posts (for now, until a dedicated API endpoint exists)
    const uniqueCategories = [...new Set(response.data.map(post => post.category).filter(Boolean))]
    categories.value = ['All', ...uniqueCategories]

  } catch (err) {
    error.value = 'Failed to fetch posts.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchPosts()
})

const handleCategoryChange = (event) => {
  selectedCategory.value = event.target.value === 'All' ? null : event.target.value
  fetchPosts()
}
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Blog Posts</h1>
    <div class="flex justify-between items-center mb-4">
      <router-link to="/posts/create" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Create New Post
      </router-link>
      <div class="relative">
        <select @change="handleCategoryChange" class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
          <option value="All">All Categories</option>
          <option v-for="cat in categories.filter(c => c !== 'All')" :key="cat" :value="cat">{{ cat }}</option>
        </select>
        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
        </div>
      </div>
    </div>

    <div v-if="loading" class="text-center text-gray-500">Loading posts...</div>
    <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>
    <div v-else-if="posts.length === 0" class="text-center text-gray-500">No posts found. Create one!</div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="post in posts" :key="post.id" class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-2">
          <router-link :to="{ name: 'PostDetail', params: { id: post.id } }" class="text-blue-600 hover:underline">
            {{ post.title }}
          </router-link>
        </h2>
        <p class="text-gray-600">{{ post.content.substring(0, 100) }}...</p>
          <span v-if="post.category" class="inline-block bg-blue-100 text-blue-800 text-xs px-2 rounded-full uppercase font-semibold tracking-wide mt-2">{{ post.category }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Component-specific styles */
</style>
