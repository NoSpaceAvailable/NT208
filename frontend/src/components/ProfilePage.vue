<template>
    <div style="display: contents;">
        <div v-if="getProfile() === false">
            
        </div>
        <div v-else>

        </div>
    </div>
</template>

<script>
    export default {
        name: 'ProfilePage',
        methods: {
            getProfile() {
                fetch('/api/')
                .then((response) => {
                    
                });
            }
        }
    }
</script>