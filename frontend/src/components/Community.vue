<template>
    <div class="min-h-screen p-4 md:p-8 bg-[#111111]">
        <!-- Search bar -->
        <form class="max-w-md mx-auto" @submit.prevent>
            <label for="default-search" class="mb-2 text-sm font-medium text-gray-300 sr-only">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                    </svg>
                </div>
                <input
                    type="search"
                    id="default-search"
                    v-model="searchQuery"
                    class="block w-full p-4 ps-10 text-sm text-white border border-[#2D2D2D] rounded-lg bg-[#1A1A1A] focus:ring-[#8FC773]/50 focus:border-[#8FC773] placeholder-gray-500"
                    placeholder="Search Users by Name..."
                />
            </div>
        </form>

        <!-- Community section -->
        <div class="mt-12 max-w-6xl mx-auto">
            <h2 class="text-3xl font-bold text-center text-[#8FC773] mb-8">
                Meet Our Community
            </h2>

            <div v-if="paginatedUsers.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <div
                    v-for="user in paginatedUsers"
                    :key="user.id"
                    class="bg-[#131313] rounded-xl shadow-lg p-6 flex flex-col items-center text-center transition-all hover:shadow-xl hover:shadow-[#8FC773]/20 hover:scale-105"
                >
                    <img
                        :src="user.avatarUrl"
                        :alt="user.name + ' avatar'"
                        class="w-24 h-24 rounded-full object-cover mb-4 border-4 border-[#2D2D2D] group-hover:border-[#8FC773]/50 transition-colors"
                    />
                    <h3 class="text-xl font-semibold text-white">
                        {{ user.name }}
                    </h3>
                    <p class="text-sm text-[#8FC773]/80 mt-1">
                        {{ user.role }}
                    </p>
                    <p class="text-xs text-gray-500 mt-2">
                        Number of Transaction: {{ user.transactions }}
                    </p>

                    <!-- Rating Line -->
                    <div class="w-full mt-4">
                        <div class="flex justify-between text-xs text-gray-400 mb-1">
                            <span>Reputation</span>
                            <span>{{ user.rating.toFixed(1) }}/10</span>
                        </div>
                        <div class="w-full bg-[#2D2D2D] rounded-full h-2.5">
                            <div
                                :class="['h-2.5 rounded-full', getRatingColorClass(user.rating)]"
                                :style="{ width: (user.rating / 10 * 100) + '%' }"
                            ></div>
                        </div>
                    </div>

                    <!-- <a
                        href="#"
                        class="mt-6 inline-block bg-[#8FC773] hover:bg-[#7BBF5A] text-black text-sm font-medium py-2 px-4 rounded-lg transition-colors"
                    >
                        View Profile
                    </a> -->
                </div>
            </div>
            <div v-else class="text-center text-gray-400 mt-10">
                <p class="text-xl">No users found matching your search criteria.</p>
            </div>

            <!-- Pagination Controls -->
            <div v-if="totalPages > 1" class="mt-10 flex justify-center items-center space-x-2">
                <button
                    @click="prevPage"
                    :disabled="currentPage === 1"
                    class="px-4 py-2 text-sm font-medium text-gray-300 bg-[#1A1A1A] border border-[#3A3A3A] rounded-md hover:bg-[#2D2D2D] hover:text-[#8FC773] disabled:opacity-50 disabled:hover:bg-[#1A1A1A] disabled:hover:text-gray-300 transition-colors"
                >
                    Previous
                </button>

                <template v-for="(page, index) in pageNumbersToShow" :key="index">
                    <span v-if="page === '...'" class="px-2 py-2 text-sm text-gray-400">...</span>
                    <button
                        v-else
                        @click="goToPage(page)"
                        :class="[
                            'px-4 py-2 text-sm font-medium border rounded-md transition-colors',
                            currentPage === page
                                ? 'bg-[#8FC773] text-black border-[#8FC773]'
                                : 'text-gray-300 bg-[#1A1A1A] border-[#3A3A3A] hover:bg-[#2D2D2D] hover:text-[#8FC773]'
                        ]"
                    >
                        {{ page }}
                    </button>
                </template>

                <button
                    @click="nextPage"
                    :disabled="currentPage === totalPages"
                    class="px-4 py-2 text-sm font-medium text-gray-300 bg-[#1A1A1A] border border-[#3A3A3A] rounded-md hover:bg-[#2D2D2D] hover:text-[#8FC773] disabled:opacity-50 disabled:hover:bg-[#1A1A1A] disabled:hover:text-gray-300 transition-colors"
                >
                    Next
                </button>
            </div>
            <div v-if="totalPages > 0" class="mt-4 text-center text-sm text-gray-400">
                Page {{ currentPage }} of {{ totalPages }}
                <span v-if="searchQuery"> ({{ filteredUsers.length }} users found)</span>
                <span v-else> ({{ allUsers.length }} total users)</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';

