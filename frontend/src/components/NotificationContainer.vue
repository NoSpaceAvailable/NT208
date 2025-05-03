<template>
    <div class="fixed top-20 right-4 z-[100] space-y-2">
        <Notification
            v-for="notification in notifications"
            :key="notification.id"
            :message="notification.message"
            :description="notification.description"
            :type="notification.type"
            :duration="notification.duration"
            @close="removeNotification(notification.id)"
        />
    </div>
</template>

<script>
import { useNotification } from '../services/notificationService';
import Notification from './Notification.vue';

export default {
    name: 'NotificationContainer',
    components: {
        Notification
    },
    setup() {
        const { notifications, removeNotification } = useNotification();
        return {
            notifications,
            removeNotification
        };
    }
};
</script> 