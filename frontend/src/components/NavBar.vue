<template>
  <div class="sticky mx-auto flex justify-between items-center p-4 bg-[#262423] shadow-md">
    <!-- Logo -->
    <a class="text-xl font-bold text-[#f6f6f6]" href="/">Almacenar</a>

    <!-- Center Links -->
    <div class="flex-grow flex justify-center">
      <ul class="flex space-x-4">
        <li v-for="(link, index) in links" :key="index" class="relative">
          <!-- Dropdown for Marketplace -->
          <div v-if="link.text === 'Marketplace'" class="relative">
            <a class="text-[#f6f6f6] hover:text-[#8FC773] cursor-pointer" @click="toggleDropdown('marketplace')">
              {{ link.text }}
            </a>
            <ul v-if="activeDropdown === 'marketplace'" class="absolute bg-[#171615] shadow-lg mt-2 w-40"
              @click="handleDropdownClick">
              <li v-for="(item, idx) in DropdownItems.Marketplace" :key="idx">
                <a class="block px-4 py-2 bg-[#171615] text-[#f6f6f6] hover:text-[#8FC773]" :href="item.url">{{
                  item.label }}</a>
              </li>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a v-else class="text-[#f6f6f6] hover:text-[#8FC773]" :href="link.url" :title="`${link.text} page`"
            @click="handleOnclickEvent(link)">
            {{ link.text }}
          </a>
        </li>
      </ul>
    </div>

    <!-- Right Links -->
    <div>
      <ul class="flex space-x-4 pl-4">
        <li v-for="(link, index) in linksRight" :key="index" class="relative">
          <!-- Dropdown for My account -->
          <div v-if="link.text === 'My account'" class="relative">
            <a class="text-[#f6f6f6] hover:text-[#8FC773] cursor-pointer" @click="toggleDropdown('account')">
              {{ link.text }}
            </a>
            <ul v-if="activeDropdown === 'account'" class="absolute bg-white shadow-lg mt-2 w-40 right-0"
              @click="handleDropdownClick">
              <!-- Display login/register for unauthenticated users -->
              <template v-if="!isAuthenticated">
                <li>
                  <a class="block px-4 py-2 bg-[#171615] text-[#f6f6f6] hover:text-[#8FC773]"
                    href="/auth#login">Login</a>
                </li>
                <li>
                  <a class="block px-4 py-2 bg-[#171615] text-[#f6f6f6] hover:text-[#8FC773]"
                    href="/auth#register">Register</a>
                </li>
              </template>
              <!-- Display account options for authenticated users -->
              <template v-else>
                <li v-for="(item, idx) in DropdownItems.Account" :key="idx">
                  <a class="block px-4 py-2 bg-[#171615] text-[#f6f6f6] hover:text-[#8FC773]" href="#">{{ item.label
                  }}</a>
                </li>
              </template>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a v-else class="text-[#f6f6f6] hover:text-[#8FC773]" :href="link.url" :title="`${link.text} page`"
            @click="handleOnclickEvent(link)">
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
          url: "/",
          title: "lqc's game shop",
          banner: "A place where gamers can buy and sell their best items!"
        },
        {
          text: "Community",
          url: "/community",
          title: "Community page",
          banner: "where users can view rate of each trader"
        },
        {
          text: "Marketplace",
          url: "#"
        },
        {
          text: "About us",
          url: "/about",
          title: "about page",
          banner: "this is where the developer of this fking app can say something about them"
        },
        {
          text: "Support",
          url: "/support",
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
          { label: "Merchandise", url: "/merchandise" },
          { label: "Sell my items", url: "/sell" }
        ],
        Account: [
          { label: "Profile", url: "#" },
          { label: "Notification", url: "#" },
          { label: "Transaction history", url: "#" },
          { label: "Logout", url: "/api/auth/logout" }
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
      window.location.href = link.url;
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
    handleDropdownClick(event) {
      // Stop event propagation to prevent the dropdown from closing
      event.stopPropagation();
    },
    async checkAuthStatus() {
      try {
        const response = await fetch("/api/auth/check", {
          method: "GET",
          credentials: "include"
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