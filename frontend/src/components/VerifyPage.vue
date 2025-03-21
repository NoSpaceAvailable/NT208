<template>
  <footer class="bg-gray-100 border-t border-gray-300 py-6">
    <div class="container mx-auto px-4">
      <!-- Grid Layout for Footer Sections -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Quick Links -->
        <div>
          <h5 class="text-lg font-semibold mb-3">Quick Links</h5>
          <ul class="flex flex-wrap gap-3">
            <li v-for="(link, index) in links" :key="index">
              <a href="#" class="text-gray-700 hover:text-blue-500 transition-colors duration-200">
                {{ link.text }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Social Media -->
        <div>
          <h5 class="text-lg font-semibold mb-3">Follow Us</h5>
          <ul class="flex gap-3">
            <li>
              <a href="#" class="text-gray-700 hover:text-blue-500 transition-colors duration-200 text-2xl">
                <i class="fab fa-facebook"></i>
              </a>
            </li>
            <li>
              <a href="#" class="text-gray-700 hover:text-blue-500 transition-colors duration-200 text-2xl">
                <i class="fab fa-twitter"></i>
              </a>
            </li>
            <li>
              <a href="#" class="text-gray-700 hover:text-blue-500 transition-colors duration-200 text-2xl">
                <i class="fab fa-instagram"></i>
              </a>
            </li>
            <li>
              <a href="#" class="text-gray-700 hover:text-blue-500 transition-colors duration-200 text-2xl">
                <i class="fab fa-linkedin"></i>
              </a>
            </li>
          </ul>
        </div>

        <!-- Newsletter -->
        <div>
          <h5 class="text-lg font-semibold mb-3">Subscribe to Our Newsletter</h5>
          <form class="flex">
            <input
              type="email"
              class="flex-grow p-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Enter your email"
            />
            <button
              type="submit"
              class="bg-blue-500 text-white px-4 py-2 rounded-r-md hover:bg-blue-600 transition-colors duration-200"
            >
              Subscribe
            </button>
          </form>
        </div>
      </div>

      <!-- Copyright Notice -->
      <p class="text-center text-gray-600 mt-6">
        &copy; 2025 Almacenar. All rights reserved.
      </p>
    </div>
  </footer>
</template>

<script>
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
      ]
    };
  }
};
</script>