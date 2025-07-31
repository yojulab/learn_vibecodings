import { createRouter, createWebHistory } from 'vue-router'
import PostListView from '../views/PostListView.vue'
import PostDetailView from '../views/PostDetailView.vue'
import PostCreateView from '../views/PostCreateView.vue'
import PostEditView from '../views/PostEditView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'PostList',
      component: PostListView,
    },
    {
      path: '/post/new',
      name: 'PostCreate',
      component: PostCreateView,
    },
    {
      path: '/post/:id',
      name: 'PostDetail',
      component: PostDetailView,
    },
    {
      path: '/post/:id/edit',
      name: 'PostEdit',
      component: PostEditView,
    },
  ],
})

export default router
