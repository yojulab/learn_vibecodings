import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/posts' // Redirect root to post list
    },
    {
      path: '/posts',
      name: 'PostList',
      component: () => import('../views/PostListView.vue')
    },
    {
      path: '/posts/create',
      name: 'PostCreate',
      component: () => import('../views/PostCreateView.vue')
    },
    {
      path: '/posts/:id',
      name: 'PostDetail',
      component: () => import('../views/PostDetailView.vue')
    },
    {
      path: '/posts/:id/edit',
      name: 'PostEdit',
      component: () => import('../views/PostEditView.vue')
    }
  ]
})

export default router
