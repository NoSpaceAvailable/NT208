<template>
    <div class="min-h-screen bg-[#111111]">
        <!-- Carousel Section -->
        <div class="relative w-full bg-[#111111]">
            <div class="relative h-56 overflow-hidden sm:h-64 xl:h-80 2xl:h-96">
                <!-- Carousel Items -->
                <div v-for="(item, index) in carouselItems" :key="index" :class="['absolute inset-0 w-full h-full transition-opacity duration-700',
                    { 'opacity-100 z-10': currentIndex === index, 'opacity-0 z-0': currentIndex !== index }]">
                    <img :src="item.image" class="w-full h-full object-cover" :alt="item.alt" />
                </div>
            </div>

            <!-- Indicators -->
            <div class="absolute bottom-5 left-1/2 z-30 flex -translate-x-1/2 space-x-3">
                <button v-for="(item, index) in carouselItems" :key="'indicator-' + index" @click="currentIndex = index"
                    :class="['h-3 w-3 rounded-full transition-colors',
                        currentIndex === index ? 'bg-[#8FC773]' : 'bg-white/50']" :aria-label="'Slide ' + (index + 1)">
                </button>
            </div>

            <!-- Navigation Arrows -->
            <button @click="prevSlide"
                class="absolute left-0 top-0 z-30 flex h-full items-center justify-center px-4 opacity-0 hover:opacity-100 transition-opacity">
                <div class="h-10 w-10 flex items-center justify-center bg-[#111111]/50 rounded-full">
                    <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 1 1 5l4 4" />
                    </svg>
                </div>
            </button>
            <button @click="nextSlide"
                class="absolute right-0 top-0 z-30 flex h-full items-center justify-center px-4 opacity-0 hover:opacity-100 transition-opacity">
                <div class="h-10 w-10 flex items-center justify-center bg-[#111111]/50 rounded-full">
                    <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 9 4-4-4-4" />
                    </svg>
                </div>
            </button>
        </div>

        <!-- Item Detail Modal -->
        <div v-if="selectedItem" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
            <div class="bg-[#131313] rounded-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
                <div class="p-6">
                    <div class="flex justify-between items-start">
                        <h3 class="text-xl font-bold text-[#8FC773]">{{ selectedItem.name }}</h3>
                        <button @click="selectedItem = null" class="text-white/70 hover:text-white">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    <div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div
                            class="bg-gradient-to-br from-[#1A1A1A] to-[#111111] rounded-lg p-6 flex items-center justify-center">
                            <img :src="getItemImage(selectedItem.name, selectedItem.rarity)" :alt="selectedItem.name"
                                class="max-h-64 object-contain">
                        </div>

                        <div class="space-y-4">
                            <div>
                                <p class="text-sm text-white/80">Type</p>
                                <p class="text-white capitalize">{{ selectedItem.type }}</p>
                            </div>
                            <div>
                                <p class="text-sm text-white/80">Rarity</p>
                                <p :style="getRarityStyle(selectedItem.rarity)"
                                    class="inline-block px-2 py-1 rounded text-sm">
                                    {{ getRarityName(selectedItem.rarity) }}
                                </p>
                            </div>
                            <div>
                                <p class="text-sm text-white/80">Current price</p>
                                <p class="text-[#8FC773] font-bold">{{ selectedItem.price.toFixed(2) }} {{ currency }}
                                </p>
                            </div>
                            <div v-if="selectedItem.collection">
                                <p class="text-sm text-white/80">Collection</p>
                                <p class="text-white">{{ selectedItem.collection }}</p>
                            </div>
                        </div>
                    </div>

                    <div class="mt-6 pt-6 border-t border-gray-700 flex space-x-3">
                        <button @click="this.$router.push('/merchandise')"
                            class="flex-1 py-2 bg-[#8FC773] text-black rounded-lg font-medium hover:bg-[#7BBF5A]">
                            Find on market
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="max-w-7xl mx-auto p-4 md:p-2">
            <!-- News & Items Grid -->
            <div class="flex flex-col lg:flex-row gap-6">
                <!-- News Section (Left Column) -->
                <div class="w-full lg:w-1/4">
                    <div class="bg-[#111111]/80 rounded-xl shadow-xl p-2">
                        <h1 class="text-2xl font-bold text-[#8FC773] mb-2 text-center">Latest News</h1>
                        <p class="text-sm text-[#8FC773]/80 mb-6 text-center">Stay updated with CS:GO news and updates
                        </p>

                        <div class="space-y-6">
                            <div v-for="(news, index) in newsItems" :key="index"
                                class="bg-[#131313] rounded-lg overflow-hidden hover:shadow-[#8FC773]/20 hover:shadow-lg transition-all duration-300">
                                <a :href="news.link" target="_blank" class="block">
                                    <img :src="news.image" class="w-full h-48 object-cover" :alt="news.title" />
                                    <div class="p-4">
                                        <h2 class="text-lg font-semibold text-white mb-2">{{ news.title }}</h2>
                                        <p class="text-sm text-[#8FC773]/80">{{ news.description }}</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Items Section (Right Column) -->
                <div class="w-full">
                    <div class="bg-[#111111]/80 rounded-xl shadow-xl p-2 h-full">
                        <h1 class="text-2xl font-bold text-[#8FC773] mb-6">Featured Items</h1>

                        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
                            <div v-for="(item, index) in items" :key="index"
                                class="bg-[#131313] rounded-xl overflow-hidden hover:shadow-lg hover:shadow-[#8FC773]/20 transition-all duration-300 group"
                                @click="selectItem(item)">
                                <div
                                    class="relative aspect-square bg-gradient-to-br from-[#1A1A1A] to-[#111111] flex items-center justify-center">
                                    <img :src="item.image" class="w-full h-full object-contain p-4" :alt="item.name" />
                                </div>
                                <div class="p-3">
                                    <p class="text-sm font-medium text-white truncate">{{ item.name }}</p>
                                    <p class="text-xs text-[#8FC773]/80 mt-1">{{ item.collection }}</p>
                                    <div class="flex justify-between items-center mt-2">
                                        <p class="text-sm text-[#8FC773] font-bold">{{ item.price.toFixed(2) }} {{
                                            currency }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MainPage',
    data() {
        return {
            selectedItem: null,
            rarityColors: {
                '1': { background: '#4B69FF', text: '#FFFFFF' }, // Industrial
                '2': { background: '#8847FF', text: '#FFFFFF' }, // Mil-Spec
                '3': { background: '#D32CE6', text: '#FFFFFF' }, // Restricted
                '4': { background: '#EB4B4B', text: '#FFFFFF' }, // Classified
                '5': { background: '#FFD700', text: '#000000' }, // Covert
            },
            rarityNames: {
                '1': 'Industrial',
                '2': 'Mil-Spec',
                '3': 'Restricted',
                '4': 'Classified',
                '5': 'Covert'
            },
            currentIndex: 0,
            currency: 'VND',
            carouselItems: [
                { image: '/src/images/banner1.png', alt: 'Banner 1' },
                { image: '/src/images/banner2.png', alt: 'Banner 2' },
                { image: '/src/images/banner3.png', alt: 'Banner 3' },
                { image: '/src/images/banner4.png', alt: 'Banner 4' }
            ],
            newsItems: [
                {
                    title: 'Champions of Shanghai',
                    description: 'The Perfect World Shanghai Grand Final was one to remember.',
                    image: '/src/images/news1.jpg',
                    link: 'https://www.counter-strike.net/newsentry/529833471389991079'
                },
                {
                    title: 'Season\'s Greetings',
                    description: 'Welcome to Premier Season Two.',
                    image: '/src/images/news2.png',
                    link: 'https://www.counter-strike.net/newsentry/520830071182721028'
                }
            ],
            items: [],
            autoSlideInterval: null
        };
    },
    mounted() {
        this.startAutoSlide();
    },
    beforeUnmount() {
        this.stopAutoSlide();
    },
    methods: {
        constructItemName(item_kind, item_name) {
            return item_kind + ' | ' + item_name;
        },
        getRarityName(rarity) {
            return this.rarityNames[rarity] || 'Unknown';
        },
        getRarityStyle(rarity) {
            const style = this.rarityColors[rarity] || { background: '#CCCCCC', text: '#000000' };
            return {
                backgroundColor: style.background,
                color: style.text
            };
        },
        selectItem(item) {
            console.log(item);  
            this.selectedItem = item;
        },
        getItemImage(_name, rarity) {
            const parts = _name.split(' | ')
            const kind = parts[0].replaceAll(' ', '_');
            const skin_name = parts[1].replaceAll(' ', '_');
            return `/src/images/gun/${kind}/${rarity}/${skin_name}.png`;
        },
        async fetchTopTen() {
            try {
                const response = await fetch('/api/product/list?featured=1');

                if (response.ok) {
                    const data = await response.json();
                    data.forEach(item => {
                        const _name = this.constructItemName(item.kind, item.name)
                        this.items.push({
                            "name": _name,
                            "collection": item.collection,
                            "price": parseInt(item.price),
                            "rarity": item.rarity,
                            "image": this.getItemImage(_name, item.rarity)
                        })
                    });
                }
            } catch (err) {
                console.log(`Error while fetching top 10 items: ${err}`);
            }
        },
        prevSlide() {
            this.currentIndex = (this.currentIndex - 1 + this.carouselItems.length) % this.carouselItems.length;
        },
        nextSlide() {
            this.currentIndex = (this.currentIndex + 1) % this.carouselItems.length;
        },
        startAutoSlide() {
            this.autoSlideInterval = setInterval(() => {
                this.nextSlide();
            }, 4000);
        },
        stopAutoSlide() {
            if (this.autoSlideInterval) {
                clearInterval(this.autoSlideInterval);
            }
        }
    },
    async mounted() {
        await this.fetchTopTen();
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

/* Smooth transitions */
.carousel-item {
    transition: opacity 700ms ease-in-out;
}
</style>