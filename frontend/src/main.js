import { createApp } from 'vue';
import App from './App.vue';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
import vue3GoogleLogin from 'vue3-google-login';

import router from './router/router';

const gauthOption = {
    clientId: '718649155809-pvn7nnt5m98em3h2svvgidkvteh6pkik.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'select_account'
};

createApp(NavBar).mount('#nav');
createApp(App)
    .use(router)
    .use(vue3GoogleLogin, gauthOption)
    .mount('#app');
createApp(Footer).mount('#footer');