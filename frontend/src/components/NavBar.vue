<template>
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Almacenar</a>
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li v-for="(link, index) in links" :key="index" class="nav-item">
          <!-- Dropdown for Marketplace -->
          <div v-if="link.text === 'Marketplace'" class="dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              {{ link.text }}
            </a>
            <ul class="dropdown-menu">
              <!-- Dynamically render dropdown items based on link text -->
              <li v-for="(item, idx) in DropdownItems.Marketplace" :key="idx">
                <a class="dropdown-item" href="#">{{ item.label }}</a>
              </li>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a
            v-else
            class="nav-link"
            aria-current="page"
            :href="link.url"
            :title="`${link.text} page`"
            @click.prevent="handleOnclickEvent(link)"
          >
            {{ link.text }}
          </a>
        </li>
      </ul>
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li v-for="(link, index) in linksRight" :key="index" class="nav-item">          
            <!-- Dropdown for My account -->
          <div v-if="link.text === 'My account'" class="dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              {{ link.text }}
            </a>
            <ul class="dropdown-menu dropdown-menu-end">
              <!-- Dynamically render dropdown items based on link text -->
              <li v-for="(item, idx) in DropdownItems.Account" :key="idx">
                <a class="dropdown-item" href="#">{{ item.label }}</a>
              </li>
            </ul>
          </div>
          <!-- Regular links for other items -->
          <a
            v-else
            class="nav-link"
            aria-current="page"
            :href="link.url"
            :title="`${link.text} page`"
            @click.prevent="handleOnclickEvent(link)"
          >
            {{ link.text }}
          </a>
        </li>
      </ul>
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
            banner: "get suport from AI agent"
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
        }
      };
    },
    methods: {
      handleOnclickEvent(link) {
        document.getElementById("title").innerText = link.title;
        document.getElementById("banner").innerText = link.banner;
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  </style>