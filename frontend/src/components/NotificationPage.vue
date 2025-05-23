<template>
  <div class="min-h-screen bg-[#111111] p-4 md:p-8">
    <div class="max-w-4xl mx-auto bg-[#111111]/80 rounded-xl shadow-xl p-6">
      <h1 class="text-2xl font-bold text-[#8FC773] mb-4 text-center">🔔 Notifications</h1>

      <div class="space-y-4">
        <div
            v-for="(noti, index) in sortedNotifications"
            :key="noti.id || index"
            :class="[
                'bg-[#131313] rounded-lg p-4 cursor-pointer shadow transition-all duration-300',
                noti.seen ? 'opacity-80 hover:opacity-100' : 'border border-[#8FC773] animate-pulse'
            ]"
            @click="markAsSeen(noti)"
        >
            <div class="flex justify-between items-center">
                <p class="text-white font-medium">{{ noti.message }}</p>
                <span class="text-xs text-[#8FC773]/80">{{ formatTimestamp(noti.timestamp) }}</span>
            </div>
        </div>

        <div v-if="notifications.length === 0" class="text-center text-gray-500 mt-10">
            <p>📭 No notifications.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'NotificationPage',
  data() {
    return {
      notifications: [
      ],
    };
  },
  computed: {
    sortedNotifications() {
        if (!this.notifications) return [];
        return [...this.notifications].sort((a, b) => {
            const dateA = new Date(a.timestamp.split(' foo')[0].replace(/(\d{2})-(\d{2})-(\d{4})/, '$2/$1/$3'));
            const dateB = new Date(b.timestamp.split(' foo')[0].replace(/(\d{2})-(\d{2})-(\d{4})/, '$2/$1/$3'));
            return dateB - dateA;
        });
    },
  },
  methods: {
    async fetchNotifications() {
        try {
            const response = await fetch('/api/notification/read', {
                        method: 'GET',
                        credentials: 'include'
                    }); 
            const data = await response.json();
            this.notifications.length = 0;
            this.notifications = data.map(n => ({
                id: n.id.toString(),
                message: n.message,
                timestamp: n.timestamp,
                seen: n.seen
                }));
        } catch (error) {
            console.error('Error fetching notifications:', error);
        }
    },
    formatTimestamp(raw) {
        return raw?.split(' foo')[0] || '';
    },
    async markAsSeen(notification) {
        if (notification.seen) return;
        notification.seen = true;
        try {
            const result = await fetch(`/api/notification/mark/${notification.id}`, {
                method: 'GET',
                credentials: 'include'
            });
            if (!result.ok) {
                throw new Error('Failed to mark notification as seen');
            }
            else
            {
                await this.fetchNotifications();
            }
        } catch (error) {
            console.error('Error updating notification:', error);
            notification.seen = false;
        }
    },
  },
  mounted() {
        fetch('/api/notification/add', {
                    method: 'POST',
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        message: 'You bought AWP | Dragon Lore'
                    })
                });
        this.fetchNotifications();
  },
};
</script>

<style scoped>
@keyframes pulse {
    0% {
        transform: scale(1);
        box-shadow: 0 0 8px #8FC77388;
    }
    100% {
        transform: scale(1.02);
        box-shadow: 0 0 16px #8FC773cc;
    }
}

.animate-pulse {
    animation: pulse 1s ease-in-out infinite alternate;
}
</style>
