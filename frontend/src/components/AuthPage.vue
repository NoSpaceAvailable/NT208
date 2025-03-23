<template>
  <div style="display: contents">
    <!-- Video Background -->
    <div class="absolute left-0 w-full h-full overflow-hidden z-0">
      <video autoplay muted loop class="w-full h-full object-cover">
        <source src="/src/videos/auth_wallpaper.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>

    <!-- Content Overlay -->
    <div class="flex flex-grow items-center justify-center relative z-10">
      <div
        class="flex flex-col w-full max-w-sm mx-auto p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-lg transform rounded-2xl shadow-xl">
        <!-- Verification Form (Replaces Login/Register Form) -->
        <VerifyPage v-if="showVerificationModal" :email="formData.email" @close="showVerificationModal = false" />

        <!-- Login/Register Form (Default) -->
        <template v-else>
          <div class="flex flex-col justify-center mx-auto items-center gap-3 pb-4 pt-4">
            <h1 class="text-2xl font-bold text-[#8FC773] my-auto">Almacenar</h1>
          </div>
          <div class="text-xs font-light text-[#8FC773] pb-4 text-center">Login into your account</div>

          <!-- Username Field -->
          <form @submit.prevent="submitForm" class="flex flex-col">
            <div class="pb-2">
              <label for="username" class="block mb-2 text-base font-medium text-[#8FC773]">Username</label>
              <div class="relative text-gray-400">
                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                  <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="lucide lucide-mail">
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
              <label for="password" class="block mb-2 text-base font-medium text-[#8FC773]">Password</label>
              <div class="relative text-gray-400">
                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="lucide lucide-square-asterisk">
                    <rect width="18" height="18" x="3" y="3" rx="2"></rect>
                    <path d="M12 8v8"></path>
                    <path d="m8.5 14 7-4"></path>
                    <path d="m8.5 10 7 4"></path>
                  </svg>
                </span>
                <input type="password" id="password" placeholder="••••••••••" v-model="formData.password" required
                  class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 block w-full p-2.5 rounded-l-lg py-3 px-4"
                  autocomplete="new-password" aria-autocomplete="list" />
              </div>
            </div>

            <!-- Confirm Password Field (Visible only on Register Page) -->
            <div class="pb-6" v-if="isRegisterPage">
              <label for="confirm-password" class="block mb-2 text-base font-medium text-[#8FC773]">Confirm
                Password:</label>
              <div class="relative text-gray-400">
                <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="lucide lucide-square-asterisk">
                    <rect width="18" height="18" x="3" y="3" rx="2"></rect>
                    <path d="M12 8v8"></path>
                    <path d="m8.5 14 7-4"></path>
                    <path d="m8.5 10 7 4"></path>
                  </svg>
                </span>
                <input type="password" id="confirm-password" placeholder="••••••••••" v-model="formData.confirmPassword"
                  required
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
              <a :href="isRegisterPage ? '#login' : '#register'" class="font-medium text-[#8FC773] hover:underline">
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
              <button
                class="flex flex-row gap-2 p-2 rounded-md border-2 border-gray-400 text-[#8FC773] justify-center items-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="24px" height="24px">
                  <path fill="#FFC107"
                    d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z" />
                  <path fill="#FF3D00"
                    d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z" />
                  <path fill="#4CAF50"
                    d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z" />
                  <path fill="#1976D2"
                    d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z" />
                </svg>
                <span class="font-medium">Login with Google</span>
              </button>
              <button
                class="flex flex-row gap-2 p-2 rounded-md border-2 border-gray-400 text-[#8FC773] justify-center items-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="24px" height="24px">
                  <path fill="#3F51B5"
                    d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5V37z" />
                  <path fill="#FFF"
                    d="M34.368,25H31v13h-5V25h-3v-4h3v-2.41c0.002-3.508,1.459-5.59,5.592-5.59H35v4h-2.287C31.104,17,31,17.6,31,18.723V21h4L34.368,25z" />
                </svg>
                <span class="font-medium">Login with Facebook</span>
              </button>
            </div>
          </form>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import VerifyPage from './VerifyPage.vue';

export default {
  name: 'AuthPage',
  components: { VerifyPage },
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