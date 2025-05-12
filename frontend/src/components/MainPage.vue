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
                        currentIndex === index ? 'bg-[#8FC773]' : 'bg-white/50']"
                    :aria-label="'Slide ' + (index + 1)">
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
                                class="bg-[#131313] rounded-xl overflow-hidden hover:shadow-lg hover:shadow-[#8FC773]/20 transition-all duration-300 group">
                                <div
                                    class="relative aspect-square bg-gradient-to-br from-[#1A1A1A] to-[#111111] flex items-center justify-center">
                                    <img :src="item.image" class="w-full h-full object-contain p-4" :alt="item.name" />
                                    <div
                                        class="absolute bottom-2 left-2 right-2 flex justify-between items-center opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="text-xs bg-[#8FC773] text-black px-2 py-1 rounded">
                                            Details
                                        </button>
                                        <button
                                            class="text-xs bg-white/10 text-white px-2 py-1 rounded hover:bg-[#8FC773] hover:text-black transition-colors">
                                            Add to Cart
                                        </button>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <p class="text-sm font-medium text-white truncate">{{ item.name }}</p>
                                    <p class="text-xs text-[#8FC773]/80 mt-1">{{ item.description }}</p>
                                    <div class="flex justify-between items-center mt-2">
                                        <p class="text-sm text-[#8FC773] font-bold">${{ item.price.toFixed(2) }}</p>
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
            currentIndex: 0,
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
            items: [
                {
                    image: '/src/images/items/gun_14.webp',
                    name: "AWP | Asiimov",
                    description: "Field-Tested",
                    price: 299.99,
                    rarity: "4"
                },
                {
                    image: '/src/images/items/gun_15.webp',
                    name: "AK-47 | Vulcan",
                    description: "Minimal Wear",
                    price: 349.99,
                    rarity: "4"
                },
                {
                    image: '/src/images/items/gun_16.webp',
                    name: "M4A4 | Howl",
                    description: "Factory New",
                    price: 399.99,
                    rarity: "5"
                },
                {
                    image: '/src/images/items/gun_17.webp',
                    name: "Desert Eagle | Blaze",
                    description: "Factory New",
                    price: 249.99,
                    rarity: "3"
                },
                {
                    image: '/src/images/items/gun_18.webp',
                    name: "AWP | Dragon Lore",
                    description: "Minimal Wear",
                    price: 449.99,
                    rarity: "5"
                },
                {
                    image: '/src/images/items/knife_gloves_65.webp',
                    name: "Sport Gloves | Pandora's Box",
                    description: "Field-Tested",
                    price: 199.99,
                    rarity: "5"
                },
                {
                    image: '/src/images/items/knife_gloves_67.webp',
                    name: "Karambit | Doppler",
                    description: "Factory New",
                    price: 179.99,
                    rarity: "5"
                },
                {
                    image: '/src/images/items/knife_gloves_68.webp',
                    name: "M9 Bayonet | Crimson Web",
                    description: "Minimal Wear",
                    price: 219.99,
                    rarity: "4"
                },
                {
                    image: '/src/images/items/knife_gloves_69.webp',
                    name: "Butterfly Knife | Fade",
                    description: "Factory New",
                    price: 239.99,
                    rarity: "5"
                },
                {
                    image: '/src/images/items/knife_gloves_70.webp',
                    name: "Driver Gloves | Lunar Weave",
                    description: "Minimal Wear",
                    price: 259.99,
                    rarity: "4"
                }
            ],
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