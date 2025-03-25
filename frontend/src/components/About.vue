<template>
    <div style="display: contents">
        <!-- Video Background -->
        <div class="absolute left-0 w-full h-full overflow-hidden z-0">
            <video autoplay muted loop class="w-full h-full object-cover">
                <source src="/src/videos/auth_wallpaper.mp4" type="video/mp4" />
                Your browser does not support the video tag.
            </video>
        </div>

        <!-- Content Overlay -->
        <div class="flex flex-grow items-center justify-center relative z-10">
            <div class="flex flex-col w-full max-w-lg mx-auto p-8 bg-[#1A1A1A]/90 rounded-xl shadow-xl">
                <div class="text-center pb-6">
                    <h1 class="text-3xl font-extrabold text-[#8FC773]">About our CSGO skin shop</h1>
                    <p class="text-sm text-[#f6f6f6] mt-2">
                        Premium marketplace for the most sought-after CSGO skins, knives, and weapon cases.
                    </p>
                </div>

                <div class="flex flex-col space-y-4">
                    <div class="p-4 bg-[#313131] rounded-lg shadow-md">
                        <h2 class="text-xl font-bold text-[#8FC773]">Why choose us?</h2>
                        <p class="text-sm text-gray-300 mt-2">
                            We offer competitive prices, instant skin delivery, and secure transactions. Trust us to
                            elevate your CSGO experience with top-tier skins.
                        </p>
                    </div>

                    <div class="p-4 bg-[#313131] rounded-lg shadow-md">
                        <h2 class="text-xl font-bold text-[#8FC773]">Our mission</h2>
                        <p class="text-sm text-gray-300 mt-2">
                            To provide a seamless, user-friendly platform for CSGO enthusiasts to buy, sell, and trade
                            skins with confidence.
                        </p>
                    </div>

                    <div class="p-4 bg-[#313131] rounded-lg shadow-md">
                        <h2 class="text-xl font-bold text-[#8FC773]">Join the community</h2>
                        <p class="text-sm text-gray-300 mt-2">
                            Become part of our growing community of CSGO players. Follow us on social media to stay
                            updated on the latest deals and exclusive offers.
                        </p>
                    </div>
                </div>

                <div class="mt-6 text-center">
                    <a href="/"
                        class="bg-[#8FC773] text-[#000000] px-6 py-2 rounded-lg font-medium hover:bg-[#8FC773] hover:text-[#ffffff]">
                        Start shopping now!
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>