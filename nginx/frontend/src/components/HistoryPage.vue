<template>
    <div style="display: contents">
        <div
            class="flex flex-grow items-center justify-center relative z-20 bg-[url('/src/images/history_wallpaper.png')] bg-cover bg-center">
            <div class="flex flex-grow items-center justify-center relative z-20">
                <div class="w-full max-w-4xl p-6 md:p-8 bg-[#111111]/80 rounded-xl shadow-xl">
                    <h2 class="text-2xl font-semibold text-[#8FC773] mb-4 text-center">Transaction history</h2>
                    <p class="text-sm text-white mb-4 text-center">Transaction history for the last 30 days</p>
                    <p class="text-sm text-white mb-4 text-center">
                        Your wallet address:
                        <span class="font-mono text-[#8FC773] flex items-center justify-center">
                            {{ wallet_address }}
                            <button
                                @click.stop="copyHash(wallet_address, 1)"
                                class="ml-1 text-gray-400 hover:text-white transition-colors"
                                :title="isCopiedAddress ? 'Copied!' : 'Copy'">
                                <svg v-if="!isCopiedAddress" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500"
                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                            </button>
                        </span>
                    </p>
                    <div class="bg-[#131313]/85 rounded-xl shadow-sm p-6">
                        <!-- Table headers -->
                        <div class="grid grid-cols-12 gap-4 text-white font-medium pb-2 border-b border-[#333]">
                            <div class="col-span-2 text-left">From</div>
                            <div class="col-span-2 text-left">To</div>
                            <div class="col-span-2 text-right">Amount</div>
                            <div class="col-span-2 text-right">Type</div>
                            <div class="col-span-2 text-right">Status</div>
                            <div class="col-span-2 text-right">Date</div>
                        </div>
                        <!-- Scrollable list -->
                        <ul class="max-h-96 overflow-y-auto text-white">
                            <li v-for="(transaction, index) in transactions" :key="index"
                                class="grid grid-cols-12 gap-4 p-3 border-b border-[#222] last:border-0 hover:bg-[#222]/50 cursor-pointer transition-colors"
                                @click="openTransactionDetails(transaction)">
                                <div class="col-span-2 text-left font-mono text-sm truncate">
                                    {{ transaction.sender_address === wallet_address ? 'You' : shortenAddress(transaction.sender_address) }}
                                </div>
                                <div class="col-span-2 text-left font-mono text-sm truncate">
                                    {{ transaction.receiver_address === wallet_address ? 'You' : shortenAddress(transaction.receiver_address) }}
                                </div>
                                <div class="col-span-2 text-right font-mono text-[#8FC773]">{{ transaction.amount }} VND
                                </div>
                                <div class="col-span-2 text-right text-sm text-white">{{ transaction.type }}</div>
                                <div class="col-span-2 text-right text-sm text-white">
                                    <span :class="getStatusClass(transaction.status)">{{ transaction.status }}</span>
                                </div>
                                <div class="col-span-2 text-right text-sm text-white">{{ formatDate(transaction.timestamp)
                                }}</div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Transaction Details Modal -->
        <div v-if="selectedTransaction" class="fixed inset-0 bg-black/70 flex items-center justify-center z-30">
            <div class="bg-[#111111] rounded-xl shadow-xl max-w-2xl w-full p-6 border border-[#333]">
                <div class="flex justify-between items-center mb-4">
                    <h3 class="text-xl font-semibold text-[#8FC773]">Transaction details</h3>
                    <button @click="selectedTransaction = null;resetCopy()" class="text-white hover:text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <div class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <!-- From Address -->
                        <div>
                            <p class="text-sm text-white">From</p>
                            <div class="flex items-center gap-2">
                                <p class="font-mono break-all text-[#8FC773]">
                                    {{ selectedTransaction.sender_address === wallet_address ? 'You' : selectedTransaction.sender_address }}
                                </p>
                                <button v-if="selectedTransaction.sender_address !== wallet_address"
                                    @click.stop="copyHash(selectedTransaction.sender_address, 2)"
                                    class="ml-1 text-gray-400 hover:text-white transition-colors"
                                    :title="isCopiedFrom ? 'Copied!' : 'Copy'">
                                    <svg v-if="!isCopiedFrom" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                    </svg>
                                    <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M5 13l4 4L19 7" />
                                    </svg>
                                </button>
                            </div>
                        </div>

                        <!-- To Address -->
                        <div>
                            <p class="text-sm text-white">To</p>
                            <div class="flex items-center gap-2">
                                <p class="font-mono break-all text-[#8FC773]">
                                    {{ selectedTransaction.receiver_address === wallet_address ? 'You' : selectedTransaction.receiver_address }}
                                </p>
                                <button v-if="selectedTransaction.receiver_address !== wallet_address"
                                    @click.stop="copyHash(selectedTransaction.receiver_address, 3)"
                                    class="ml-1 text-gray-400 hover:text-white transition-colors"
                                    :title="isCopiedTo ? 'Copied!' : 'Copy'">
                                    <svg v-if="!isCopiedTo" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                    </svg>
                                    <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M5 13l4 4L19 7" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <p class="text-sm text-white">Amount</p>
                            <p class="text-[#8FC773] font-mono">{{ selectedTransaction.amount }} VND</p>
                        </div>
                        <div>
                            <p class="text-sm text-white">Type</p>
                            <p class="text-[#8FC773]">{{ selectedTransaction.type }}</p>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <p class="text-sm text-white">Status</p>
                            <p class="text-[#8FC773]">
                                <span :class="getStatusClass(selectedTransaction.status)">{{ selectedTransaction.status }}</span>
                            </p>
                        </div>
                        <div>
                            <p class="text-sm text-white">Date</p>
                            <p class="text-[#8FC773]">{{ formatDateLong(selectedTransaction.timestamp) }}</p>
                        </div>
                    </div>

                    <div v-if="selectedTransaction.message" class="pt-4">
                        <p class="text-sm text-white">Message</p>
                        <p class="text-[#8FC773] break-all">{{ selectedTransaction.message }}</p>
                    </div>

                    <div v-if="selectedTransaction.transaction_hash" class="pt-4 border-t border-[#333]">
                        <p class="text-sm text-white">Transaction hash</p>
                        <p class="font-mono break-all text-[#8FC773] flex items-center">
                            {{ selectedTransaction.transaction_hash }}
                            <button @click.stop="copyHash(selectedTransaction.transaction_hash, 4)"
                                class="ml-1 text-gray-400 hover:text-white transition-colors"
                                :title="isCopiedHash ? 'Copied!' : 'Copy'">
                                <svg v-if="!isCopiedHash" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500"
                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                            </button>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            isCopiedAddress: false,
            isCopiedFrom: false,
            isCopiedTo: false,
            isCopiedHash: false,
            copyTimeout: null,
            wallet_address: null,
            selectedTransaction: null,
            transactions: []
        }
    },
    methods: {
        openTransactionDetails(transaction) {
            this.selectedTransaction = transaction;
        },
        shortenAddress(address) {
            if (address === this.wallet_address) return 'You';
            return `${address.substring(0, 6)}...${address.substring(address.length - 6)}`;
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        },
        formatDateLong(dateString) {
            const date = new Date(dateString);
            return date.toLocaleString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                timeZoneName: 'short'
            });
        },
        copyHash(text, type) {
            navigator.clipboard.writeText(text).then(() => {
                // Clear any existing timeout
                if (this.copyTimeout) clearTimeout(this.copyTimeout);

                // Show checkmark
                switch (type) {
                    case 1:
                        this.isCopiedAddress = true;
                        this.copyTimeout = setTimeout(() => {
                            this.isCopiedAddress = false;
                        }, 3000);
                        break;
                    case 2:
                        this.isCopiedFrom = true;
                        this.copyTimeout = setTimeout(() => {
                            this.isCopiedFrom = false;
                        }, 3000);
                        break;
                    case 3:
                        this.isCopiedTo = true;
                        this.copyTimeout = setTimeout(() => {
                            this.isCopiedTo = false;
                        }, 3000);
                        break;
                    case 4:
                        this.isCopiedHash = true;
                        this.copyTimeout = setTimeout(() => {
                            this.isCopiedHash = false;
                        }, 3000);
                        break;
                }
            }).catch(err => {
                console.error('Failed to copy:', err);
            });
        },
        resetCopy() {
            this.isCopiedAddress = false;
            this.isCopiedFrom = false;
            this.isCopiedTo = false;
            this.isCopiedHash = false;
        },
        getTransactions() {
            fetch('/api/transaction/history', {
                method: 'GET',
                credentials: 'include'
            }).then((res) => {
                return res.json();
            }).then((data) => {
                this.transactions = data.history;
            }).catch((err) => {
                console.error('Error fetching transaction history:', err);
            })
        },
        getWalletAddress() {
            fetch('/api/profile/fetch/me', {
                method: 'GET',
                credentials: 'include'
            }).then((data) => {
                if (data.status === 401) {
                    this.$router.push('/auth#login');
                    return;
                } else if (data.status === 404) {
                    this.$router.push('/profile');
                    return;
                }
                return data.json();
            }).then((data) => {
                this.wallet_address = data.profile.wallet_address;
            }).catch((err) => {
                console.error('Error fetching wallet address:', err);
            })
        },
        getStatusClass(status) {
            // Implement your logic to determine the status class based on the status
            // For example, you can use a switch statement or a mapping function
            switch (status) {
                case 'completed':
                    return 'text-green-500';
                case 'pending':
                    return 'text-yellow-500';
                case 'failed':
                    return 'text-red-500';
                default:
                    return 'text-gray-500';
            }
        }
    },
    mounted() {
        this.getWalletAddress();
        this.getTransactions();
    }
}
</script>