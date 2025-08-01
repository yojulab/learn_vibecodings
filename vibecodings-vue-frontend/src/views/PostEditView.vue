<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PostForm from '../components/PostForm.vue'
import api from '../services/api'

const route = useRoute()
const router = useRouter()
const post = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchPost = async (id) => {
  loading.value = true
  error.value = null
  try {
    const response = await api.get(`/posts/${id}`)
    post.value = response.data
  } catch (err) {
    error.value = 'Failed to fetch post for editing.'
    console.error(err)
    // Redirect to 404 or list if post not found
    router.push({ name: 'PostList' })
  } finally {
    loading.value = false
  }
}

const handleFormSubmit = async (formData) => {
  loading.value = true
  error.value = null
  try {
    await api.put(`/posts/${post.value.id}`, formData)
    router.push({ name: 'PostDetail', params: { id: post.value.id } })
  } catch (err) {
    error.value = 'Failed to update post.'
    console.error('Error updating post:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchPost(route.params.id)
})

watch(() => route.params.id, (newId) => {
  if (newId) {
    fetchPost(newId)
  }
})
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Edit Post</h1>

    <div v-if="loading" class="text-center text-gray-500 mb-4">Loading post for editing...</div>
    <div v-else-if="error" class="text-center text-red-500 mb-4">{{ error }}</div>
    <div v-else-if="post">
      <PostForm
        @submit="handleFormSubmit"
        :initialTitle="post.title"
        :initialContent="post.content"
        :disabled="loading"
      />
    </div>
    <div v-else class="text-center text-gray-500">Post not found for editing.</div>
  </div>
</template>

<style scoped>
/* Component-specific styles */
</style>
