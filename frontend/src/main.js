import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import vue3GoogleLogin from 'vue3-google-login';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';

const gauthOption = {
  clientId: '718649155809-pvn7nnt5m98em3h2svvgidkvteh6pkik.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
};

const app = createApp(App);

// Install the router and the Google OAuth plugin on the single app instance
app.use(router);
app.use(vue3GoogleLogin, gauthOption);

app.component('NavBar', NavBar);
app.component('Footer', Footer);
app.mount('#app');
