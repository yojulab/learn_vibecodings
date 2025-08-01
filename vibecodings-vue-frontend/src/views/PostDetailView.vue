<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api, { deletePost } from '../services/api'
import { marked } from 'marked'

const route = useRoute()
const router = useRouter()
const post = ref(null)
const loading = ref(true)
const error = ref(null)

const renderedContent = ref('')

const handleDelete = async () => {
  if (confirm('Are you sure you want to delete this post?')) {
    try {
      await deletePost(post.value.id)
      router.push({ name: 'PostList' })
    } catch (err) {
      error.value = 'Failed to delete post.'
      console.error(err)
    }
  }
}

const fetchPost = async (id) => {
  loading.value = true
  error.value = null
  try {
    const response = await api.get(`/posts/${id}`)
    post.value = response.data
    renderedContent.value = marked(post.value.content) // Render markdown
  } catch (err) {
    error.value = 'Failed to fetch post.'
    console.error(err)
    // Redirect to 404 or list if post not found
    router.push({ name: 'PostList' })
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
    <div v-if="loading" class="text-center text-gray-500">Loading post...</div>
    <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>
    <div v-else-if="post" class="bg-white p-8 rounded-lg shadow-md">
      <h1 class="text-4xl font-extrabold mb-4 text-gray-900">{{ post.title }}</h1>
      <p class="text-sm text-gray-500 mb-6">
        By {{ post.author_id }} on {{ new Date(post.created_at).toLocaleDateString() }}
      </p>
      <div class="prose lg:prose-lg max-w-none mb-8 text-gray-800" v-html="renderedContent"></div>
      <div class="flex space-x-4">
        <router-link :to="{ name: 'PostEdit', params: { id: post.id } }" class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded">
          Edit
        </router-link>
        <button @click="handleDelete" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
          Delete
        </button>
      </div>
    </div>
    <div v-else class="text-center text-gray-500">Post not found.</div>
  </div>
</template>


<style scoped>
/* Component-specific styles */
</style>
