<template>
    <div style="display: contents">
        <!-- Payment step -->
        <div class="flex flex-grow items-center justify-center relative z-20 bg-[url('/src/images/pay_wallpaper.png')] bg-cover bg-center">
            <div class="w-full max-w-xl p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-xl">
                <h2 class="text-2xl font-semibold text-[#8FC773] mb-4 text-center">Transfer money</h2>
                <p class="text-sm text-white mb-4 text-center">
                    Your wallet address: <span class="font-mono text-[#8FC773]">{{ wallet_address }}</span>
                </p>
                <p class="text-sm text-white mb-4 text-center">
                    Your wallet balance: <span class="font-mono text-[#8FC773]">{{ wallet_balance }}</span>
                </p>
                <form @submit.prevent="pay" class="space-y-4">
                    <div>
                        <label class="text-sm text-[#8FC773]">Transfer an amount of:</label>
                        <input v-model="transaction_template.amount" type="number" min="0"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <div>
                        <label class="text-sm text-[#8FC773]">To the address:</label>
                        <input v-model="transaction_template.to" type="text" placeholder="Wallet address"
                            class="w-full p-2 bg-[#131313] rounded-lg border border-gray-600 text-white" required>
                    </div>
                    <button type="submit"
                        class="w-full py-2 bg-[#8FC773] text-black font-semibold rounded-lg hover:bg-[#7BBF5A]">
                        Transfer
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PaymentPage',
    data() {
        return {
            wallet_address: null,
            wallet_balance: -1,
            transaction_template: {
                'to': null,
                'amount': null
            }
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
        pay() {
            if (!this.transaction_template.to || !this.transaction_template.amount) {
                alert('Please fill in all fields!');
                return;
            }

            if (this.wallet_balance < this.transaction_template.amount) {
                alert('You don\'t have enough money in your wallet!');
                return;
            } else {
                fetch('/api/transaction/pay', {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.transaction_template)
                }).then((resp) => {
                    if (resp.ok) {
                        alert('Payment successful!');
                        this.getWalletBalance();
                    } else {
                        alert('Payment failed!');
                    }
                }).catch((error) => {
                    console.error('Error processing payment:', error);
                    alert('Payment failed!');
                })
            }
        }
    },
    mounted() {
        this.fetchProfile();
        this.getWalletBalance()
    },
}
</script>