import { createWebHistory, createRouter } from 'vue-router';
import AuthPage from '../components/AuthPage.vue';
import NotFound from '../components/404.vue';
import MainPage from '../components/MainPage.vue';
import Community from '@/components/Community.vue';
import About from '@/components/About.vue';
import Support from '@/components/Support.vue';
import Merchandise from '@/components/Merchandise.vue';
import SellItem from '@/components/SellItem.vue';
import VerifyPage from '@/components/VerifyPage.vue';

const routes = [
    { path: '/', component: MainPage },
    { path: '/about', component: About },
    { path: '/auth', component: AuthPage },
    { path: '/sell', component: SellItem },
    { path: '/support', component: Support },
    { path: '/verify', component: VerifyPage },
    { path: '/community', component: Community },
    { path: '/merchandise', component: Merchandise },
    { path: '/:pathMatch(.*)', component: NotFound },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;