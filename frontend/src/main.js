import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
import vue3GoogleLogin from 'vue3-google-login';

const gauthOption = {
    clientId: '957032210822-4v67c9lvii451v6i4djg4qr098h8vsqd.apps.googleusercontent.com',
};

createApp(NavBar).mount('#nav');
createApp(App)
    .use(router)
    .use(vue3GoogleLogin, gauthOption)
    .mount('#app');
createApp(Footer).mount('#footer');