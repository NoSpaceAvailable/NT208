<template>
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
            <span
                class="inline-flex h-10 w-10 items-center justify-center bg-transparent">
                <svg class="h-6 w-6 text-white dark:text-gray-400 hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M5 1 1 5l4 4" />
                </svg>
                <span class="hidden">Previous</span>
            </span>
        </button>
        <button id="data-carousel-next" type="button"
            class="group absolute right-0 top-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 focus:outline-none opacity-0 hover:opacity-100">
            <span
                class="inline-flex h-10 w-10 items-center justify-center bg-transparent">
                <svg class="h-6 w-6 text-white dark:text-gray-400 hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 9 4-4-4-4" />
                </svg>
                <span class="hidden">Next</span>
            </span>
        </button>
    </div>
</template>

<script>
export default {
    name: 'MainPage',
    data() {
        return {
            currentIndex: 0,
            totalItems: 4, // Number of carousel items
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
</style>