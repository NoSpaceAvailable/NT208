<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <!-- Form -->
    <form @submit.prevent="submitForm" class="space-y-4">
      <!-- Username Field -->
      <div>
        <label for="username" class="block text-sm font-medium text-gray-700">Username:</label>
        <input
          id="username"
          type="text"
          v-model="formData.username"
          required
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          autocomplete="off"
        />
      </div>

      <!-- Email Field (Visible only on Register Page) -->
      <div v-if="isRegisterPage">
        <label for="email" class="block text-sm font-medium text-gray-700">Email:</label>
        <input
          id="email"
          type="email"
          v-model="formData.email"
          required
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      <!-- Password Field -->
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password:</label>
        <input
          id="password"
          type="password"
          v-model="formData.password"
          required
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          autocomplete="off"
        />
      </div>

      <!-- Confirm Password Field (Visible only on Register Page) -->
      <div v-if="isRegisterPage">
        <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirm Password:</label>
        <input
          id="confirm-password"
          type="password"
          v-model="formData.confirmPassword"
          required
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        <p v-if="passwordMismatch" class="mt-2 text-sm text-red-600">Passwords do not match.</p>
      </div>

      <!-- Submit Button -->
      <button
        type="submit"
        :disabled="isRegisterPage && passwordMismatch"
        class="w-full px-4 py-2 bg-blue-600 text-white rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {{ isRegisterPage ? 'Register' : 'Login' }}
      </button>

      <!-- Toggle Between Login and Register -->
      <p class="text-center text-sm text-gray-600">
        <span v-if="isRegisterPage">Already have an account? </span>
        <span v-else>Don't have an account? </span>
        <a
          :href="isRegisterPage ? '#login' : '#register'"
          class="text-blue-600 hover:text-blue-500"
        >
          {{ isRegisterPage ? 'Login here' : 'Register here' }}
        </a>
      </p>
    </form>

    <!-- Verification Modal -->
    <div
      v-if="showVerificationModal"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Email Verification</h3>
        <VerifyPage :email="formData.email" @close="showVerificationModal = false" />
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
      showVerificationModal: false // Controls modal visibility
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
            this.showVerificationModal = true;
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