<script setup>
import { ref } from 'vue'
import PostForm from '../components/PostForm.vue'
import api from '../services/api'
import { useRouter } from 'vue-router'

const router = useRouter()
const loading = ref(false)
const error = ref(null)

const handleFormSubmit = async (formData) => {
  loading.value = true
  error.value = null
  try {
    const response = await api.post('/posts', formData)
    router.push({ name: 'PostDetail', params: { id: response.data.id } })
  } catch (err) {
    error.value = 'Failed to create post.'
    console.error('Error creating post:', err)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Create New Post</h1>
    <div v-if="loading" class="text-center text-gray-500 mb-4">Creating post...</div>
    <div v-if="error" class="text-center text-red-500 mb-4">{{ error }}</div>
    <PostForm @submit="handleFormSubmit" :disabled="loading" />
  </div>
</template>

<style scoped>
/* Component-specific styles */
</style>
