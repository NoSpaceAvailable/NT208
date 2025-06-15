<template>
    <div style="display: contents;">
        <!-- Content Overlay -->
        <div class="flex flex-grow items-center justify-center relative z-10 bg-[url('/src/images/profile_wallpaper.png')] bg-cover bg-center">
            <!-- Main Container -->
            <div class="flex flex-col w-full max-w-5xl mx-auto p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-lg">
                <!-- Heading -->
                <h1 class="text-3xl font-bold text-[#8FC773] mb-6">
                    We’re here to help
                </h1>

                <!-- Search Bar -->
                <div class="relative max-w-xl mb-8">
                    <input type="text"
                        class="w-full bg-gray-50 text-gray-600 border border-gray-300 rounded-md py-2 pl-4 pr-10 focus:outline-none focus:border-[#8FC773] focus:ring-1 focus:ring-[#8FC773]"
                        placeholder="Search..." />
                    <svg class="absolute right-3 top-2.5 h-5 w-5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M13.293 14.707a1 1 0 01-1.414 0l-2.829-2.828A5.5 5.5 0 1114.5 5.5a5.5 5.5 0 01-4.048 5.337l2.829 2.828a1 1 0 010 1.414zM7 10a3 3 0 106 0 3 3 0 00-6 0z"
                            clip-rule="evenodd" />
                    </svg>
                </div>

                <!-- Card Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    <!-- Card 1: My Account -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            My account
                        </h2>
                        <p class="text-gray-200 text-center">
                            Create and manage your account
                        </p>
                    </div>

                    <!-- Card 2: Email Campaigns -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M16 7H8m8 4H8m8 4H8m8 4H8" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            Email campaigns
                        </h2>
                        <p class="text-gray-200 text-center">
                            Engage your contacts with modern email design
                        </p>
                    </div>

                    <!-- Card 3: WhatsApp & SMS -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M2.25 15a4.5 4.5 0 004.5 4.5h9.75a4.5 4.5 0 004.5-4.5v-6a4.5 4.5 0 00-4.5-4.5H6.75a4.5 4.5 0 00-4.5 4.5v6z" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            WhatsApp &amp; SMS
                        </h2>
                        <p class="text-gray-200 text-center">
                            Connect with contacts via targeted messaging
                        </p>
                    </div>

                    <!-- Card 4: Transactional Emails -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M20 13V7a1 1 0 00-1-1H5a1 1 0 00-1 1v6m16 0l-3 3m3-3l-3-3" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            Transactional Emails
                        </h2>
                        <p class="text-gray-200 text-center">
                            Send one-to-one emails with high deliverability
                        </p>
                    </div>

                    <!-- Card 5: Contacts -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M17.5 6.5a2.121 2.121 0 00-3 0l-7 7a2.121 2.121 0 000 3l2 2a2.121 2.121 0 003 0l7-7a2.121 2.121 0 000-3l-2-2z" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            Contacts
                        </h2>
                        <p class="text-gray-200 text-center">
                            Manage and segment your contacts effectively
                        </p>
                    </div>

                    <!-- Card 6: Automation -->
                    <div
                        class="bg-[#313131]/80 rounded-lg shadow p-6 transition-colors duration-300 cursor-pointer hover:bg-[#313131]/90">
                        <div class="mb-4 text-[#8FC773] flex justify-center">
                            <!-- Placeholder icon -->
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6l4 2" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-medium text-[#8FC773] mb-2 text-center">
                            Automation
                        </h2>
                        <p class="text-gray-200 text-center">
                            Automate your processes to save time
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <!-- Chatbot Section -->
        <div>
            <!-- Chat Window: Rendered when showChat is true -->
            <div v-if="showChat"
                class="fixed bottom-20 right-8 z-50 bg-[#111111] rounded-xl shadow-lg w-[30rem] h-[36rem] flex flex-col">
                <div class="bg-[#111111]/90 text-[#8FC773] px-6 py-3 rounded-t-xl flex justify-between items-center">
                    <span class="font-bold text-xl">Online support</span>
                    <button @click="closeChat" class="text-[#8FC773] font-bold text-2xl">X</button>
                </div>
                <div id="chatbox" class="flex-1 p-6 overflow-y-auto">
                    <!-- Chat Messages -->
                    <div v-for="(msg, index) in messages" :key="index" class="mb-5">
                        <!-- User Message -->
                        <div v-if="msg.sender === 'user'" class="flex justify-end">
                            <div class="bg-[#8FC773] text-white rounded-lg p-3 max-w-[75%] text-base">
                                {{ msg.text }}
                            </div>
                        </div>
                        <!-- Bot Message -->
                        <div v-else class="flex justify-start">
                            <div class="bg-[#313131] text-gray-200 rounded-lg p-3 max-w-[75%] text-base" 
                                v-html="renderMarkdown(msg.text)">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="px-6 py-3">
                    <input type="text" v-model="message" @keyup.enter="sendMessage"
                        class="w-full bg-gray-50 text-gray-600 border border-gray-300 rounded-md py-3 pl-5 pr-12 focus:outline-none focus:border-[#8FC773] focus:ring-1 focus:ring-[#8FC773] text-base"
                        placeholder="Type your message..." />
                </div>
            </div>

            <!-- Floating Chat Button: Visible when chat is closed -->
            <button v-if="!showChat" @click="toggleChat"
                class="fixed bottom-4 right-4 z-50 bg-[#8FC773] text-white p-4 rounded-full shadow-lg hover:bg-[#7EB864] transition-colors">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h12a2 2 0 012 2z" />
                </svg>
            </button>
        </div>
    </div>
</template>

<script>
import { marked } from 'marked';
import DOMPurify from 'dompurify';

marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: false,
    mangle: false,
    sanitize: true,
    sanitizer: (html) => DOMPurify.sanitize(html)
});

export default {
    name: "SupportPage",
    data() {
        return {
            showChat: false,
            message: "",
            messages: []
        };
    },
    methods: {
        toggleChat() {
            this.showChat = !this.showChat;
        },
        closeChat() {
            this.showChat = false;
        },
        async ask_bot(message) {
            const response = await fetch("/api/bot/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ question: message })
            });
            if (!response.ok) {
                return {
                    "status": "error",
                    "bot_answer": "Sorry, I am unable to process your request at the moment."
                };
            }
            return response.json();
        },
        sendMessage() {
            if (this.message.trim() !== "") {
                this.messages.push({ sender: "user", text: this.message.trim() });
                this.$nextTick(() => {
                    const chatbox = document.getElementById("chatbox");
                    chatbox.scrollTop = chatbox.scrollHeight;
                });

                this.ask_bot(this.message.trim()).then(response => {
                    this.messages.push({ sender: "bot", text: response.bot_answer });
                    this.$nextTick(() => {
                        const chatbox = document.getElementById("chatbox");
                        chatbox.scrollTop = chatbox.scrollHeight;
                    });
                });
                this.message = "";
            }
        },
        renderMarkdown(text) {
            if (typeof text !== "string") {
                return '';
            }
            return marked(text);
        }
    },
    mounted() {
        this.messages.push({ sender: "bot", text: "Hello! How can I help you today?" });
    }
};
</script>