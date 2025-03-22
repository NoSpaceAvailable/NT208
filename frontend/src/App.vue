<template>
    <div class="min-h-screen flex flex-col items-center bg-gray-100 text-gray-900 h-full w-full">
        <!-- Router View -->
        <router-view />
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: "lqc's game shop",
            banner: "A place where gamers can buy and sell their best items!"
        };
    }
};
</script>