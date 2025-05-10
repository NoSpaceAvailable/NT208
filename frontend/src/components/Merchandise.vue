<template>
    <div style="display: contents">
        <div
            class="container mx-auto p-6 bg-[url(/src/images/shop_wallpaper.png)] bg-cover bg-center text-white flex-grow min-h-screen z-10 max-w-full">
            <!-- Header & Search Bar -->
            <div class="relative">
                <div class="absolute inset-0 bg-[#000000] opacity-80 rounded-lg"></div>
                <div class="relative flex items-center justify-between p-4">
                    <h1 class="text-xl font-bold">Skin Storage</h1>
                    <div class="flex space-x-2">
                        <input v-model="searchQuery" @keyup="applyFilters" placeholder="Searching skin..."
                            class="p-2 rounded bg-gray-700 text-white" />
                        <button @click="showFilter = !showFilter" class="p-2 bg-blue-500 text-white rounded">Choose
                            filter</button>
                    </div>
                </div>
            </div>

            <!-- Filters -->
            <div v-if="showFilter" class="mt-4 relative">
                <div class="absolute inset-0 bg-[#000000] opacity-80 rounded-lg"></div>
                <div class="relative p-4">
                    <div class="flex items-center space-x-4">
                        <!-- Gun Filter -->
                        <div>
                            <label class="block text-white">Type:</label>
                            <select @change="addFilter('weaponType', $event.target.value)"
                                class="p-2 rounded bg-gray-700 text-white inline-block whitespace-nowrap">
                                <option value="All">All</option>
                                <option v-for="weapon in weaponTypes" :key="weapon" :value="weapon" v-html="formatWeaponType(weapon)"></option>
                            </select>
                        </div>

                        <!-- Rarity Filter -->
                        <div>
                            <label class="block text-white">Rarity:</label>
                            <select @change="addFilter('rarity', $event.target.value)"
                                class="p-2 rounded bg-gray-700 text-white inline-block whitespace-nowrap">
                                <option value="All">All</option>
                                <option v-for="rarity in rarities" :key="rarity" :value="rarity" :style="{ color: rarityColors[rarity] }">
                                    {{ rarityString[rarity] }}
                                </option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Display Selected Filters -->
            <div v-if="filter.weaponType.length || filter.rarity.length" class="mt-4 relative">
                <div class="absolute inset-0 bg-[#000000] opacity-80 rounded-lg"></div>
                <div class="relative p-2">
                    <h3 class="text-white">Selected Filters:</h3>
                    <div class="flex flex-wrap gap-2 rounded-lg">
                        <!-- Selected Weapons -->
                        <span v-for="weapon in filter.weaponType" :key="weapon"
                            class="bg-blue-600 p-2 flex rounded-lg items-center space-x-2">
                            <span v-html="formatWeaponType(weapon)"></span>
                            <button @click="removeFilter('weaponType', weapon)" class="text-white">✕</button>
                        </span>

                        <!-- Selected Rarities -->
                        <span v-for="rarity in filter.rarity" :key="rarity"
                            class="p-2 flex rounded-lg items-center space-x-2"
                            :style="{ backgroundColor: rarityColors[rarity] }">
                            <span>{{ rarityString[rarity] }}</span>
                            <button @click="removeFilter('rarity', rarity)" class="text-white">✕</button>
                        </span>
                    </div>
                </div>
            </div>

            <!-- Main Content: Responsive Layout -->
            <div class="flex flex-col md:flex-row gap-4 mt-4">
                <!-- Left Section: Skins List & Pagination -->
                <div class="w-full md:w-2/5 relative">
                    <div class="absolute inset-0 bg-[#000000] opacity-80 rounded-lg"></div>
                    <div class="relative p-4 flex flex-col">
                        <div class="flex flex-col gap-4 flex-grow">
                            <div v-for="(skin) in paginatedSkins" :key="skin.name" @click="selectSkin(skin)"
                                class="cursor-pointer bg-gray-700 p-4 rounded-lg flex items-center space-x-4 hover:bg-gray-600 relative"
                                :class="{ 'border-2 border-green-400': selectedSkin && selectedSkin.name === skin.name && selectedSkin.weapon === skin.weapon }">
                                <div class="absolute left-0 top-0 h-full w-5 rounded-l"
                                    :style="{ backgroundColor: rarityColors[skin.rarity] || '#6B7280' }"></div>
                                <img :src="`/src/images/gun/${skin.weapon.replace(/ /g, '_')}/${skin.rarity}/${skin.name.replace(/ /g, '_')}.png`"
                                    :alt="skin.name" class="w-14 h-10" />
                                <div class="flex-1">
                                    <h2 class="text-lg font-semibold">{{ skin.name }}</h2>
                                    <p class="text-gray-400" v-html="formatWeaponType(skin.weapon)"></p>
                                </div>
                                <div class="ml-auto">
                                    <p class="text-green-400 text-lg font-bold">avg. price: {{ skin.avg_price }}</p>
                                </div>
                            </div>

                            <!-- Empty Placeholder Items -->
                            <div v-for="index in (5 - paginatedSkins.length)" :key="'empty-' + index"
                                class="bg-gray-700 p-4 rounded-lg min-h-[60px] opacity-50"></div>
                        </div>

                        <!-- Pagination Controls -->
                        <div class="flex justify-center space-x-4 mt-4">
                            <button @click="prevPage" :disabled="currentPage === 1"
                                class="p-2 bg-gray-600 text-white rounded disabled:opacity-50">Previous</button>
                            <span class="text-white">{{ currentPage }} / {{ totalPages }}</span>
                            <button @click="nextPage" :disabled="currentPage === totalPages"
                                class="p-2 bg-gray-600 text-white rounded disabled:opacity-50">Next</button>
                        </div>
                    </div>
                </div>

                <!-- Right Section: Skin Details -->
                <div class="w-full md:w-3/5 relative">
                    <div class="absolute inset-0 bg-[#000000] opacity-80 rounded-lg"></div>
                    <div class="relative p-4 flex flex-col items-center">
                        <template v-if="selectedSkin">
                            <h2 class="text-xl font-bold">{{ selectedSkin.name }}</h2>
                            <img :src="`/src/images/gun/${selectedSkin.weapon.replace(/ /g, '_')}/${selectedSkin.rarity}/${selectedSkin.name.replace(/ /g, '_')}.png`"
                                :alt="selectedSkin.name" class="w-64 h-48" />
                            <p class="text-white"><strong>Type:</strong> <span v-html="formatWeaponType(selectedSkin.weapon)"></span></p>
                            <p :style="{ color: rarityColors[selectedSkin.rarity] || '#6B7280' }"><strong
                                    class="text-white">Rarity:</strong> <strong>{{ rarityToString(selectedSkin.rarity)
                                    }}</strong></p>

                            <!-- Price Selection -->
                            <div class="mt-4 w-full flex flex-col items-center">
                                <p class="text-white"><strong>Price range:</strong> {{ selectedSkin.min_price }} - {{
                                    selectedSkin.max_price }}</p>
                                <input type="number" v-model="selectedPrice" @keyup="validatePrice"
                                    class="p-2 rounded bg-gray-700 text-white" />
                                <p class="text-red-400 mt-2">{{ priceError }}</p>
                                <p class="text-green-400 text-lg font-bold mt-2">{{ selectedPrice }} {{ currency }}</p>
                            </div>

                            <!-- Buy & Sell Buttons -->
                            <div class="flex mt-4 gap-4">
                                <button
                                    class="px-4 py-2 bg-green-600 text-white rounded disabled:bg-gray-500 disabled:cursor-not-allowed"
                                    @click="buyItem" :disabled="priceError !== ''">
                                    Buy
                                </button>

                                <button
                                    class="px-4 py-2 bg-blue-600 text-white rounded disabled:bg-gray-500 disabled:cursor-not-allowed"
                                    @click="sellItem" :disabled="priceError !== ''">
                                    Sell
                                </button>
                            </div>
                        </template>
                        <p v-else class="text-gray-500 text-lg">Select a skin to view details.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            currency: "€",
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
        },
        validatePrice() {
            let min = this.parsePrice(this.selectedSkin.min_price);
            let max = this.parsePrice(this.selectedSkin.max_price);
            let price = parseFloat(this.selectedPrice);

            if (isNaN(price) || price < min || price > max) {
                this.priceError = `Price must be between ${min.toFixed(2)} ${this.currency} and ${max.toFixed(2)} ${this.currency}`;
            } else {
                this.priceError = "";
            }
        },
        buySkin(skin, price) {
            if (this.priceError) {
                alert("Invalid price!");
                return;
            }
            alert(`Buying ${skin.name} for ${price.toFixed(2)} ${this.currency}`);
        },
        sellSkin(skin, price) {
            if (this.priceError) {
                alert("Invalid price!");
                return;
            }
            alert(`Selling ${skin.name} for ${price.toFixed(2)} ${this.currency}`);
        },
        async loadSkins() {
            function parsePrice(price) {
                if (!price) return NaN;
                return parseFloat(price.replace(/[^0-9.,]/g, "").replace(",", ".").trim());
            }
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
                                min_price: skinData.min_price || "N/A",
                                max_price: skinData.max_price || "N/A",
                                avg_price: skinData.min_price && skinData.max_price ? (((parsePrice(skinData.min_price) + parsePrice(skinData.max_price))) / 2).toFixed(2) + " " + this.currency : skinData.price
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