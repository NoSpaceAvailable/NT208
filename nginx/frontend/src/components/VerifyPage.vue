<template>
  <div class="flex flex-col w-full max-w-sm mx-auto p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-lg transform rounded-2xl shadow-xl">
    <!-- Verification Form -->
    <form @submit.prevent="submitForm" class="space-y-4">
      <div class="flex flex-col justify-center mx-auto items-center gap-3 pb-4 pt-4">
        <h1 class="text-2xl font-bold text-[#8FC773] my-auto">Verify Your Email</h1>
      </div>
      <div class="text-xs font-light text-[#8FC773] pb-4 text-center">
        Enter the 6-digit code sent to your email.
      </div>

      <!-- Verification Code Input -->
      <div>
        <label for="verify-code" class="block mb-2 text-base font-medium text-[#8FC773]">
          Verification Code:
        </label>
        <div class="relative text-gray-400">
          <span class="absolute inset-y-0 left-0 flex items-center p-1 pl-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="lucide lucide-lock"
            >
              <rect width="18" height="11" x="3" y="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
          </span>
          <input
            id="verify-code"
            type="text"
            v-model="code"
            pattern="^[0-9]{6}$"
            required
            class="pl-12 mb-2 bg-gray-50 text-gray-600 border focus:border-transparent border-gray-300 sm:text-sm rounded-lg ring-3 ring-transparent focus:ring-1 focus:outline-hidden focus:ring-gray-400 block w-full p-2.5 rounded-l-lg py-3 px-4"
            placeholder="123456"
          />
        </div>
      </div>

      <!-- Buttons -->
      <div class="flex justify-end space-x-3">
        <button
          type="button"
          @click="$emit('close')"
          class="w-full text-[#f6f6f6] hover:text-[#8FC773] bg-[#313131] focus:outline-hidden focus:ring-primary-300 font-medium rounded-lg px-4 py-2 text-sm text-center mb-6"
        >
          Close
        </button>
        <button
          type="submit"
          class="w-full text-[#f6f6f6] hover:text-[#8FC773] bg-[#313131] focus:outline-hidden focus:ring-primary-300 font-medium rounded-lg px-4 py-2 text-sm text-center mb-6"
        >
          Verify
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'VerifyPage',
  props: ['email'],
  data() {
    return { code: '' };
  },
  methods: {
    async submitForm() {
      try {
        const response = await fetch('/api/auth/verify', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: this.email, code: this.code })
        });

        if (response.ok) {
          alert('Verification successful! You can now log in.');
          this.$emit('close'); // Close modal on success
          location.href = '/auth#login'; // Redirect to login page
        } else {
          alert('Verification failed: Wrong code. Try again.');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Failed to verify. Please try again later.');
      }
    }
  }
};
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>