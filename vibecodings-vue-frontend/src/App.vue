<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from './stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.clearToken()
  router.push({ name: 'home' })
}
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <header class="bg-gray-800 text-white p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-2xl font-bold text-white no-underline">My Blog</router-link>
        <nav>
          <button v-if="authStore.isAuthenticated" @click="handleLogout" class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded text-sm">
            Logout
          </button>
          <router-link v-else to="/login" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded text-sm no-underline">
            Login
          </router-link>
        </nav>
      </div>
    </header>

    <main class="flex-grow container mx-auto p-4">
      <router-view />
    </main>

    <footer class="bg-gray-700 text-white p-4 text-center">
      <div class="container mx-auto">
        <p>&copy; 2023 My Blog</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Tailwind handles most styling, but custom styles can go here */
</style>