<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
      <form @submit.prevent="submitForm" class="space-y-4">
        <input type="hidden" :value="email" />

        <div>
          <label for="verify-code" class="block text-sm font-medium text-gray-700">
            Enter your 6-digit verification code:
          </label>
          <input id="verify-code" type="text" v-model="code" pattern="^[0-9]{6}$" required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" />
        </div>

        <div class="flex justify-end space-x-3">
          <button type="button" @click="$emit('close')"
            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-gray-700 bg-gray-100 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Close
          </button>
          <button type="submit"
            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Verify
          </button>
        </div>
      </form>
    </div>
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