<template>
    <div style="display: contents">
        <div id="carousel-example" class="relative w-full">
            <!-- Carousel wrapper -->
            <div class="relative h-56 overflow-hidden sm:h-64 xl:h-80 2xl:h-96">
                <!-- Item 1 -->
                <div id="carousel-item-1"
                    :class="['carousel-item', 'absolute', 'inset-0', 'w-full', 'h-full', { 'active': currentIndex === 0 }]">
                    <img src="@/images/banner1.png" class="w-full h-full object-cover" alt="banner1" />
                </div>
                <!-- Item 2 -->
                <div id="carousel-item-2"
                    :class="['carousel-item', 'absolute', 'inset-0', 'w-full', 'h-full', { 'active': currentIndex === 1 }]">
                    <img src="@/images/banner2.png" class="w-full h-full object-cover" alt="banner2" />
                </div>
                <!-- Item 3 -->
                <div id="carousel-item-3"
                    :class="['carousel-item', 'absolute', 'inset-0', 'w-full', 'h-full', { 'active': currentIndex === 2 }]">
                    <img src="@/images/banner3.png" class="w-full h-full object-cover" alt="banner3" />
                </div>
                <!-- Item 4 -->
                <div id="carousel-item-4"
                    :class="['carousel-item', 'absolute', 'inset-0', 'w-full', 'h-full', { 'active': currentIndex === 3 }]">
                    <img src="@/images/banner4.png" class="w-full h-full object-cover" alt="banner4" />
                </div>
            </div>
            <!-- Slider indicators -->
            <div class="absolute bottom-5 left-1/2 z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse">
                <button id="carousel-indicator-1" type="button"
                    :class="['h-3', 'w-3', 'rounded-full', { 'bg-white': currentIndex === 0, 'bg-white/50': currentIndex !== 0 }]"
                    aria-current="true" aria-label="Slide 1"></button>
                <button id="carousel-indicator-2" type="button"
                    :class="['h-3', 'w-3', 'rounded-full', { 'bg-white': currentIndex === 1, 'bg-white/50': currentIndex !== 1 }]"
                    aria-current="false" aria-label="Slide 2"></button>
                <button id="carousel-indicator-3" type="button"
                    :class="['h-3', 'w-3', 'rounded-full', { 'bg-white': currentIndex === 2, 'bg-white/50': currentIndex !== 2 }]"
                    aria-current="false" aria-label="Slide 3"></button>
                <button id="carousel-indicator-4" type="button"
                    :class="['h-3', 'w-3', 'rounded-full', { 'bg-white': currentIndex === 3, 'bg-white/50': currentIndex !== 3 }]"
                    aria-current="false" aria-label="Slide 4"></button>
            </div>
            <!-- Slider controls -->
            <button id="data-carousel-prev" type="button"
                class="group absolute left-0 top-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 focus:outline-none opacity-0 hover:opacity-100">
                <span class="inline-flex h-10 w-10 items-center justify-center bg-transparent">
                    <svg class="h-6 w-6 text-white dark:text-gray-400 hover:text-white" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 1 1 5l4 4" />
                    </svg>
                    <span class="hidden">Previous</span>
                </span>
            </button>
            <button id="data-carousel-next" type="button"
                class="group absolute right-0 top-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 focus:outline-none opacity-0 hover:opacity-100">
                <span class="inline-flex h-10 w-10 items-center justify-center bg-transparent">
                    <svg class="h-6 w-6 text-white dark:text-gray-400 hover:text-white" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 9 4-4-4-4" />
                    </svg>
                    <span class="hidden">Next</span>
                </span>
            </button>
        </div>
        <!-- Main Content Section -->
        <div class="flex flex-1 w-full h-full bg-[url(/src/images/navi.png)] bg-cover bg-center">
            <!-- News Section (20% width) -->
            <div class="flex-1 flex flex-col m-8" style="flex-basis: 20%;">
                <!-- News Header -->
                <div class="text-center mb-6">
                    <h1 class="text-3xl font-bold text-[#8FC773]">Latest news</h1>
                    <p class="text-[#8FC773]">Stay updated with the most recent CS:GO news and updates.</p>
                </div>

                <!-- News Cards -->
                <div class="flex-1 space-y-6">
                    <div
                        class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                        <a href="https://www.counter-strike.net/newsentry/529833471389991079" target="_blank">
                            <img src="@/images/news1.jpg" class="w-full h-48 object-cover" alt="news1" />
                            <div class="p-4">
                                <h2 class="text-xl font-semibold mb-2">Champions of Shanghai</h2>
                                <p class="text-gray-600">The Perfect World Shanghai Grand Final was one to remember.</p>
                            </div>
                        </a>
                    </div>
                    <div
                        class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                        <a href="https://www.counter-strike.net/newsentry/520830071182721028" target="_blank">
                            <img src="@/images/news2.png" class="w-full h-48 object-cover" alt="news2" />
                            <div class="p-4">
                                <h2 class="text-xl font-semibold mb-2">Season's Greetings</h2>
                                <p class="text-gray-600">Welcome to Premier Season Two.</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Items Section (80% width) -->
            <div class="flex-1 flex flex-col m-4" style="flex-basis: 80%;">
                <!-- Items Grid -->
                <div class="grid grid-cols-5 m-1">
                    <!-- Item Cards -->
                    <div v-for="(item, index) in items" :key="index"
                        class="mr-1 mb-8 bg-[#000000] rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 opacity-90">
                        <img :src="item.image" class="w-full h-42 object-cover p-6" :alt="item.name" />
                        <div class="p-4">
                            <h2 class="text-xl font-semibold mb-2 text-[#8FC773]">{{ item.name }}</h2>
                            <p class="text-[#8FC773]">{{ item.description }}</p>
                            <p class="text-lg font-bold mt-2 text-[#8FC773]">${{ item.price }}</p>
                            <button
                                class="mt-4 w-full text-[#f6f6f6] hover:text-[#8FC773] bg-[#313131] py-2 rounded-lg transition-colors duration-300">
                                Add to Cart
                            </button>
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
            totalItems: 4, // Number of carousel items
            items: [
                {
                    image: "/src/images/items/gun_14.webp",
                    name: "Gun 14",
                    description: "A powerful and reliable weapon.",
                    price: 299.99
                },
                {
                    image: "/src/images/items/gun_15.webp",
                    name: "Gun 15",
                    description: "Perfect for close-range combat.",
                    price: 349.99
                },
                {
                    image: "/src/images/items/gun_16.webp",
                    name: "Gun 16",
                    description: "High precision and accuracy.",
                    price: 399.99
                },
                {
                    image: "/src/images/items/gun_17.webp",
                    name: "Gun 17",
                    description: "Lightweight and easy to handle.",
                    price: 249.99
                },
                {
                    image: "/src/images/items/gun_18.webp",
                    name: "Gun 18",
                    description: "Ideal for long-range engagements.",
                    price: 449.99
                },
                {
                    image: "/src/images/items/knife_gloves_65.webp",
                    name: "Knife Gloves 65",
                    description: "Stylish and deadly. Suite for ADP",
                    price: 199.99
                },
                {
                    image: "/src/images/items/knife_gloves_67.webp",
                    name: "Knife Gloves 67",
                    description: "Durable and comfortable.",
                    price: 179.99
                },
                {
                    image: "/src/images/items/knife_gloves_68.webp",
                    name: "Knife Gloves 68",
                    description: "Perfect for stealth missions.",
                    price: 219.99
                },
                {
                    image: "/src/images/items/knife_gloves_69.webp",
                    name: "Knife Gloves 69",
                    description: "Enhanced grip and control.",
                    price: 239.99
                },
                {
                    image: "/src/images/items/knife_gloves_70.webp",
                    name: "Knife Gloves 70",
                    description: "Premium design and quality.",
                    price: 259.99
                }
            ]
        };
    },
    mounted() {
        this.showSlide(this.currentIndex);
        this.setupEventListeners();
        this.setAutoSlide();
    },
    methods: {
        showSlide(index) {
            this.currentIndex = index;
        },
        prevSlide() {
            this.currentIndex = (this.currentIndex - 1 + this.totalItems) % this.totalItems;
        },
        nextSlide() {
            this.currentIndex = (this.currentIndex + 1) % this.totalItems;
        },
        setupEventListeners() {
            const $prevButton = document.getElementById('data-carousel-prev');
            const $nextButton = document.getElementById('data-carousel-next');

            $prevButton.addEventListener('click', () => {
                this.prevSlide();
            });

            $nextButton.addEventListener('click', () => {
                this.nextSlide();
            });

            const indicators = document.querySelectorAll('[id^="carousel-indicator-"]');
            indicators.forEach((indicator, index) => {
                indicator.addEventListener('click', () => {
                    this.currentIndex = index;
                });
            });
        },
        setAutoSlide() {
            setInterval(() => {
                this.nextSlide();
            }, 4000);
        },
    },
};
</script>

<style scoped>
.carousel-item {
    opacity: 0;
    transition: opacity 700ms ease-in-out;
}

.carousel-item.active {
    opacity: 1;
}

/* Card Hover Effect */
.bg-white:hover {
    transform: translateY(-5px);
    transition: transform 0.3s ease;
}
</style>