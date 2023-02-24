import { createRouter, createWebHashHistory } from 'vue-router'
import WelcomeView from '../views/WelcomeView.vue'
import UploadView from '../views/UploadView.vue'


const routes = [
    {
      path: '/',
      name: 'home',
      component: WelcomeView
    },
    {
      path: '/upload',
      name: 'upload',
      component: UploadView
    }
  ]
  
  const router = createRouter({
    history: createWebHashHistory(),
    routes
  })
  
  export default router