<template>
    <div v-if="show" class="fixed top-20 right-4 z-[100]">
        <div :class="[
            'p-4 rounded-lg shadow-lg max-w-sm transition-all duration-300 transform',
            type === 'success' ? 'bg-green-500' : 
            type === 'error' ? 'bg-red-500' :
            type === 'info' ? 'bg-blue-500' :
            type === 'warning' ? 'bg-yellow-500' : 'bg-gray-500'
        ]">
            <div class="flex items-center">
                <div class="flex-shrink-0">
                    <svg v-if="type === 'success'" class="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <svg v-else-if="type === 'error'" class="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                    <svg v-else-if="type === 'info'" class="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                    <svg v-else-if="type === 'warning'" class="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                    </svg>
                </div>
                <div class="ml-3">
                    <p class="text-sm font-medium text-white">{{ message }}</p>
                    <p v-if="description" class="text-xs text-white/80 mt-1">{{ description }}</p>
                </div>
                <div class="ml-auto pl-3">
                    <div class="-mx-1.5 -my-1.5">
                        <button @click="close" class="inline-flex rounded-md p-1.5 text-white hover:bg-white/10 focus:outline-none">
                            <span class="sr-only">Dismiss</span>
                            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Notification',
    props: {
        message: {
            type: String,
            required: true
        },
        description: {
            type: String,
            default: null
        },
        type: {
            type: String,
            default: 'info',
            validator: value => ['success', 'error', 'info', 'warning'].includes(value)
        },
        duration: {
            type: Number,
            default: 3000
        }
    },
    data() {
        return {
            show: true
        }
    },
    mounted() {
        if (this.duration > 0) {
            setTimeout(() => {
                this.close();
            }, this.duration);
        }
    },
    methods: {
        close() {
            this.show = false;
            this.$emit('close');
        }
    }
}
</script> 