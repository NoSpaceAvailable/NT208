<template>
    <div class="min-h-screen p-4 md:p-8 bg-[#111111]">
        <div class="max-w-7xl mx-auto">
            <!-- Header Section -->
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
                <div>
                    <h1 class="text-2xl md:text-3xl font-bold text-[#8FC773]">Your CS:GO Inventory</h1>
                    <p class="text-white/80">Manage your skins, stickers, and other items</p>
                </div>
                <div class="mt-4 md:mt-0 flex space-x-3">
                    <button @click="showDepositModal = true"
                        class="px-4 py-2 bg-[#8FC773] text-black font-medium rounded-lg hover:bg-[#7BBF5A] transition-colors">
                        Deposit Items
                    </button>
                    <button @click="showWithdrawModal = true"
                        class="px-4 py-2 bg-transparent border border-[#8FC773] text-[#8FC773] font-medium rounded-lg hover:bg-[#8FC773]/10 transition-colors">
                        Withdraw Items
                    </button>
                </div>
            </div>

            <!-- Filters Section -->
            <div class="bg-[#131313] rounded-xl p-4 mb-6">
                <div class="flex flex-col md:flex-row md:items-center md:justify-between space-y-4 md:space-y-0">
                    <div class="flex items-center space-x-3">
                        <div class="relative">
                            <select v-model="filterType"
                                class="appearance-none bg-[#1A1A1A] text-white pl-3 pr-8 py-2 rounded-lg border border-gray-700 focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                                <option value="all">All Items</option>
                                <option value="weapon">Weapons</option>
                                <option value="knife">Knives</option>
                                <option value="gloves">Gloves</option>
                                <option value="sticker">Stickers</option>
                                <option value="case">Cases</option>
                            </select>
                            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                                </svg>
                            </div>
                        </div>
                        <div class="relative">
                            <select v-model="filterRarity"
                                class="appearance-none bg-[#1A1A1A] text-white pl-3 pr-8 py-2 rounded-lg border border-gray-700 focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                                <option value="all">All Rarities</option>
                                <option v-for="rarity in rarities" :key="rarity" :value="rarity"
                                    :style="{ color: rarityColors[rarity]['background'] }">
                                    {{ rarityNames[rarity] }}
                                </option>
                            </select>
                            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="relative w-full md:w-64">
                        <input v-model="searchQuery" type="text" placeholder="Search items..."
                            class="w-full bg-[#1A1A1A] text-white pl-3 pr-10 py-2 rounded-lg border border-gray-700 focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                        <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                            <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Stats Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div class="bg-[#131313] rounded-xl p-4">
                    <p class="text-sm text-white/80">Total Items</p>
                    <p class="text-2xl font-bold text-[#8FC773]">{{ filteredItems.length }}</p>
                </div>
                <div class="bg-[#131313] rounded-xl p-4">
                    <p class="text-sm text-white/80">Inventory Value</p>
                    <p class="text-2xl font-bold text-[#8FC773]">${{ inventoryValue.toFixed(2) }}</p>
                </div>
                <div class="bg-[#131313] rounded-xl p-4">
                    <p class="text-sm text-white/80">Most Valuable Item</p>
                    <p v-if="mostValuableItem" class="text-2xl font-bold text-[#8FC773]">
                        {{ mostValuableItem.name }} (${{ mostValuableItem.price.toFixed(2) }})
                    </p>
                    <p v-else class="text-2xl font-bold text-[#8FC773]">-</p>
                </div>
            </div>

            <!-- Inventory Grid -->
            <div v-if="filteredItems.length > 0" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
                <div v-for="item in filteredItems" :key="item.id"
                    class="bg-[#131313] rounded-xl overflow-hidden hover:shadow-lg hover:shadow-[#8FC773]/20 transition-all duration-300 group">
                    <div class="relative aspect-square bg-gradient-to-br from-[#1A1A1A] to-[#111111] flex items-center justify-center">
                        <img :src="getItemImage(item)" :alt="item.name" class="w-full h-full object-contain p-4">
                        <div class="absolute top-2 right-2 flex items-center space-x-1">
                            <span v-if="item.stattrak" class="bg-[#CF6A32] text-white text-xs px-1.5 py-0.5 rounded">ST</span>
                            <span :style="getRarityStyle(item.rarity)" class="text-xs px-1.5 py-0.5 rounded">
                                {{ getRarityName(item.rarity) }}
                            </span>
                        </div>
                        <div class="absolute bottom-2 left-2 right-2 flex justify-between items-center opacity-0 group-hover:opacity-100 transition-opacity">
                            <button @click="selectItem(item)" class="text-xs bg-[#8FC773] text-black px-2 py-1 rounded">
                                Details
                            </button>
                            <button @click="toggleSelectItem(item)"
                                :class="{'bg-[#8FC773] text-black': selectedItems.some(i => i.id === item.id), 'bg-white/10 text-white': !selectedItems.some(i => i.id === item.id)}"
                                class="text-xs px-2 py-1 rounded">
                                {{ selectedItems.some(i => i.id === item.id) ? 'Selected' : 'Select' }}
                            </button>
                        </div>
                    </div>
                    <div class="p-3">
                        <p class="text-sm font-medium text-white truncate">{{ item.name }}</p>
                        <div class="flex justify-between items-center mt-1">
                            <p class="text-xs text-[#8FC773]">${{ item.price.toFixed(2) }}</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Empty State -->
            <div v-else class="bg-[#131313] rounded-xl p-8 text-center">
                <div class="max-w-md mx-auto">
                    <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
                    </svg>
                    <h3 class="mt-2 text-lg font-medium text-white">No items found</h3>
                    <p class="mt-1 text-sm text-white/60">
                        Your inventory is empty or no items match your filters.
                    </p>
                    <div class="mt-6">
                        <button @click="showDepositModal = true"
                            class="inline-flex items-center px-4 py-2 bg-[#8FC773] text-black font-medium rounded-lg hover:bg-[#7BBF5A]">
                            <svg class="-ml-1 mr-2 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                            </svg>
                            Deposit Items
                        </button>
                    </div>
                </div>
            </div>

            <!-- Selected Items Actions -->
            <div v-if="selectedItems.length > 0" class="fixed bottom-4 left-0 right-0 flex justify-center">
                <div class="bg-[#131313] border border-[#8FC773]/50 rounded-xl shadow-xl p-4 flex items-center space-x-4">
                    <span class="text-sm text-white">{{ selectedItems.length }} item(s) selected</span>
                    <button @click="showSellModal = true"
                        class="px-4 py-2 bg-[#8FC773] text-black font-medium rounded-lg hover:bg-[#7BBF5A]">
                        Sell Selected
                    </button>
                    <button @click="showTradeUpModal = true"
                        class="px-4 py-2 bg-[#4A6FA5] text-white font-medium rounded-lg hover:bg-[#3D5B84]">
                        Trade Up
                    </button>
                    <button @click="selectedItems = []"
                        class="px-4 py-2 bg-transparent text-white font-medium rounded-lg hover:bg-white/10">
                        Clear
                    </button>
                </div>
            </div>

            <!-- Item Detail Modal -->
            <div v-if="selectedItem" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
                <div class="bg-[#131313] rounded-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
                    <div class="p-6">
                        <div class="flex justify-between items-start">
                            <h3 class="text-xl font-bold text-[#8FC773]">{{ selectedItem.name }}</h3>
                            <button @click="selectedItem = null" class="text-white/70 hover:text-white">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>

                        <div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="bg-gradient-to-br from-[#1A1A1A] to-[#111111] rounded-lg p-6 flex items-center justify-center">
                                <img :src="getItemImage(selectedItem)" :alt="selectedItem.name" class="max-h-64 object-contain">
                            </div>

                            <div class="space-y-4">
                                <div>
                                    <p class="text-sm text-white/80">Type</p>
                                    <p class="text-white capitalize">{{ selectedItem.type }}</p>
                                </div>
                                <div>
                                    <p class="text-sm text-white/80">Rarity</p>
                                    <p :style="getRarityStyle(selectedItem.rarity)" class="inline-block px-2 py-1 rounded text-sm">
                                        {{ getRarityName(selectedItem.rarity) }}
                                    </p>
                                </div>
                                <div>
                                    <p class="text-sm text-white/80">Exterior</p>
                                    <p class="text-white">{{ selectedItem.exterior || '-' }}</p>
                                </div>
                                <div>
                                    <p class="text-sm text-white/80">Current Price</p>
                                    <p class="text-[#8FC773] font-bold">${{ selectedItem.price.toFixed(2) }}</p>
                                </div>
                                <div v-if="selectedItem.collection">
                                    <p class="text-sm text-white/80">Collection</p>
                                    <p class="text-white">{{ selectedItem.collection }}</p>
                                </div>
                                <div v-if="selectedItem.stattrak">
                                    <p class="text-sm text-white/80">StatTrak™</p>
                                    <p class="text-[#CF6A32]"><strong>Yes</strong></p>
                                </div>
                                <div v-if="selectedItem.for_sale">
                                    <p class="text-sm text-[#8FC773]"><strong>This item is for sale</strong></p>
                                </div>
                            </div>
                        </div>

                        <div class="mt-6 pt-6 border-t border-gray-700 flex space-x-3">
                            <button @click="toggleSelectItem(selectedItem)"
                                :class="{'bg-[#8FC773] text-black': selectedItems.some(i => i.id === selectedItem.id), 'bg-white/10 text-white': !selectedItems.some(i => i.id === selectedItem.id)}"
                                class="flex-1 py-2 rounded-lg font-medium">
                                {{ selectedItems.some(i => i.id === selectedItem.id) ? 'Remove from Selection' : 'Add to Selection' }}
                            </button>
                            <button @click="showSellModal = true; selectedItemToSell = selectedItem; selectedItem = null"
                                class="flex-1 py-2 bg-[#8FC773] text-black rounded-lg font-medium hover:bg-[#7BBF5A]">
                                Sell Item
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Deposit Modal -->
            <div v-if="showDepositModal" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
                <div class="bg-[#131313] rounded-xl max-w-md w-full">
                    <div class="p-6">
                        <div class="flex justify-between items-start">
                            <h3 class="text-xl font-bold text-[#8FC773]">Deposit CS:GO Items</h3>
                            <button @click="showDepositModal = false" class="text-white/70 hover:text-white">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>
                        <div class="mt-6 space-y-4">
                           <div>
                                <p class="text-sm text-white/80 mb-2">1. Open CS:GO and go to your inventory</p>
                                <p class="text-sm text-white/80 mb-2">2. Click on "Trade Offers" in the main menu</p>
                                <p class="text-sm text-white/80 mb-2">3. Find our bot in your friends list or enter our trade URL:</p>
                                <div class="bg-[#1A1A1A] p-3 rounded-lg mt-2">
                                    <p class="text-xs text-white break-all">https://steamcommunity.com/tradeoffer/new/?partner=123456789&token=abcdefg</p>
                                    <button @click="copyTradeUrl" class="mt-2 text-xs text-[#8FC773] hover:underline">
                                        Copy Trade URL
                                    </button>
                                </div>
                                <p class="text-sm text-white/80 mt-4">4. Select the items you want to deposit and send the trade offer</p>
                            </div>

                            <div class="pt-4 border-t border-gray-700">
                                <button @click="showDepositModal = false"
                                    class="w-full py-2 bg-[#8FC773] text-black rounded-lg font-medium hover:bg-[#7BBF5A]">
                                    I've Sent the Trade Offer
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Withdraw Modal -->
            <div v-if="showWithdrawModal" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
                <div class="bg-[#131313] rounded-xl max-w-md w-full">
                    <div class="p-6">
                        <div class="flex justify-between items-start">
                            <h3 class="text-xl font-bold text-[#8FC773]">Withdraw CS:GO Items</h3>
                            <button @click="showWithdrawModal = false" class="text-white/70 hover:text-white">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>
                        <div class="mt-6 space-y-4">
                            <div>
                                <label class="block text-sm text-white/80 mb-1">Steam Trade URL</label>
                                <input v-model="withdrawTradeUrl" type="text" placeholder="https://steamcommunity.com/tradeoffer/new/?partner=..."
                                    class="w-full bg-[#1A1A1A] text-white px-3 py-2 rounded-lg border border-gray-700 focus:outline-none focus:ring-1 focus:ring-[#8FC773]">
                            </div>

                            <div v-if="selectedItems.length > 0">
                                <p class="text-sm text-white/80 mb-2">Selected Items ({{ selectedItems.length }})</p>
                                <div class="bg-[#1A1A1A] rounded-lg p-3 max-h-40 overflow-y-auto">
                                    <div v-for="item in selectedItems" :key="item.id" class="flex items-center justify-between py-1">
                                        <p class="text-xs text-white truncate">{{ item.name }}</p>
                                        <p class="text-xs text-[#8FC773]">${{ item.price.toFixed(2) }}</p>
                                    </div>
                                </div>
                            </div>
                            <div v-else>
                                <p class="text-sm text-white/80">No items selected for withdrawal</p>
                            </div>

                            <div class="pt-4 border-t border-gray-700 flex space-x-3">
                                <button @click="showWithdrawModal = false"
                                    class="flex-1 py-2 bg-transparent border border-gray-600 text-white rounded-lg font-medium hover:bg-white/10">
                                    Cancel
                                </button>
                                <button @click="confirmWithdraw" :disabled="selectedItems.length === 0 || !withdrawTradeUrl"
                                    :class="{'bg-[#8FC773] hover:bg-[#7BBF5A] text-black': selectedItems.length > 0 && withdrawTradeUrl, 'bg-gray-600 text-white/50 cursor-not-allowed': selectedItems.length === 0 || !withdrawTradeUrl}"
                                    class="flex-1 py-2 rounded-lg font-medium">
                                    Confirm Withdrawal
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sell Modal -->
            <div v-if="showSellModal" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
                <div class="bg-[#131313] rounded-xl max-w-md w-full">
                    <div class="p-6">
                        <div class="flex justify-between items-start">
                            <h3 class="text-xl font-bold text-[#8FC773]">Sell Items</h3>
                            <button @click="closeSellModal" class="text-white/70 hover:text-white">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>
                        <div class="mt-6 space-y-4">
                            <div v-if="itemsToDisplayInSellModal.length > 0">
                                <p class="text-sm text-white/80 mb-2">
                                    {{ itemsToDisplayInSellModal.length > 1 ? `Selected Items (${itemsToDisplayInSellModal.length})` : 'Item to Sell' }}
                                </p>
                                <div class="bg-[#1A1A1A] rounded-lg p-3 max-h-40 overflow-y-auto">
                                    <div v-for="item in itemsToDisplayInSellModal" :key="item.id" class="flex items-center justify-between py-1">
                                        <p class="text-xs text-white truncate">{{ item.name }}</p>
                                        <p class="text-xs text-[#8FC773]">${{ item.price.toFixed(2) }}</p>
                                    </div>
                                </div>
                                <div class="mt-3 flex items-center justify-between">
                                    <p class="text-sm text-white/80">Total Value</p>
                                    <p class="text-lg font-bold text-[#8FC773]">${{ totalSellValue.toFixed(2) }}</p>
                                </div>
                            </div>
                            <div v-else>
                                <p class="text-sm text-white/80">No items selected for sale</p>
                            </div>

                            <div class="pt-4 border-t border-gray-700 flex space-x-3">
                                <button @click="closeSellModal"
                                    class="flex-1 py-2 bg-transparent border border-gray-600 text-white rounded-lg font-medium hover:bg-white/10">
                                    Cancel
                                </button>
                                <button @click="confirmSell" :disabled="itemsToDisplayInSellModal.length === 0"
                                    :class="{'bg-[#8FC773] hover:bg-[#7BBF5A] text-black': itemsToDisplayInSellModal.length > 0, 'bg-gray-600 text-white/50 cursor-not-allowed': itemsToDisplayInSellModal.length === 0}"
                                    class="flex-1 py-2 rounded-lg font-medium">
                                    Confirm Sale
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Trade Up Modal -->
            <div v-if="showTradeUpModal" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4">
                <div class="bg-[#131313] rounded-xl max-w-md w-full">
                    <div class="p-6">
                        <div class="flex justify-between items-start">
                            <h3 class="text-xl font-bold text-[#8FC773]">Trade Up Contract</h3>
                            <button @click="showTradeUpModal = false" class="text-white/70 hover:text-white">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>
                        <div class="mt-6 space-y-4">
                           <div>
                                <p class="text-sm text-white/80 mb-2">Selected Items ({{ selectedItems.length }}/10)</p>
                                <div class="bg-[#1A1A1A] rounded-lg p-3 max-h-40 overflow-y-auto">
                                    <div v-if="selectedItems.length > 0">
                                        <div v-for="item in selectedItems" :key="item.id" class="flex items-center justify-between py-1">
                                            <p class="text-xs text-white truncate">{{ item.name }}</p>
                                            <p class="text-xs text-[#8FC773]">${{ item.price.toFixed(2) }}</p>
                                        </div>
                                    </div>
                                    <div v-else class="text-center py-4">
                                        <p class="text-sm text-white/60">No items selected</p>
                                    </div>
                                </div>
                                <div class="mt-3 flex items-center justify-between">
                                    <p class="text-sm text-white/80">Total Value</p>
                                    <p class="text-lg font-bold text-[#8FC773]">${{ totalSelectedValue.toFixed(2) }}</p>
                                </div>
                            </div>

                            <div>
                                <p class="text-sm text-white/80 mb-2">Potential Outcome</p>
                                <div class="bg-[#1A1A1A] rounded-lg p-3">
                                    <div v-if="selectedItems.length >= 10" class="text-center py-2">
                                        <p class="text-sm text-[#8FC773]">You could receive an item worth up to:</p>
                                        <p class="text-xl font-bold text-[#8FC773] mt-1">${{ (totalSelectedValue * 1.5).toFixed(2) }}</p>
                                        <p class="text-xs text-white/60 mt-1">(Based on similar trade up contracts)</p>
                                    </div>
                                    <div v-else class="text-center py-4">
                                        <p class="text-sm text-white/60">Select 10 items to see potential outcome</p>
                                    </div>
                                </div>
                            </div>

                            <div class="pt-4 border-t border-gray-700 flex space-x-3">
                                <button @click="showTradeUpModal = false"
                                    class="flex-1 py-2 bg-transparent border border-gray-600 text-white rounded-lg font-medium hover:bg-white/10">
                                    Cancel
                                </button>
                                <button @click="confirmTradeUp" :disabled="selectedItems.length < 10"
                                    :class="{'bg-[#4A6FA5] hover:bg-[#3D5B84] text-white': selectedItems.length >= 10, 'bg-gray-600 text-white/50 cursor-not-allowed': selectedItems.length < 10}"
                                    class="flex-1 py-2 rounded-lg font-medium">
                                    Execute Trade Up
                                </button>
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
    name: 'InventoryPage',
    setup() {
        const { showNotification } = useNotification();
        return { showNotification };
    },
    data() {
        return {
            items: [],
            selectedItems: [],
            selectedItem: null,
            selectedItemToSell: null,
            filterType: 'all',
            filterRarity: 'all',
            searchQuery: '',
            showDepositModal: false,
            showWithdrawModal: false,
            showSellModal: false,
            showTradeUpModal: false,
            withdrawTradeUrl: '',
            isLoading: false,
            rarities: [ '1', '2', '3', '4', '5' ],
            rarityColors: {
                '1': { background: '#4B69FF', text: '#FFFFFF' }, // Industrial
                '2': { background: '#8847FF', text: '#FFFFFF' }, // Mil-Spec
                '3': { background: '#D32CE6', text: '#FFFFFF' }, // Restricted
                '4': { background: '#EB4B4B', text: '#FFFFFF' }, // Classified
                '5': { background: '#FFD700', text: '#000000' }, // Covert
            },
            rarityNames: {
                '1': 'Industrial',
                '2': 'Mil-Spec',
                '3': 'Restricted',
                '4': 'Classified',
                '5': 'Covert'
            }
        }
    },
    computed: {
        filteredItems() {
            let filtered = this.items;

            if (this.filterType !== 'all') {
                filtered = filtered.filter(item => item.type === this.filterType);
            }

            if (this.filterRarity !== 'all') {
                filtered = filtered.filter(item => item.rarity === this.filterRarity);
            }

            if (this.searchQuery) {
                const query = this.searchQuery.toLowerCase();
                filtered = filtered.filter(item =>
                    item.name.toLowerCase().includes(query) ||
                    (item.collection && item.collection.toLowerCase().includes(query))
                );
            }

            return filtered;
        },
        inventoryValue() {
            return this.items.reduce((total, item) => total + item.price, 0);
        },
        mostValuableItem() {
            if (this.items.length === 0) return null;
            return this.items.reduce((max, item) => item.price > max.price ? item : max, this.items[0]);
        },
        totalSelectedValue() {
            return this.selectedItems.reduce((total, item) => total + item.price, 0);
        },
        itemsToDisplayInSellModal() {
            if (this.selectedItemToSell) {
                return [this.selectedItemToSell];
            }
            return this.selectedItems;
        },
        totalSellValue() {
            return this.itemsToDisplayInSellModal.reduce((total, item) => total + item.price, 0);
        }
    },
    methods: {
        getItemImage(item) {
            const parts = item.name.split(' | ')
            const kind = parts[0].replace(' ', '_');
            const name = parts[1].replace(' ', '_');
            return `/src/images/gun/${kind}/${item.rarity}/${name}.png`;
        },
        getRarityStyle(rarity) {
            const style = this.rarityColors[rarity] || { background: '#CCCCCC', text: '#000000' };
            return {
                backgroundColor: style.background,
                color: style.text
            };
        },
        getRarityName(rarity) {
            return this.rarityNames[rarity] || 'Unknown';
        },
        toggleSelectItem(item) {
            const index = this.selectedItems.findIndex(i => i.id === item.id);
            if (index >= 0) {
                this.selectedItems.splice(index, 1);
            } else {
                this.selectedItems.push(item);
            }
        },
        selectItem(item) {
            this.selectedItem = item;
            this.selectedItemToSell = null;
        },
        closeSellModal() {
            this.showSellModal = false;
            this.selectedItemToSell = null;
        },
        copyTradeUrl() {
            navigator.clipboard.writeText('https://steamcommunity.com/tradeoffer/new/?partner=123456789&token=abcdefg');
            this.showNotification('Trade URL copied to clipboard', { type: 'success' });
            this.showDepositModal = false;
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
        async fetchInventory() {
            this.isLoading = true;
            try {
                const response = await fetch('/api/product/inventory', {
                    method: 'GET',
                    credentials: 'include'
                });
                const data = await response.json();
                if (!data) {
                    alert("Cannot retrieve information from inventory!");
                    return;
                }
                this.items = []

                data.forEach(e => {
                    const item = e.item;
                    const properties = e.properties;
                    this.items.push(
                        {
                            id: this.items.length + 1,
                            name: this.constructItemName(item.item_kind, item.item_name),
                            type: item.item_type,
                            rarity: item.rarity,
                            price: parseFloat(item.price),
                            exterior: properties.exterior,
                            stattrak: properties.stattrak,
                            collection: properties.collection,
                            for_sale: properties.for_sale,
                        }
                    );
                });
            } catch (error) {
                console.error('Error fetching inventory:', error);
                this.showNotification('Failed to load inventory', { type: 'error' });
            } finally {
                this.isLoading = false;
            }
        },
        constructItemName(item_kind, item_name) {
            return item_kind + ' | ' + item_name;
        },
        async confirmWithdraw() {
            if (this.selectedItems.length === 0 || !this.withdrawTradeUrl) {
                this.showNotification('Please select items and enter your trade URL.', { type: 'warning' });
                return;
            }
            this.isLoading = true;
            try {
                // Simulate API call
                await new Promise(resolve => setTimeout(resolve, 1000));
                
                this.showNotification('Withdrawal request submitted', {
                    type: 'success',
                    description: 'Your items will be sent to your Steam account shortly.'
                });
                this.showWithdrawModal = false;
                this.withdrawTradeUrl = '';
                this.selectedItems = [];
            } catch (error) {
                this.showNotification('Failed to process withdrawal', { type: 'error' });
            } finally {
                this.isLoading = false;
            }
        },
        async confirmSell() {
            this.isLoading = true;
            const itemsBeingSold = this.itemsToDisplayInSellModal;

            if (itemsBeingSold.length === 0) {
                this.showNotification('No items selected for sale.', { type: 'warning' });
                this.isLoading = false;
                return;
            }

            try {
                // Simulate API call
                await new Promise(resolve => setTimeout(resolve, 1000));

                const totalValueSold = itemsBeingSold.reduce((total, item) => total + item.price, 0);

                this.showNotification('Items sold successfully', {
                    type: 'success',
                    description: `$${totalValueSold.toFixed(2)} has been added to your balance.`
                });

                // Remove sold items from inventory
                const soldItemIds = new Set(itemsBeingSold.map(item => item.id));
                this.items = this.items.filter(item => !soldItemIds.has(item.id));

                this.selectedItems = [];
                this.closeSellModal();
            } catch (error) {
                this.showNotification('Failed to sell items', { type: 'error' });
            } finally {
                this.isLoading = false;
            }
        },
        async confirmTradeUp() {
            if (this.selectedItems.length < 10) {
                this.showNotification('You need to select 10 items for a trade up.', { type: 'warning' });
                return;
            }
            this.isLoading = true;
            try {
                // Simulate API call
                await new Promise(resolve => setTimeout(resolve, 1500));

                const outcomeValue = this.totalSelectedValue * (0.8 + Math.random() * 1.4);
                const outcomeRarity = this.getUpgradedRarity();

                const newItem = {
                    id: Date.now(),
                    name: `${this.getRarityName(outcomeRarity)} Skin (Trade Up)`,
                    type: this.selectedItems[0].type,
                    rarity: outcomeRarity,
                    price: outcomeValue,
                    added_at: new Date().toLocaleDateString(),
                    collection: this.selectedItems[0].collection,
                    exterior: 'Factory New',
                };

                this.showNotification('Trade Up completed!', {
                    type: 'success',
                    description: `You received: ${newItem.name} worth $${newItem.price.toFixed(2)}.`
                });

                // Remove traded items and add new item
                const tradedItemIds = new Set(this.selectedItems.map(item => item.id));
                this.items = [
                    ...this.items.filter(item => !tradedItemIds.has(item.id)),
                    newItem
                ];

                this.selectedItems = [];
                this.showTradeUpModal = false;
            } catch (error) {
                this.showNotification('Trade Up failed', { type: 'error' });
            } finally {
                this.isLoading = false;
            }
        },
        getUpgradedRarity() {
            const rarities = ['1', '2', '3', '4', '5'];
            const validItems = this.selectedItems.filter(item => rarities.includes(item.rarity));
            
            if (validItems.length === 0) return '1'; // Default to Industrial
            
            const avgIndex = validItems.reduce((sum, item) => {
                return sum + rarities.indexOf(item.rarity);
            }, 0) / validItems.length;

            const newIndex = Math.min(
                Math.floor(avgIndex + 1 + Math.random()),
                rarities.length - 1
            );
            return rarities[newIndex];
        }
    },
    async mounted() {
        await this.fetchProfile();
        await this.fetchInventory();
    }
}
</script>

<style scoped>
/* Custom scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #1A1A1A;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb {
    background: #8FC773;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #7BBF5A;
}
</style>