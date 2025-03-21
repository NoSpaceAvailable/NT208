<template>
  <div class="min-h-screen flex flex-col items-center bg-gray-100 text-gray-900 p-6">
    <!-- Page Title -->
    <h1 id="title" class="text-3xl font-bold text-blue-600 mb-2">
      {{ title }}
    </h1>

    <!-- Page Banner -->
    <p id="banner" class="text-lg text-gray-700 mb-6">
      {{ banner }}
    </p>

    <!-- Router View -->
    <router-view class="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6" />
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