// Dummy user data - Added 'rating' property
const allUsers = ref([
    { id: 1, name: 'Alice Wonderland', role: 'Community Lead', avatarUrl: 'https://i.pravatar.cc/150?u=alice', transactions: 10, rating: 9.2 },
    { id: 2, name: 'Bob The Builder', role: 'Top Contributor', avatarUrl: 'https://i.pravatar.cc/150?u=bob', transactions: 23, rating: 8.5 },
    { id: 3, name: 'Charlie Brown', role: 'Moderator', avatarUrl: 'https://i.pravatar.cc/150?u=charlie', transactions: 23, rating: 7.0 },
    { id: 4, name: 'Diana Prince', role: 'Active Member', avatarUrl: 'https://i.pravatar.cc/150?u=diana', transactions: 2, rating: 6.5 },
    { id: 5, name: 'Edward Scissorhands', role: 'New Member', avatarUrl: 'https://i.pravatar.cc/150?u=edward', transactions: 12, rating: 4.2 },
    { id: 6, name: 'Fiona Gallagher', role: 'Mentor', avatarUrl: 'https://i.pravatar.cc/150?u=fiona', transactions: 1, rating: 9.8 },
    { id: 7, name: 'George Costanza', role: 'Event Organizer', avatarUrl: 'https://i.pravatar.cc/150?u=george', transactions: 45, rating: 3.1 },
    { id: 8, name: 'Harry Potter', role: 'Wizarding Enthusiast', avatarUrl: 'https://i.pravatar.cc/150?u=harry', transactions: 55, rating: 7.7 },
    { id: 9, name: 'Ivy Gardener', role: 'Botanist', avatarUrl: 'https://i.pravatar.cc/150?u=ivy', transactions: 234, rating: 8.0 },
    { id: 10, name: 'Jack Sparrow', role: 'Captain', avatarUrl: 'https://i.pravatar.cc/150?u=jack', transactions: 22, rating: 2.5 },
    { id: 11, name: 'Kyle Broflovski', role: 'Student', avatarUrl: 'https://i.pravatar.cc/150?u=kyle', transactions: 31, rating: 5.5 },
    { id: 12, name: 'Laura Palmer', role: 'Mystery', avatarUrl: 'https://i.pravatar.cc/150?u=laura', transactions: 22, rating: 6.9 },
    { id: 13, name: 'Michael Scott', role: 'Manager', avatarUrl: 'https://i.pravatar.cc/150?u=michael', transactions: 13, rating: 1.5 },
    { id: 14, name: 'Nancy Drew', role: 'Detective', avatarUrl: 'https://i.pravatar.cc/150?u=nancy', transactions: 13, rating: 8.8 },
    { id: 15, name: 'Oliver Twist', role: 'Orphan', avatarUrl: 'https://i.pravatar.cc/150?u=oliver', transactions: 45, rating: 4.9 },
    { id: 16, name: 'Peter Pan', role: 'Lost Boy', avatarUrl: 'https://i.pravatar.cc/150?u=peter', transactions: 55, rating: 7.2 },
    { id: 17, name: 'Quinn Fabray', role: 'Cheerleader', avatarUrl: 'https://i.pravatar.cc/150?u=quinn', transactions: 556, rating: 9.0 },
]);

