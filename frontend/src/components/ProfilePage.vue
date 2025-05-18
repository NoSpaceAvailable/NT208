<template>
    <div class="min-h-screen p-4 md:p-8 bg-[url('/src/images/profile_wallpaper.png')] bg-cover bg-center">
        <!-- Wallet Creation Step -->
        <div v-if="!wallet_address" class="flex flex-grow items-center justify-center relative z-20">
            <div class="w-full max-w-xl p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-xl text-center">
                <h2 class="text-2xl font-semibold text-[#8FC773] mb-4">Create your wallet</h2>
                <p class="text-sm text-white mb-6">You need a wallet address before creating your profile</p>
                <button @click="createWallet"
                    class="w-full py-2 bg-[#8FC773] text-black font-semibold rounded-lg hover:bg-[#7BBF5A] transition-colors">
                    Create wallet
                </button>
                <p v-if="wallet_error" class="text-red-400 mt-4">{{ wallet_error }}</p>
            </div>
        </div>

        <!-- Profile Creation Step -->
        <div v-else-if="!profile" class="flex flex-grow items-center justify-center relative z-20">
            <div class="w-full max-w-xl p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-xl">
                <h2 class="text-2xl font-semibold text-[#8FC773] mb-4 text-center">Create Your Profile</h2>
                <p class="text-sm text-white mb-4 text-center">Fill in the details below to create your profile</p>
                <p class="text-sm text-white mb-4 text-center">
                    Your wallet address: <span class="font-mono text-[#8FC773]">{{ wallet_address }}</span>
                </p>
                <form @submit.prevent="createProfile" class="space-y-4">
                    <div>
                        <label class="text-sm text-[#8FC773]">Profile name (will be displayed on your profile)</label>
                        <input v-model="newProfile.profile_name"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">Fullname</label>
                        <input v-model="newProfile.full_name"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">Bio (optional)</label>
                        <textarea v-model="newProfile.bio"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white"></textarea>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">Country</label>
                        <input v-model="newProfile.country"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">Province or city</label>
                        <input v-model="newProfile.city"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">Date of Birth</label>
                        <input v-model="newProfile.birthdate" type="date"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <button type="submit"
                        class="w-full py-2 bg-[#8FC773] text-black font-semibold rounded-lg hover:bg-[#7BBF5A]">
                        Create profile
                    </button>
                </form>
            </div>
        </div>

        <!-- Profile Content -->
        <div v-else class="relative max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row gap-6">
                <!-- Left Column -->
                <div class="flex-1 space-y-6">
                    <!-- Basic Info Card -->
                    <div class="bg-[#131313] rounded-xl shadow-sm p-6">
                        <h2 class="text-xl font-semibold text-[#8FC773] mb-4">Basic Information</h2>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <p class="text-sm text-white">Username</p>
                                <p class="font-medium text-[#8FC773]">{{ profile.profile_name }}</p>
                            </div>
                            <div>
                                <p class="text-sm text-white">Fullname</p>
                                <p class="font-medium text-[#8FC773]">{{ profile.full_name }}</p>
                            </div>
                            <div>
                                <p class="text-sm text-white">Date of Birth</p>
                                <p class="font-medium text-[#8FC773]">{{ profile.birthdate }}</p>
                            </div>
                            <div>
                                <p class="text-sm text-white">Location</p>
                                <p class="font-medium text-[#8FC773]">{{ profile.location }}</p>
                            </div>
                            <div class="col-span-2">
                                <p class="text-sm text-white">Bio</p>
                                <p class="font-medium text-[#8FC773]">
                                    {{ profile.bio ? profile.bio : '(none)' }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Wallet/Account Card -->
                    <div class="bg-[#131313] rounded-xl shadow-sm p-6">
                        <h2 class="text-xl font-semibold text-[#8FC773] mb-4">Account Details</h2>
                        <div class="space-y-4">
                            <div>
                                <p class="text-sm text-white">Wallet address</p>
                                <p class="font-mono font-medium text-[#8FC773] break-all">
                                    {{ profile.wallet_address }}
                                </p>
                            </div>
                            <div>
                                <p class="text-sm text-white">Member since</p>
                                <p class="font-medium text-[#8FC773]">{{ profile.joined_at }}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="flex-1 space-y-6">
                    <!-- Inventory Card -->
                    <div class="bg-[#131313] rounded-xl shadow-sm p-6">
                        <div class="flex justify-between items-center mb-4">
                            <h2 class="text-xl font-semibold text-[#8FC773]">Pinned Items</h2>
                        </div>
                        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
                            <div v-for="i in 4" :key="i"
                                class="aspect-square bg-gray-800 rounded-lg flex items-center justify-center hover:scale-110 duration-300">
                                <span class="text-white">Item {{ i }}</span>
                            </div>
                            <div
                                class="aspect-square bg-gray-800 border-2 border-dashed border-gray-200 rounded-lg flex items-center justify-center hover:scale-110 duration-300">
                                <span class="text-white">+ Add</span>
                            </div>
                        </div>
                    </div>

                    <!-- Ratings Card -->
                    <div class="bg-[#131313] rounded-xl shadow-sm p-6">
                        <h2 class="text-xl font-semibold text-[#8FC773] mb-4">Seller Rating</h2>
                        <div class="flex items-center space-x-2 mb-3">
                            <div class="flex">
                                <span v-for="i in 5" :key="i" class="text-yellow-400">★</span>
                            </div>
                            <span class="font-medium text-[#8FC773]">4.8</span>
                            <span class="text-sm text-white">(128 reviews)</span>
                        </div>
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-white">5 stars</span>
                                <div class="w-3/4 h-2 bg-gray-200 rounded-full overflow-hidden">
                                    <div class="h-full bg-yellow-400" style="width: 85%"></div>
                                </div>
                                <span class="text-sm text-white">85%</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-white">4 stars</span>
                                <div class="w-3/4 h-2 bg-gray-200 rounded-full overflow-hidden">
                                    <div class="h-full bg-yellow-400" style="width: 10%"></div>
                                </div>
                                <span class="text-sm text-white">10%</span>
                            </div>
                            <div class="pt-3 border-t border-gray-100">
                                <p class="text-sm italic text-white">"Don't buy! I lost 2000$ for this fkin bastard !!!"
                                </p>
                                <p class="text-xs text-[#8FC773] mt-1">- Sarah M., 2 days ago</p>
                            </div>
                            <div class="pt-3">
                                <p class="text-sm italic text-white">"DON'T BELIEVE IN SARAH !! SHE IS CRAYZY AS F"</p>
                                <p class="text-xs text-[#8FC773] mt-1">- Alex (shop owner), 2 days ago</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useNotification } from '../services/notificationService';

