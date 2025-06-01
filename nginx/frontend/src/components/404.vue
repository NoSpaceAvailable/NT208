<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100 text-gray-900">
    <!-- 404 Error Message -->
    <h1 class="text-6xl font-bold text-red-600">404</h1>
    <p class="text-lg text-gray-700 mt-2">Page not found</p>

    <!-- Home Link -->
    <router-link 
      to="/" 
      class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-200"
    >
      Go back home
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
};
</script>