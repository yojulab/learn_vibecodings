<script setup>
import { ref, watch } from 'vue'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'

const props = defineProps({
  initialTitle: { type: String, default: '' },
  initialContent: { type: String, default: '' },
})

const emits = defineEmits(['submit'])

const title = ref(props.initialTitle)
const content = ref(props.initialContent)

watch(() => props.initialTitle, (newVal) => {
  title.value = newVal
})

watch(() => props.initialContent, (newVal) => {
  content.value = newVal
})

const handleSubmit = () => {
  emits('submit', { title: title.value, content: content.value, author_id: 'temp_author' }) // TODO: Replace temp_author with actual author_id from auth system
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="bg-white p-6 rounded-lg shadow-md">
    <div class="mb-4">
      <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
      <input
        type="text"
        id="title"
        v-model="title"
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        required
      />
    </div>
    <div class="mb-6">
      <label for="content" class="block text-gray-700 text-sm font-bold mb-2">Content:</label>
      <VueSimplemde v-model="content" ref="markdownEditor" />
    </div>
    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      Submit
    </button>
  </form>
</template>

<style scoped>
/* Component-specific styles */
</style>

<style scoped>
/* Component-specific styles */
</style>
