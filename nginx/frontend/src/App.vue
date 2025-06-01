<template>
    <div class="min-h-screen flex flex-col">
        <!-- Router View -->
        <router-view />
        <!-- Notification Container -->
        <NotificationContainer />
    </div>
</template>

<script>
import NotificationContainer from './components/NotificationContainer.vue';

export default {
    components: {
        NotificationContainer
    }
};
</script>