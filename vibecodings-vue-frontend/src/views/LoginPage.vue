<script setup>
import { ref } from 'vue'
import api from '../services/api'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref(null)
const router = useRouter()
const authStore = useAuthStore()

const handleLogin = async () => {
  if (!username.value || !password.value) {
    error.value = 'Please enter both username and password.'
    return
  }

  loading.value = true
  error.value = null

  try {
    const formData = new URLSearchParams()
    formData.append('username', username.value)
    formData.append('password', password.value)

    const response = await api.post('/token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
    
    authStore.setToken(response.data.access_token)
    router.push({ name: 'PostList' }) // Redirect to post list on success

  } catch (err) {
    error.value = err.response?.data?.detail || 'Login failed. Please check your credentials.'
    console.error('Login error:', err)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container mx-auto p-4 flex justify-center items-center min-h-[calc(100vh-128px)]">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
      <h1 class="text-3xl font-bold mb-6 text-center">Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div v-if="error" class="text-red-500 text-sm mb-4">{{ error }}</div>
        <div class="flex items-center justify-between">
          <button
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            :disabled="loading"
          >
            {{ loading ? 'Logging in...' : 'Login' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
/* Component-specific styles */
</style>
