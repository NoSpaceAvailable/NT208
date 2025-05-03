<template>
    <div style="display: contents">
        <!-- Add money step -->
        <div
            class="flex flex-grow items-center justify-center relative z-20 bg-[url('/src/images/pay_wallpaper.png')] bg-cover bg-center">
            <div class="w-full max-w-xl p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-xl">
                <h2 class="text-2xl font-semibold text-[#8FC773] mb-4 text-center">Add money to wallet</h2>
                <p class="text-sm text-white mb-4 text-center">
                    Your wallet address: <span class="font-mono text-[#8FC773]">{{ wallet_address }}</span>
                </p>
                <p class="text-sm text-white mb-4 text-center">
                    Your current balance: <span class="font-mono text-[#8FC773]">{{ wallet_balance }}</span>
                </p>
                <form @submit.prevent="addMoney" class="space-y-4">
                    <div>
                        <label class="text-sm text-[#8FC773]">Amount to add:</label>
                        <input v-model="amount" type="number" min="1" step="1"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <button type="submit"
                        class="w-full py-2 bg-[#8FC773] text-black font-semibold rounded-lg hover:bg-[#7BBF5A]">
                        Proceed to payment
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AddMoneyPage',
    data() {
        return {
            wallet_address: null,
            wallet_balance: -1,
            amount: null
        }
    },
    methods: {
        getWalletBalance() {
            fetch('/api/transaction/balance', {
                method: 'GET',
                credentials: 'include'
            }).then((resp) => {
                return resp.json()
            }).then((data) => {
                this.wallet_balance = data.balance || '(failed to fetch data)';
            }).catch((error) => {
                console.error('Error fetching wallet balance!')
            })
        },
        async fetchProfile() {
            try {
                const response = await fetch('/api/profile/fetch', {
                    method: 'GET',
                    credentials: 'include'
                });

                if (response.status === 401) {
                    this.$router.push('/auth#login');
                    return;
                } else if (response.status === 404) {
                    this.$router.push('/profile');
                    return;
                }

                if (response.ok) {
                    const data = await response.json();
                    if (data) {
                        const profile = data.profile;
                        this.wallet_address = profile.wallet_address;
                    }
                }
            } catch (err) {
                console.error('Error fetching profile:', err);
            }
        },
        addMoney() {
            if (!this.amount || this.amount <= 0) {
                alert('Please enter a valid amount!');
                return;
            }

            fetch('/api/transaction/add', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    address: this.wallet_address,
                    amount: this.amount
                })
            }).then((resp) => {
                if (resp.ok) {
                    return resp.json();
                } else {
                    throw new Error('Failed to create payment');
                }
            }).then((data) => {
                if (data.status === 'ok' && data.pay_url) {
                    // Open payment URL in new window
                    window.open(data.pay_url, '_blank');
                } else {
                    alert('Failed to create payment link');
                }
            }).catch((error) => {
                console.error('Error creating payment:', error);
                alert('Failed to create payment');
            })
        }
    },
    mounted() {
        this.fetchProfile();
        this.getWalletBalance()
    },
}
</script>