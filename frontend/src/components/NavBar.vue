<template>
  <div class="sticky mx-auto flex justify-between items-center p-4 bg-gray-100 shadow-md">
    <!-- Logo -->
    <a class="text-xl font-bold" href="/">Almacenar</a>

    <!-- Center Links -->
    <div class="flex-grow flex justify-center">
      <ul class="flex space-x-4">
        <li v-for="(link, index) in links" :key="index" class="relative">
          <!-- Dropdown for Marketplace -->
          <div v-if="link.text === 'Marketplace'" class="relative">
            <a class="text-gray-700 hover:text-gray-900 cursor-pointer" @click="toggleDropdown('marketplace')">
              {{ link.text }}
            </a>
            <ul v-if="activeDropdown === 'marketplace'" class="absolute bg-white shadow-lg mt-2 w-40">
              <li v-for="(item, idx) in DropdownItems.Marketplace" :key="idx">
                <a class="block px-4 py-2 text-gray-700 hover:bg-gray-200" href="#">{{ item.label }}</a>
              </li>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a v-else class="text-gray-700 hover:text-gray-900" :href="link.url" :title="`${link.text} page`"
            @click.prevent="handleOnclickEvent(link)">
            {{ link.text }}
          </a>
        </li>
      </ul>
    </div>

    <!-- Right Links -->
    <div>
      <ul class="flex space-x-4">
        <li v-for="(link, index) in linksRight" :key="index" class="relative">
          <!-- Dropdown for My account -->
          <div v-if="link.text === 'My account'" class="relative">
            <a class="text-gray-700 hover:text-gray-900 cursor-pointer" @click="toggleDropdown('account')">
              {{ link.text }}
            </a>
            <ul v-if="activeDropdown === 'account'" class="absolute bg-white shadow-lg mt-2 w-40 right-0">
              <!-- Display login/register for unauthenticated users -->
              <template v-if="!isAuthenticated">
                <li>
                  <a class="block px-4 py-2 text-gray-700 hover:bg-gray-200" href="/auth#login">Login</a>
                </li>
                <li>
                  <a class="block px-4 py-2 text-gray-700 hover:bg-gray-200" href="/auth#register">Register</a>
                </li>
              </template>
              <!-- Display account options for authenticated users -->
              <template v-else>
                <li v-for="(item, idx) in DropdownItems.Account" :key="idx">
                  <a class="block px-4 py-2 text-gray-700 hover:bg-gray-200" href="#">{{ item.label }}</a>
                </li>
              </template>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a v-else class="text-gray-700 hover:text-gray-900" :href="link.url" :title="`${link.text} page`"
            @click.prevent="handleOnclickEvent(link)">
            {{ link.text }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: [
        {
          text: "Home",
          url: "#",
          title: "lqc's game shop",
          banner: "A place where gamers can buy and sell their best items!"
        },
        {
          text: "Community",
          url: "#",
          title: "Community page",
          banner: "where users can view rate of each trader"
        },
        {
          text: "Marketplace",
          url: "#"
        },
        {
          text: "About us",
          url: "#",
          title: "about page",
          banner: "this is where the developer of this fking app can say something about them"
        },
        {
          text: "Support",
          url: "#",
          title: "Support page",
          banner: "get support from AI agent"
        }
      ],
      linksRight: [
        {
          text: "Search",
          url: "#",
          title: "search box",
          banner: "search something here"
        },
        {
          text: "My account",
          url: "#"
        }
      ],
      DropdownItems: {
        Marketplace: [
          { label: "Merchandise" },
          { label: "Sell my items" }
        ],
        Account: [
          { label: "Profile" },
          { label: "Notification" },
          { label: "Transaction history" }
        ]
      },
      activeDropdown: null, // Tracks which dropdown is active
      isAuthenticated: false
    };
  },
  computed: {
    isAuthPage() {
      return window.location.pathname === "/auth" || window.location.pathname === "/verify";
    }
  },
  methods: {
    handleOnclickEvent(link) {
      document.getElementById("title").innerText = link.title;
      document.getElementById("banner").innerText = link.banner;
    },
    toggleDropdown(dropdown) {
      // Toggle the dropdown
      this.activeDropdown = this.activeDropdown === dropdown ? null : dropdown;
      if (this.activeDropdown) {
        document.addEventListener("click", this.closeDropdown);
      } else {
        document.removeEventListener("click", this.closeDropdown);
      }
    },
    closeDropdown(event) {
      if (!this.$el.contains(event.target)) {
        this.activeDropdown = null;
        document.removeEventListener("click", this.closeDropdown);
      }
    },
    async checkAuthStatus() {
      try {
        const response = await fetch("/api/auth/check", {
          method: "GET",
          credentials: "include" // Include cookies in the request
        });
        const data = await response.json();
        this.isAuthenticated = data.status === "ok";
      } catch (error) {
        console.error("Error checking authentication status:", error);
      }
    }
  },
  async created() {
    await this.checkAuthStatus(); // Check authentication status when the component is created
  },
  beforeDestroy() {
    document.removeEventListener("click", this.closeDropdown);
  }
};
</script>