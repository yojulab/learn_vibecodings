<template>
  <form @submit.prevent="handleSubmit" class="space-y-4">
    <div>
      <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
      <input type="text" id="title" v-model="editablePost.title" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
    </div>
    <div>
      <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
      <input type="text" id="category" v-model="editablePost.category" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
    </div>
    <div>
      <label for="content" class="block text-sm font-medium text-gray-700">Content</label>
      <textarea id="content" v-model="editablePost.content" required rows="10" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
    </div>
    <div>
      <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
        {{ post ? 'Update' : 'Create' }} Post
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import type { Post, PostCreate, PostUpdate } from '@/api/posts';

const props = defineProps<{
  post?: Post | null;
}>();

const emit = defineEmits<{
  (e: 'submit', data: PostCreate | PostUpdate): void;
}>();

const editablePost = ref<PostCreate | PostUpdate>({
  title: '',
  content: '',
  category: '',
});

watch(() => props.post, (newPost) => {
  if (newPost) {
    editablePost.value = { ...newPost };
  } else {
    editablePost.value = { title: '', content: '', category: '' };
  }
}, { immediate: true });

function handleSubmit() {
  emit('submit', editablePost.value);
}
</script>
