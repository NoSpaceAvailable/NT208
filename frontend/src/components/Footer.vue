<template>
    <footer class="bg-gray-100 py-0 px-0 m-0 w-full">
        <!-- Social Media Section at the Top -->
        <section class="bg-black text-white w-full">
            <h5 class="text-center font-semibold mb-2 py-4">FOLLOW US ON SOCIAL MEDIA</h5>
            <div class="text-center py-4">
                <ul class="flex gap-3 justify-center">
                    <li v-for="(icon, name) in icons" :key="name">
                        <component :is="icon" />
                    </li>
                </ul>
            </div>
        </section>

        <!-- Middle Section with Quick Links and Newsletter -->
        <section class="grid grid-cols-1 md:grid-cols-2 gap-6 px-6 py-8 bg-[#111111] w-full">
            <!-- Quick Links -->
            <div class="text-center md:text-left">
                <h5 class="text-lg font-semibold mb-3 text-[#ededed]">Quick Links</h5>
                <ul class="space-y-2">
                    <li v-for="(link, index) in links" :key="index">
                        <a href="#" class="text-[#8FC773] hover:text-white">{{ link.text }}</a>
                    </li>
                </ul>
            </div>

            <!-- Newsletter -->
            <div class="text-center md:text-left">
                <h5 class="text-lg font-semibold mb-3 text-[#ededed]">Subscribe to Our Newsletter</h5>
                <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
                    <form class="flex justify-center md:justify-start" id="notification-email">
                        <input type="email"
                            class="p-2 pl-10 bg-[#131313] rounded-lg border border-gray-600 text-white focus:outline-none focus:ring-1 focus:ring-[#8FC773]"
                            placeholder="Enter your email"/>
                    </form>
                    <button
                            class="px-4 py-2 bg-[#8FC773] text-black font-medium rounded-lg hover:bg-[#7BBF5A] transition-colors" 
                            onclick="submitSubscribeForm();"
                            >
                            Subscribe!
                    </button>
                </div>
            </div>
        </section>

        <!-- Copyright Notice at the Bottom -->
        <section class="text-center py-4 bg-[#313131] w-full">
            <p class="text-[#8FC773]">&copy; 2025 Almacenar. All rights reserved.</p>
        </section>
    </footer>
</template>

<script>
import IconInstagram from './icons/IconInstagram.vue';
import IconFacebook from './icons/IconFacebook.vue';
import IconDiscord from './icons/IconDiscord.vue';
import IconTiktok from './icons/IconTiktok.vue';
import IconX from './icons/IconX.vue';

export default {
    name: "Footer",
    data() {
        return {
            links: [
                { text: "Home" },
                { text: "Community" },
                { text: "Marketplace" },
                { text: "About us" },
                { text: "Support" }
            ],
            icons: {
                facebook: IconFacebook,
                discord: IconDiscord,
                tiktok: IconTiktok,
                instagram: IconInstagram,
                x: IconX
            }
        };
    },
    methods: {
        submitSubscribeForm() {
            document.getElementById('notification-email').submit();
        },
    },
};
</script>

<style>
footer {
    margin: 0;
    padding: 0;
}
</style>