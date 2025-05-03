import { ref } from 'vue';

const notifications = ref([]);

export const useNotification = () => {
    const showNotification = (message, options = {}) => {
        const {
            type = 'info',
            duration = 3000,
            description = null,
            persistent = false
        } = options;

        const id = Date.now();
        notifications.value.push({
            id,
            message,
            type,
            duration: persistent ? 0 : duration,
            description
        });

        if (!persistent) {
            setTimeout(() => {
                removeNotification(id);
            }, duration);
        }

        return id;
    };

    const removeNotification = (id) => {
        notifications.value = notifications.value.filter(n => n.id !== id);
    };

    const updateNotification = (id, updates) => {
        const index = notifications.value.findIndex(n => n.id === id);
        if (index !== -1) {
            notifications.value[index] = {
                ...notifications.value[index],
                ...updates
            };
        }
    };

    const clearAllNotifications = () => {
        notifications.value = [];
    };

    return {
        notifications,
        showNotification,
        removeNotification,
        updateNotification,
        clearAllNotifications
    };
}; 