const searchQuery = ref('');
const currentPage = ref(1);
const usersPerPage = ref(8);

const filteredUsers = computed(() => {
    if (!searchQuery.value) {
        return allUsers.value;
    }
    return allUsers.value.filter(user =>
        user.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        user.role.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
});

const totalPages = computed(() => {
    if (filteredUsers.value.length === 0) return 0;
    return Math.ceil(filteredUsers.value.length / usersPerPage.value);
});

const paginatedUsers = computed(() => {
    const start = (currentPage.value - 1) * usersPerPage.value;
    const end = start + usersPerPage.value;
    return filteredUsers.value.slice(start, end);
});

watch(searchQuery, () => {
    currentPage.value = 1;
});

watch(totalPages, (newTotalPages) => {
    if (currentPage.value > newTotalPages && newTotalPages > 0) {
        currentPage.value = newTotalPages;
    } else if (newTotalPages === 0 && filteredUsers.value.length > 0) {
        currentPage.value = 1;
    } else if (newTotalPages === 0) {
        currentPage.value = 1;
    }
});


function nextPage() {
    if (currentPage.value < totalPages.value) {
        currentPage.value++;
    }
}

function prevPage() {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
}

function goToPage(pageNumber) {
    if (typeof pageNumber === 'number' && pageNumber >= 1 && pageNumber <= totalPages.value) {
        currentPage.value = pageNumber;
    }
}

const pageNumbersToShow = computed(() => {
    const pages = [];
    if (totalPages.value === 0) return pages;
    const maxPagesToShow = 5;
    const current = currentPage.value;
    const total = totalPages.value;

    if (total <= maxPagesToShow + 2) {
        for (let i = 1; i <= total; i++) pages.push(i);
    } else {
        pages.push(1);
        let startPage, endPage;
        if (current <= maxPagesToShow - 2) {
            startPage = 2;
            endPage = maxPagesToShow - 1;
            for (let i = startPage; i <= endPage; i++) pages.push(i);
            if (endPage < total -1) pages.push('...');
        } else if (current >= total - (maxPagesToShow - 3)) {
            pages.push('...');
            startPage = total - (maxPagesToShow - 2);
            for (let i = startPage; i < total; i++) pages.push(i);
        } else {
            pages.push('...');
            startPage = current - Math.floor((maxPagesToShow - 3) / 2); 
            endPage = current + Math.floor((maxPagesToShow - 3) / 2);
            for (let i = startPage; i <= endPage; i++) pages.push(i);
            pages.push('...');
        }
        pages.push(total);
    }
    const finalPages = pages.reduce((acc, curr, idx, src) => {
        if (!(curr === '...' && src[idx - 1] === '...')) acc.push(curr);
        return acc;
    }, []);
    if (finalPages.length > 2 && finalPages[0] === 1 && finalPages[1] === '...' && finalPages[2] === 2) finalPages.splice(1, 1);
    if (finalPages.length > 2 && finalPages[finalPages.length - 1] === total && finalPages[finalPages.length - 2] === '...' && finalPages[finalPages.length - 3] === total - 1) finalPages.splice(finalPages.length - 2, 1);
    return finalPages;
});

// Helper function for rating color
function getRatingColorClass(rating) {
    if (rating <= 3.3) {
        return 'bg-red-600'; // Low rating - Red
    } else if (rating <= 6.6) {
        return 'bg-yellow-500'; // Medium rating - Yellow
    } else {
        return 'bg-[#8FC773]'; // High rating - Green (using your theme's green)
    }
}

</script>

<style scoped>
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