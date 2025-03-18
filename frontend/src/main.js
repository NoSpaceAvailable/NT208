import { createApp } from 'vue'
import App from './App.vue'
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';

const app = createApp(App);
const nav = createApp(NavBar);  
const footer = createApp(Footer);

app.mount('#app')
nav.mount('nav')
footer.mount('footer')