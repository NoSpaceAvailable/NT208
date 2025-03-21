import { createApp } from 'vue';
import App from './App.vue';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';

import router from './router/router';

createApp(NavBar).mount('#nav');
createApp(App).use(router).mount('#app');
createApp(Footer).mount('#footer');