<template>
    <div style="display: contents">
        <!-- Content Overlay -->
        <div class="flex flex-grow items-center justify-center relative z-10 bg-[url('/src/images/profile_wallpaper.png')] bg-cover bg-center">
            <div
                class="flex flex-col w-full max-w-sm mx-auto p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-lg transform rounded-2xl shadow-xl">
                <!-- Verification Form (Replaces Login/Register Form) -->
                <VerifyPage v-if="showVerificationModal" :email="formData.email"
                    @close="showVerificationModal = false" />

                <!-- Login/Register Form (Default) -->
                <template v-else>
                    <div class="flex flex-col justify-center mx-auto items-center gap-3 pb-4 pt-4">
                        <h1 class="text-2xl font-bold text-[#8FC773] my-auto">Almacenar</h1>
                    </div>
                    <div class="text-xs font-light text-[#8FC773] pb-4 text-center">Login into your account</div>

                    <!-- Username Field -->
                    <form @submit.prevent="submitForm" class="flex flex-col">
                        <div class="pb-2">
                            <label for="username"
                                class="block mb-2 text-base font-medium text-[#8FC773]">Username</label>
                            <div class="relative text-gray-400">
                                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                                    <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <circle cx="12" cy="6" r="4" stroke="#1C274C" stroke-width="1.5" />
                                        <path
                                            d="M20 17.5C20 19.9853 20 22 12 22C4 22 4 19.9853 4 17.5C4 15.0147 7.58172 13 12 13C16.4183 13 20 15.0147 20 17.5Z"
                                            stroke="#1C274C" stroke-width="1.5" />
                                    </svg>
                                </span>
                                <input type="text" name="username" id="username"
                                    class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 block rounded-lg p-2.5 w-full"
                                    v-model="formData.username" placeholder="Username" autocomplete="off" />
                            </div>
                        </div>

                        <!-- Email Field (Visible only on Register Page) -->
                        <div class="pb-2" v-if="isRegisterPage">
                            <label for="email" class="block mb-2 text-base font-medium text-[#8FC773]">Email</label>
                            <div class="relative text-gray-400">
                                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" class="lucide lucide-mail">
                                        <rect width="20" height="16" x="2" y="4" rx="2"></rect>
                                        <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                                    </svg>
                                </span>
                                <input type="email" name="email" id="email"
                                    class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 rounded-lg p-2.5 w-full"
                                    placeholder="mail@example.com" v-model="formData.email" autocomplete="off" />
                            </div>
                        </div>

                        <!-- Password Field -->
                        <div class="pb-6">
                            <label for="password"
                                class="block mb-2 text-base font-medium text-[#8FC773]">Password</label>
                            <div class="relative text-gray-400">
                                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" class="lucide lucide-square-asterisk">
                                        <rect width="18" height="18" x="3" y="3" rx="2"></rect>
                                        <path d="M12 8v8"></path>
                                        <path d="m8.5 14 7-4"></path>
                                        <path d="m8.5 10 7 4"></path>
                                    </svg>
                                </span>
                                <input type="password" id="password" placeholder="••••••••••"
                                    v-model="formData.password" required
                                    class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 block w-full p-2.5 rounded-l-lg py-3 px-4"
                                    autocomplete="new-password" aria-autocomplete="list" />
                            </div>
                        </div>

                        <!-- Confirm Password Field (Visible only on Register Page) -->
                        <div class="pb-6" v-if="isRegisterPage">
                            <label for="confirm-password"
                                class="block mb-2 text-base font-medium text-[#8FC773]">Confirm
                                Password:</label>
                            <div class="relative text-gray-400">
                                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" class="lucide lucide-square-asterisk">
                                        <rect width="18" height="18" x="3" y="3" rx="2"></rect>
                                        <path d="M12 8v8"></path>
                                        <path d="m8.5 14 7-4"></path>
                                        <path d="m8.5 10 7 4"></path>
                                    </svg>
                                </span>
                                <input type="password" id="confirm-password" placeholder="••••••••••"
                                    v-model="formData.confirmPassword" required
                                    class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 block w-full p-2.5 rounded-l-lg py-3 px-4" />
                            </div>
                            <p v-if="passwordMismatch" class="mt-2 text-sm text-red-600">Passwords do not match.</p>
                        </div>

                        <!-- Submit Button -->
                        <button type="submit"
                            class="w-full text-[#f6f6f6] hover:text-[#8FC773] bg-[#313131] focus:outline-hidden focus:ring-primary-300 font-medium rounded-lg px-4 py-2 text-sm text-center mb-6"
                            :disabled="isRegisterPage && passwordMismatch">
                            {{ isRegisterPage ? 'Register' : 'Login' }}
                        </button>

                        <!-- Toggle Between Login and Register -->
                        <div class="text-sm font-light text-[#ffffff] text-center">
                            <span v-if="isRegisterPage">Already have an account? </span>
                            <span v-else>Don't have an account? </span>
                            <a :href="isRegisterPage ? '#login' : '#register'"
                                class="font-medium text-[#8FC773] hover:underline">
                                {{ isRegisterPage ? 'Sign In' : 'Sign Up' }}
                            </a>
                        </div>
                    </form>

                    <div class="relative flex py-8 items-center">
                        <div class="grow border-t border-[1px] border-gray-200"></div>
                        <span class="shrink mx-4 font-medium text-[#ffffff]">OR</span>
                        <div class="grow border-t border-[1px] border-gray-200"></div>
                    </div>

                    <form>
                        <div class="flex flex-col gap-2 justify-center">
                            <GoogleButton />
                        </div>
                    </form>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import { GoogleLogin, decodeCredential } from 'vue3-google-login';
import VerifyPage from './VerifyPage.vue';
import GoogleButton from './buttons/GoogleButton.vue';

export default {
    name: 'AuthPage',
    components: { VerifyPage, GoogleButton },
    data() {
        return {
            formData: {
                username: '',
                email: '',
                password: '',
                confirmPassword: ''
            },
            showVerificationModal: false // Controls whether to show the verification form
        };
    },
    computed: {
        isRegisterPage() {
            return this.$route.hash === '#register';
        },
        passwordMismatch() {
            return this.isRegisterPage && this.formData.password !== this.formData.confirmPassword;
        }
    },
    methods: {
        async submitForm() {
            if (this.isRegisterPage && this.passwordMismatch) {
                alert('Passwords do not match!');
                return;
            }

            const url = this.isRegisterPage ? '/api/auth/register' : '/api/auth/login';
            const payload = {
                username: this.formData.username,
                password: this.formData.password
            };

            if (this.isRegisterPage) {
                payload.email = this.formData.email;
            }

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();

                if (response.ok) {
                    if (this.isRegisterPage) {
                        alert('Registration successful! Please verify your email.');
                        this.showVerificationModal = true; // Show verification form
                    } else {
                        alert('Login successful!');
                        window.location.href = '/';
                    }
                } else {
                    alert(result.message || 'An error occurred.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to connect to the server.');
            }
        }
    }
};
</script>