export default {
    name: 'ProfilePage',
    setup() {
        const { showNotification } = useNotification();
        return { showNotification };
    },
    data() {
        return {
            wallet_address: null,
            wallet_error: null,
            profile: null,
            newProfile: {
                profile_name: '',
                full_name: '',
                bio: '',
                country: '',
                city: '',
                birthdate: ''
            }
        }
    },
    methods: {
        async createWallet() {
            try {
                this.wallet_error = null;
                const response = await fetch('/api/transaction/create-wallet', {
                    method: 'GET',
                    credentials: 'include'
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data.status === 'ok') {
                        this.wallet_address = data.address;
                    } else {
                        this.wallet_error = 'Failed to create wallet';
                        this.showNotification('Failed to create wallet', { type: 'error' });
                    }
                } else {
                    this.wallet_error = 'Failed to create wallet';
                    this.showNotification('Failed to create wallet', { type: 'error' });
                }
            } catch (err) {
                console.error('Error creating wallet:', err);
                this.wallet_error = 'An error occurred while creating wallet';
                this.showNotification('An error occurred while creating wallet', { type: 'error' });
            }
        },

        async fetchProfile() {
            try {
                const response = await fetch('/api/profile/fetch/me', {
                    method: 'GET',
                    credentials: 'include'
                });

                if (response.status === 401) {
                    this.$router.push('/auth#login');
                    return;
                }

                if (response.ok) {
                    const data = await response.json();
                    if (data) {
                        this.profile = data.profile;
                        this.wallet_address = this.profile.wallet_address;
                    }
                }
            } catch (err) {
                console.error('Error fetching profile:', err);
            }
        },

        async createProfile() {
            try {
                // Combine location fields
                const profileData = {
                    ...this.newProfile
                };

                const response = await fetch('/api/profile/create', {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(profileData)
                });

                if (response.ok) {
                    location.reload();
                } else {
                    this.showNotification('Failed to create profile', { 
                        type: 'error',
                        description: 'Try to change your profile name. If the problem persists, please contact the support.'
                    });
                }
            } catch (err) {
                console.error('Error creating profile:', err);
                this.showNotification('An error occurred while creating profile', { type: 'error' });
            }
        }
    },
    async mounted() {
        await this.fetchProfile();
    }
}
</script>