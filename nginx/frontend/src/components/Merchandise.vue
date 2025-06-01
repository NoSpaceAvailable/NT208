<template>
    <div class="min-h-screen p-4 md:p-8 bg-[url('/src/images/shop_wallpaper.png')] bg-cover bg-center">
        <!-- Header & Search Bar -->
        <div class="max-w-7xl mx-auto mb-6">
            <div class="bg-[#111111]/80 rounded-xl shadow-xl p-4 md:p-6">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <h1 class="text-2xl font-bold text-[#8FC773]">Skin marketplace</h1>
                    <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
                        <div class="relative flex-1">
                            <input v-model="searchQuery" @keyup="applyFilters" placeholder="Search skins..."
                                class="w-full p-2 pl-10 bg-[#131313] rounded-lg border border-gray-600 text-white focus:outline-none focus:ring-1 focus:ring-[#8FC773]" />
                            <svg class="absolute left-3 top-2.5 h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                        </div>
                        <button @click="showFilter = !showFilter"
                            class="px-4 py-2 bg-[#8FC773] text-black font-medium rounded-lg hover:bg-[#7BBF5A] transition-colors">
                            Filters
                        </button>
                    </div>
                </div>

                <!-- Filters -->
                <div v-if="showFilter" class="mt-4 pt-4 border-t border-gray-700">
                    <div class="flex flex-col md:flex-row md:items-center gap-4">
                        <!-- Gun Filter -->
                        <div class="flex-1">
                            <label class="block text-sm text-[#8FC773] mb-1">Weapon Type</label>
                            <select @change="addFilter('weaponType', $event.target.value)"
                                class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                                <option value="All">All Weapons</option>
                                <option v-for="weapon in weaponTypes" :key="weapon" :value="weapon"
                                    v-html="formatWeaponType(weapon)"></option>
                            </select>
                        </div>

                        <!-- Rarity Filter -->
                        <div class="flex-1">
                            <label class="block text-sm text-[#8FC773] mb-1">Rarity</label>
                            <select @change="addFilter('rarity', $event.target.value)"
                                class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                                <option value="All">All Rarities</option>
                                <option v-for="rarity in rarities" :key="rarity" :value="rarity"
                                    :style="{ color: rarityColors[rarity] }">
                                    {{ rarityString[rarity] }}
                                </option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Display Selected Filters -->
                <div v-if="filter.weaponType.length || filter.rarity.length" class="mt-4 pt-4 border-t border-gray-700">
                    <h3 class="text-sm text-white mb-2">Active Filters:</h3>
                    <div class="flex flex-wrap gap-2">
                        <!-- Selected Weapons -->
                        <span v-for="weapon in filter.weaponType" :key="weapon"
                            class="px-3 py-1.5 bg-[#8FC773] rounded-full flex items-center space-x-1 text-sm">
                            <span v-html="formatWeaponType(weapon)"></span>
                            <button @click="removeFilter('weaponType', weapon)" class="text-[#131313] hover:text-white">
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </button>
                        </span>

                        <!-- Selected Rarities -->
                        <span v-for="rarity in filter.rarity" :key="rarity"
                            class="px-3 py-1.5 rounded-full flex items-center space-x-1 text-sm"
                            :style="{ backgroundColor: rarityBgColors[rarity], color: rarityTextColors[rarity] }">
                            <span>{{ rarityString[rarity] }}</span>
                            <button @click="removeFilter('rarity', rarity)" class="hover:text-white">
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </button>
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row gap-6">
                <!-- Left Section: Skins List -->
                <div class="w-full lg:w-2/5">
                    <div class="bg-[#111111]/80 rounded-xl shadow-xl p-4 md:p-6">
                        <!-- Skin List -->
                        <div class="space-y-3">
                            <div v-for="skin in paginatedSkins" :key="skin.name" @click="selectSkin(skin)"
                                class="cursor-pointer bg-[#131313] p-3 rounded-lg flex items-center space-x-4 hover:bg-[#1A1A1A] transition-colors border border-transparent"
                                :class="{ 'border-[#8FC773]': selectedSkin && selectedSkin.name === skin.name && selectedSkin.weapon === skin.weapon }">
                                <div class="w-3 h-12 rounded"
                                    :style="{ backgroundColor: rarityColors[skin.rarity] || '#6B7280' }"></div>
                                <img :src="`/src/images/gun/${skin.weapon.replace(/ /g, '_')}/${skin.rarity}/${skin.name.replace(/ /g, '_')}.png`"
                                    :alt="skin.name" class="w-16 h-12 object-contain" />
                                <div class="flex-1 min-w-0">
                                    <h2 class="text-md font-semibold text-white truncate">{{ skin.name }}</h2>
                                    <p class="text-gray-400 text-sm" v-html="formatWeaponType(skin.weapon)"></p>
                                </div>
                                <div class="ml-auto text-right">
                                    <p class="text-[#8FC773] font-bold">{{ skin.avg_price }}</p>
                                    <p class="text-xs text-gray-400">avg. price</p>
                                </div>
                            </div>

                            <!-- Empty State -->
                            <div v-if="filteredSkins.length === 0" class="bg-[#131313] p-6 rounded-lg text-center">
                                <svg class="mx-auto h-10 w-10 text-gray-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <h3 class="mt-2 text-sm font-medium text-white">No skins found</h3>
                                <p class="mt-1 text-sm text-gray-400">
                                    Try adjusting your search or filters
                                </p>
                            </div>

                            <!-- Pagination -->
                            <div v-if="filteredSkins.length > 0"
                                class="flex justify-between items-center mt-4 pt-4 border-t border-gray-700">
                                <button @click="prevPage" :disabled="currentPage === 1"
                                    class="px-4 py-2 bg-[#131313] text-white rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-[#1A1A1A] transition-colors">
                                    Previous
                                </button>
                                <span class="text-sm text-white">Page {{ currentPage }} of {{ totalPages }}</span>
                                <button @click="nextPage" :disabled="currentPage === totalPages"
                                    class="px-4 py-2 bg-[#131313] text-white rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-[#1A1A1A] transition-colors">
                                    Next
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Section: Skin Details -->
                <div class="w-full lg:w-3/5">
                    <div class="bg-[#111111]/80 rounded-xl shadow-xl p-4 md:p-6 h-full">
                        <template v-if="selectedSkin">
                            <div class="flex flex-col items-center">
                                <h2 class="text-2xl font-bold text-[#8FC773] mb-2">{{ selectedSkin.name }}</h2>
                                <div
                                    class="relative w-full max-w-md aspect-video bg-[#131313] rounded-lg mb-4 flex items-center justify-center">
                                    <img :src="`/src/images/gun/${selectedSkin.weapon.replace(/ /g, '_')}/${selectedSkin.rarity}/${selectedSkin.name.replace(/ /g, '_')}.png`"
                                        :alt="selectedSkin.name" class="max-h-64 object-contain" />
                                    <div class="absolute bottom-2 left-2">
                                        <span class="px-2 py-1 rounded text-xs font-medium"
                                            :style="{ backgroundColor: rarityBgColors[selectedSkin.rarity], color: rarityTextColors[selectedSkin.rarity] }">
                                            {{ rarityToString(selectedSkin.rarity) }}
                                        </span>
                                    </div>
                                </div>

                                <div class="w-full max-w-md grid grid-cols-2 gap-4 mb-6">
                                    <div class="bg-[#131313] p-3 rounded-lg">
                                        <p class="text-sm text-gray-400">Type</p>
                                        <p class="text-white" v-html="formatWeaponType(selectedSkin.weapon)"></p>
                                    </div>
                                    <div class="bg-[#131313] p-3 rounded-lg">
                                        <p class="text-sm text-gray-400">Price Range</p>
                                        <p class="text-white">{{ selectedSkin.min_price }} - {{ selectedSkin.max_price
                                        }}</p>
                                    </div>
                                </div>

                                <!-- Action Buttons -->
                                <div class="w-full max-w-md space-y-4">
                                    <div class="flex gap-3">
                                        <button @click="findSellers" :disabled="loadingSellers"
                                            class="flex-1 py-3 bg-[#8FC773] text-black font-bold rounded-lg hover:bg-[#7BBF5A] transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
                                            <span v-if="!loadingSellers">Find sellers</span>
                                            <span v-else class="flex items-center justify-center">
                                                <div
                                                    class="animate-spin rounded-full h-4 w-4 border-b-2 border-black mr-2">
                                                </div>
                                                Loading...
                                            </span>
                                        </button>
                                        <button @click="sellItem"
                                            class="flex-1 py-3 bg-white/10 text-white font-bold rounded-lg hover:text-[#8FC773] transition-colors">
                                            Sell
                                        </button>
                                    </div>
                                </div>

                                <!-- Seller List Section -->
                                <div v-if="sellers.length > 0" class="w-full mt-6 pt-6 border-t border-gray-700">
                                    <h3 class="text-lg font-semibold text-[#8FC773] mb-4">Available sellers</h3>
                                    <!-- Horizontal scrollable seller list -->
                                    <div class="flex gap-4 overflow-x-auto pb-2 seller-scroll">
                                        <div v-for="seller in sellers" :key="seller.id"
                                            class="flex-shrink-0 bg-[#131313] p-4 rounded-lg hover:bg-[#1A1A1A] transition-colors min-w-[200px]">
                                            <div class="flex flex-col items-center space-y-3">
                                                <!-- Profile Avatar -->
                                                <div
                                                    class="w-12 h-12 bg-[#8FC773] rounded-full flex items-center justify-center">
                                                    <svg class="w-6 h-6 text-black" fill="currentColor"
                                                        viewBox="0 0 20 20">
                                                        <path fill-rule="evenodd"
                                                            d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                                                            clip-rule="evenodd" />
                                                    </svg>
                                                </div>

                                                <!-- Profile Name -->
                                                <div class="text-center">
                                                    <p class="text-white font-medium text-sm">{{ seller.profile_name ||
                                                        'Loading...' }}</p>
                                                    <p class="text-gray-400 text-xs">ID: {{ seller.id }}</p>
                                                </div>

                                                <!-- Action Buttons -->
                                                <div class="flex flex-col gap-2 w-full">
                                                    <button @click="redirectToProfile(seller.id)"
                                                        class="px-3 py-2 bg-[#8FC773] text-black text-sm rounded hover:bg-[#7BBF5A] transition-colors font-medium">
                                                        View profile
                                                    </button>
                                                    <button @click="redirectToInventory(seller.id)"
                                                        class="px-3 py-2 bg-blue-500 text-white text-sm rounded hover:bg-blue-600 transition-colors font-medium">
                                                        View inventory
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Loading State for Sellers -->
                                    <div v-if="loadingSellers" class="flex justify-center items-center py-8">
                                        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#8FC773]">
                                        </div>
                                        <span class="ml-3 text-gray-400">Loading sellers...</span>
                                    </div>
                                </div>
                            </div>
                        </template>
                        <template v-else>
                            <div class="flex flex-col items-center justify-center h-full py-12">
                                <svg class="h-16 w-16 text-gray-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z" />
                                </svg>
                                <h3 class="mt-4 text-lg font-medium text-white">Select a skin</h3>
                                <p class="mt-1 text-gray-400 text-center max-w-md">
                                    Choose a skin from the list to view details and trading options
                                </p>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useNotification } from '../services/notificationService';

