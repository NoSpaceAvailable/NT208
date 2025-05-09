<template>
    <div style="display: contents">
        <div class="absolute left-0 w-full h-full overflow-hidden z-0">
                <video autoplay muted loop class="w-full h-full object-cover">
                    <source src="/src/videos/auth_wallpaper.mp4" type="video/mp4" />
                    Your browser does not support the video tag.
                </video>
            </div>
        <div class="container mx-auto p-6 bg-gray-900 text-white rounded-lg flex-grow min-h-screen z-10">
            <!-- Header & Search Bar -->
            <div class="flex items-center justify-between bg-gray-800 p-4 rounded-lg">
                <h1 class="text-xl font-bold">Skin Storage</h1>
                <div class="flex space-x-2">
                <input 
                    v-model="searchQuery" 
                    @keyup="applyFilters" 
                    placeholder="Searching skin..." 
                    class="p-2 rounded bg-gray-700 text-white"
                />
                <button @click="applyFilters" class="p-2 bg-green-500 text-white rounded">Search</button>
                <button @click="showFilter = !showFilter" class="p-2 bg-blue-500 text-white rounded">Filter</button>
                </div>
            </div>
        
            <!-- Filters -->
            <div v-if="showFilter" class="mt-4 bg-gray-800 p-4 rounded-lg">
                <!-- Gun Filter -->
                <label class="block text-gray-400">Gun:</label>
                <select 
                    @change="addFilter('weaponType', $event.target.value)" 
                    class="p-2 rounded bg-gray-700 text-white inline-block whitespace-nowrap"
                >
                    <option value="All">All</option>
                    <option v-for="weapon in weaponTypes" :key="weapon" :value="weapon">{{ weapon }}</option>
                </select>

                <!-- Rarity Filter -->
                <label class="block text-gray-400 mt-2">Rarity:</label>
                <select 
                    @change="addFilter('rarity', $event.target.value)" 
                    class="p-2 rounded bg-gray-700 text-white inline-block whitespace-nowrap"
                >
                    <option value="All">All</option>
                    <option v-for="rarity in rarities" :key="rarity" :value="rarity">{{ rarity }}</option>
                </select>
            </div>
            
            <!-- Display Selected Filters -->
            <div v-if="filter.weaponType.length || filter.rarity.length" class="mt-4 p-2 bg-gray-800 rounded-lg">
                <h3 class="text-gray-400">Selected Filters:</h3>
                <div class="flex flex-wrap gap-2 rounded-lg">
                    <!-- Selected Weapons -->
                    <span 
                        v-for="weapon in filter.weaponType" 
                        :key="weapon" 
                        class="bg-blue-600 p-2 flex rounded-lg items-center space-x-2"
                    >
                        <span>{{ weapon }}</span>
                        <button @click="removeFilter('weaponType', weapon)" class="text-white">✕</button>
                    </span>

                    <!-- Selected Rarities -->
                    <span 
                        v-for="rarity in filter.rarity" 
                        :key="rarity" 
                        class="bg-green-600 p-2 flex rounded-lg items-center space-x-2"
                    >
                        <span>{{ rarity }}</span>
                        <button @click="removeFilter('rarity', rarity)" class="text-white">✕</button>
                    </span>
                </div>
            </div>
    
        <!-- Main Content: Responsive Layout -->
        <div class="flex flex-col md:flex-row gap-4 mt-4">
            <!-- Left Section: Skins List & Pagination -->
            <div class="w-full md:w-2/5 bg-gray-800 p-4 rounded-lg flex flex-col">
                <div class="flex flex-col gap-4 flex-grow">
                    <template v-for="(skin, index) in paginatedSkins" :key="skin.name">
                        <div 
                        @click="selectSkin(skin)"
                        class="cursor-pointer bg-gray-700 p-4 rounded-lg flex items-center space-x-4 hover:bg-gray-600 transition-all min-h-[60px]"
                        :class="{ 'border-2 border-green-400': selectedSkin && selectedSkin.name === skin.name }"
                        >
                        <div 
                            class="left-0 top-0 h-full w-5 rounded-l p-0"
                            :style="{ backgroundColor: rarityColors[skin.rarity] || '#6B7280' }"
                        ></div>
                        <img 
                            :src="`/src/images/gun/${skin.weapon.replace(/ /g, '_')}/${skin.rarity}/${skin.name.replace(/ /g, '_')}.png`" 
                            :alt="skin.name" 
                            class="w-14 h-10"
                        />
                        <div class="flex-1">
                            <h2 class="text-lg font-semibold">{{ skin.name }}</h2>
                            <p class="text-gray-400">Gun: {{ skin.weapon }}</p>
                        </div>
                        <div class="ml-auto">
                            <p class="text-green-400 text-lg font-bold">{{ skin.avg_price }}</p>
                        </div>
                        </div>
                    </template>

                <!-- Empty Placeholder Items -->
                <template v-for="index in (5 - paginatedSkins.length)" :key="'empty-' + index">
                    <div class="bg-gray-700 p-4 rounded-lg min-h-[60px] opacity-50"></div>
                </template>
            </div>
        
                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-4 mt-4">
                    <button @click="prevPage" :disabled="currentPage === 1" class="p-2 bg-gray-600 text-white rounded disabled:opacity-50">Previous</button>
                    <span class="text-white">{{ currentPage }} / {{ totalPages }}</span>
                    <button @click="nextPage" :disabled="currentPage === totalPages" class="p-2 bg-gray-600 text-white rounded disabled:opacity-50">Next</button>
                </div>
            </div>
    
            <!-- Right Section: Skin Details -->
            <div class="w-full md:w-3/5 bg-gray-800 p-4 rounded-lg flex flex-col items-center">
            <template v-if="selectedSkin">
                <h2 class="text-xl font-bold">{{ selectedSkin.name }}</h2>
                <img 
                    :src="`/src/images/gun/${selectedSkin.weapon.replace(/ /g, '_')}/${selectedSkin.rarity}/${selectedSkin.name.replace(/ /g, '_')}.png`" 
                    :alt="selectedSkin.name" 
                    class="w-64 h-48"
                />
                <p class="text-gray-400"><strong>Gun:</strong> {{ selectedSkin.weapon }}</p>
                <p class="text-gray-400"><strong>Rarity:</strong> {{ selectedSkin.rarity }}</p>

                <!-- Price Selection -->
                <div class="mt-4 w-full flex flex-col items-center">
                    <p class="text-gray-400"><strong>Price:</strong> {{ selectedSkin.min_price }} - {{ selectedSkin.max_price }}</p>
                    <input
                        type="number"
                        v-model="selectedPrice"
                        @keyup="validatePrice"
                        class="p-2 rounded bg-gray-700 text-white"
                    />
                    <p class="text-red-400 mt-2">{{ priceError }}</p>
                    <p class="text-green-400 text-lg font-bold mt-2">{{ selectedPrice }} €</p>
                </div>

                <!-- Buy & Sell Buttons -->
                <div class="flex mt-4 gap-4">
                    <button 
                        class="px-4 py-2 bg-green-600 text-white rounded disabled:bg-gray-500 disabled:cursor-not-allowed"
                        @click="buyItem"
                        :disabled="priceError !== ''"
                    >
                        Buy
                    </button>

                    <button 
                        class="px-4 py-2 bg-blue-600 text-white rounded disabled:bg-gray-500 disabled:cursor-not-allowed"
                        @click="sellItem"
                        :disabled="priceError !== ''"
                    >
                        Sell
                    </button>
                </div>
            </template>
            <p v-else class="text-gray-500 text-lg">Select a skin to view details.</p>
        </div>
        </div>
        </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchQuery: "",
        priceError: "",
        showFilter: false,
        filter: {
          weaponType: [],
          rarity: []
        },
        rarityColors: {
        "1": "#4B69FF",
        "2": "#8847FF",
        "3": "#D32CE6",
        "4": "#EB4B4B",
        "5": "#FFD700"
        },
        weaponTypes: [],
        rarities: [],
        skins: [],
        selectedSkin: null,
        selectedPrice: 0,
        currentPage: 1,
        skinsPerPage: 5
      };
    },
    computed: {
        filteredSkins() {
        return this.skins.filter(skin => {
        const matchesWeaponType = this.filter.weaponType.length === 0 || this.filter.weaponType.includes(skin.weapon);
        const matchesRarity = this.filter.rarity.length === 0 || this.filter.rarity.includes(skin.rarity);
        const matchesSearchQuery = !this.searchQuery.trim() || 
            skin.name.toLowerCase().includes(this.searchQuery.toLowerCase().trim());

        return matchesWeaponType && matchesRarity && matchesSearchQuery;
        });
    },
      totalPages() {
        return Math.ceil(this.filteredSkins.length / this.skinsPerPage);
      },
      paginatedSkins() {
        const start = (this.currentPage - 1) * this.skinsPerPage;
        const end = start + this.skinsPerPage;
        return this.filteredSkins.slice(start, end);
      }
    },
    watch: {
        'filter.weaponType'() {
            this.currentPage = 1;
        },
        'filter.rarity'() {
            this.currentPage = 1;
        }
    },
    methods: {
      applyFilters() {
        this.currentPage = 1;
      },
      addFilter(type, value) {
        if (value === "All") {
            this.filter[type] = [];
        } else if (value && !this.filter[type].includes(value)) {
            this.filter[type].push(value);
        }
        this.filter[type].sort();
        applyFilters();
      },
      removeFilter(type, value) {
        this.filter[type] = this.filter[type].filter(item => item !== value);
        applyFilters();
      },
      prevPage() {
        if (this.currentPage > 1) this.currentPage--;
      },
      nextPage() {
        if (this.currentPage < this.totalPages) this.currentPage++;
      },
      selectSkin(skin) {
        this.selectedSkin = skin;
      },
      validatePrice() {
        let min = this.parsePrice(this.selectedSkin.min_price);
        let max = this.parsePrice(this.selectedSkin.max_price);
        let price = parseFloat(this.selectedPrice);

        if (isNaN(price) || price < min || price > max) {
          this.priceError = `Price must be between ${min.toFixed(2)} € and ${max.toFixed(2)} €`;
        } else {
          this.priceError = "";
        }
      },
      buySkin(skin, price) {
        if (this.priceError) {
          alert("Invalid price!");
          return;
        }
        alert(`Buying ${skin.name} for ${price.toFixed(2)} €`);
      },
      sellSkin(skin, price) {
        if (this.priceError) {
          alert("Invalid price!");
          return;
        }
        alert(`Selling ${skin.name} for ${price.toFixed(2)} €`);
      },
      async loadSkins() {
        function parsePrice(price) {
            if (!price) return NaN;
            return parseFloat(price.replace("€", "").replace(",", ".").trim());
        }
        try {
          const response = await axios.get('/src/images/skins_data.json');
          const data = response.data;
          let extractedSkins = [];
          let weaponTypesSet = new Set();
          let raritiesSet = new Set();
        
          for (const weapon in data) {
            for (const rarity in data[weapon]) {
              for (const skinName in data[weapon][rarity]) {
                const skinData = data[weapon][rarity][skinName];
                extractedSkins.push({
                  weapon,
                  rarity,
                  name: skinName,
                  min_price: skinData.min_price || "N/A",
                  max_price: skinData.max_price || "N/A",
                  avg_price: skinData.min_price && skinData.max_price ? (((parsePrice(skinData.min_price) + parsePrice(skinData.max_price))) / 2).toFixed(2) + " €" : skinData.price
                });
                weaponTypesSet.add(weapon);
                raritiesSet.add(rarity);
              }
            }
          }
  
          this.skins = extractedSkins;
          this.weaponTypes = Array.from(weaponTypesSet).sort();
          this.rarities = Array.from(raritiesSet);
        } catch (error) {
          console.error("Error loading skins:", error);
        }
      }
    },
    mounted() {
      this.loadSkins();
    }
  };
  </script>
  