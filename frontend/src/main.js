import { createApp } from 'vue';
import App from './App.vue';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
import GoogleAuth from '@/config/google_oAuth.js';

const gauthOption = {
    clientId: '718649155809-pvn7nnt5m98em3h2svvgidkvteh6pkik.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'select_account'
}

const app = createApp(App);
app.use(GoogleAuth, gauthOption);
const nav = createApp(NavBar);  
const footer = createApp(Footer);
app.mount('#app')
nav.mount('nav')
footer.mount('footer')
import router from './router/router';

createApp(NavBar).mount('#nav');
createApp(App).use(router).mount('#app');
createApp(Footer).mount('#footer');