export default {
    name: 'MerchandisePage',
    setup() {
        const { showNotification } = useNotification();
        return { showNotification };
    },
    data() {
        return {
            currency: "VND",
            searchQuery: "",
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
            rarityBgColors: {
                "1": "rgba(75, 105, 255, 0.2)",
                "2": "rgba(136, 71, 255, 0.2)",
                "3": "rgba(211, 44, 230, 0.2)",
                "4": "rgba(235, 75, 75, 0.2)",
                "5": "rgba(255, 215, 0, 0.2)"
            },
            rarityTextColors: {
                "1": "#4B69FF",
                "2": "#8847FF",
                "3": "#D32CE6",
                "4": "#EB4B4B",
                "5": "#FFD700"
            },
            rarityString: {
                "1": "Industrial",
                "2": "Mil-spec",
                "3": "Restricted",
                "4": "Classified",
                "5": "Covert"
            },
            weaponTypes: [],
            rarities: [],
            skins: [],
            selectedSkin: null,
            currentPage: 1,
            skinsPerPage: 5,
            sellers: [],
            loadingSellers: false
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
            const end = Math.min(start + this.skinsPerPage, this.filteredSkins.length);
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
        formatWeaponType(weapon) {
            return weapon.replace('★', '<span style="color: #FFD700">★</span>');
        },
        rarityToString(rarity) {
            return this.rarityString[rarity];
        },
        applyFilters() {
            this.currentPage = 1;
            this.selectedSkin = null;
            this.sellers = []; // Clear sellers when filters change
        },
        addFilter(type, value) {
            if (value === "All") {
                this.filter[type] = [];
            } else if (value && !this.filter[type].includes(value)) {
                this.filter[type].push(value);
            }
            this.filter[type].sort();
            this.applyFilters();
        },
        removeFilter(type, value) {
            this.filter[type] = this.filter[type].filter(item => item !== value);
            this.applyFilters();
        },
        prevPage() {
            if (this.currentPage > 1) this.currentPage--;
        },
        nextPage() {
            if (this.currentPage < this.totalPages) this.currentPage++;
        },
        selectSkin(skin) {
            this.selectedSkin = skin;
            this.sellers = []; // Clear sellers when selecting new skin
        },
        parsePrice(price) {
            if (!price) return 0;
            return parseFloat(price.toString().replace(/[^0-9.,]/g, "").replace(",", ".").trim());
        },
        async fetchProfileName(userId) {
            try {
                const response = await fetch(`/api/profile/fetch/${userId}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                return data.profile?.profile_name || `User ${userId}`;
            } catch (error) {
                console.error(`Error fetching profile for user ${userId}:`, error);
                return `User ${userId}`;
            }
        },
        async findSellers() {
            if (!this.selectedSkin) {
                this.showNotification('No skin selected', {
                    type: 'error',
                    description: 'Please select a skin first'
                });
                return;
            }

            this.loadingSellers = true;
            this.sellers = [];

            try {
                const kind = encodeURIComponent(this.selectedSkin.weapon);
                const name = encodeURIComponent(this.selectedSkin.name);
                const response = await fetch(`/api/product/seller?kind=${kind}&name=${name}`);

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const sellerIds = await response.json();

                if (Array.isArray(sellerIds) && sellerIds.length > 0) {
                    // Initialize sellers array with IDs
                    this.sellers = sellerIds.map(id => ({
                        id: id,
                        profile_name: null // Will be loaded asynchronously
                    }));

                    // Fetch profile names for each seller
                    const profilePromises = sellerIds.map(async (id) => {
                        const profileName = await this.fetchProfileName(id);
                        // Update the seller object with the fetched profile name
                        const seller = this.sellers.find(s => s.id === id);
                        if (seller) {
                            seller.profile_name = profileName;
                        }
                    });

                    // Wait for all profile fetches to complete
                    await Promise.all(profilePromises);

                    this.showNotification(`Found ${this.sellers.length} sellers`, {
                        type: 'success',
                        description: `Available sellers for ${this.selectedSkin.name}`
                    });
                } else {
                    this.sellers = [];
                    this.showNotification('No sellers found', {
                        type: 'info',
                        description: 'No sellers are currently offering this item'
                    });
                }
            } catch (error) {
                console.error("Error fetching sellers:", error);
                this.showNotification('Failed to load sellers', {
                    type: 'error',
                    description: 'Please try again later'
                });
                this.sellers = [];
            } finally {
                this.loadingSellers = false;
            }
        },
        redirectToProfile(userId) {
            window.location.href = `/profile?id=${userId}`;
        },
        redirectToInventory(userId) {
            window.location.href = `/inventory?id=${userId}`;
        },
        sellItem() {
            this.$router.push('/inventory');
        },
        async loadSkins() {
            try {
                const response = await fetch('/api/product/list', {
                    method: 'GET',
                    credentials: 'include'
                });
                const data = await response.json();
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
                                min_price: skinData.min_price ? `${this.parsePrice(skinData.min_price).toFixed(2)} ${this.currency}` : "N/A",
                                max_price: skinData.max_price ? `${this.parsePrice(skinData.max_price).toFixed(2)} ${this.currency}` : "N/A",
                                avg_price: skinData.min_price && skinData.max_price
                                    ? `${((this.parsePrice(skinData.min_price) + this.parsePrice(skinData.max_price)) / 2).toFixed(2)} ${this.currency}`
                                    : skinData.price || "N/A"
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
                this.showNotification('Failed to load skins', {
                    type: 'error',
                    description: 'Please try again later'
                });
            }
        }
    },
    mounted() {
        this.loadSkins();
    }
};
</script>

<style scoped>
/* Custom scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: #1A1A1A;
    border-radius: 3px;
}

::-webkit-scrollbar-thumb {
    background: #8FC773;
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: #7BBF5A;
}

/* Seller scroll container */
.seller-scroll {
    scrollbar-width: thin;
    scrollbar-color: #8FC773 #1A1A1A;
}

.seller-scroll::-webkit-scrollbar {
    height: 8px;
}

.seller-scroll::-webkit-scrollbar-track {
    background: #1A1A1A;
    border-radius: 4px;
}

.seller-scroll::-webkit-scrollbar-thumb {
    background: #8FC773;
    border-radius: 4px;
}

.seller-scroll::-webkit-scrollbar-thumb:hover {
    background: #7BBF5A;
}
</style>