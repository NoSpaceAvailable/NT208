import { createWebHistory, createRouter } from 'vue-router';
import AuthPage from '../components/AuthPage.vue';
import NotFound from '../components/404.vue';
import MainPage from '../components/MainPage.vue';
import VerifyPage from '@/components/VerifyPage.vue';

const routes = [
    { path: '/', component: MainPage },
    { path: '/auth', component: AuthPage },
    { path: '/verify', component: VerifyPage },
    { path: '/:pathMatch(.*)', component: NotFound },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;