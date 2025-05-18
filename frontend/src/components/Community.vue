<template>
    <div class="min-h-screen p-4 md:p-8 bg-[url('/src/images/community_wallpaper.png')] bg-cover bg-center">
        <!-- Controls: Search and Sort -->
        <div class="max-w-2xl mx-auto mb-10">
            <!-- Search bar -->
            <form class="mb-6" @submit.prevent>
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
                        placeholder="Search Users by Name or Role..."
                    />
                </div>
            </form>

            <!-- Sort Controls -->
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div class="flex items-center space-x-2">
                    <label for="sort-by" class="text-sm text-gray-300">Sort by:</label>
                    <select
                        id="sort-by"
                        v-model="sortBy"
                        class="bg-[#1A1A1A] text-white border border-[#2D2D2D] rounded-md py-2 px-3 text-sm focus:ring-[#8FC773]/50 focus:border-[#8FC773] appearance-none"
                        style="background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23BBB%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'); background-repeat: no-repeat; background-position: right 0.5rem center; background-size: 0.65em auto; padding-right: 2rem;"
                    >
                        <option value="default">Default</option>
                        <option value="rating">Rating</option>
                        <option value="transactions">Transactions</option>
                        <option value="name">Name</option>
                    </select>
                </div>
                <button
                    @click="toggleSortOrder"
                    class="flex items-center space-x-1 px-3 py-2 text-sm font-medium text-gray-300 bg-[#1A1A1A] border border-[#3A3A3A] rounded-md hover:bg-[#2D2D2D] hover:text-[#8FC773] transition-colors"
                >
                    <svg v-if="sortOrder === 'asc'" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M14.707 10.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 12.586V5a1 1 0 012 0v7.586l2.293-2.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
                    <svg v-else class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 7.414V15a1 1 0 11-2 0V7.414L6.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
                    <span>{{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}</span>
                </button>
            </div>
        </div>

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
                    <h3 class="text-sm font-bold text-white truncate">
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

<script>
export default {
    name: 'CommunityPage',
    data() {
        return {
            allUsers: [],
            searchQuery: '',
            sortBy: 'default',
            sortOrder: 'desc',
            currentPage: 1,
            usersPerPage: 12,
            fetchError: null, 
            demoUsers: [
                { id: 1, name: 'John Doe', role: 'Developer', transactions: 5, rating: 8.5, avatarUrl: 'https://via.placeholder.com/150' },
                { id: 2, name: 'Jane Smith', role: 'Designer', transactions: 10, rating: 9.0, avatarUrl: 'https://via.placeholder.com/150' },
                // Add more demo users as needed
            ]
        };
    },
    computed: {
        filteredUsers() {
            if(!this.searchQuery) {
                return this.allUsers;
            }

            return this.allUsers.filter(user => {
                const searchLower = this.searchQuery.toLowerCase();
                const nameMatch = user.name && user.name.toLowerCase().includes(searchLower);
                const roleMatch = user.role && user.role.toLowerCase().includes(searchLower);
                return nameMatch || roleMatch;
            });
        },

        sortedAndFilteredUsers() {
            let users = this.filteredUsers.slice();

            if (this.sortBy === 'rating') {
                users.sort((a, b) => this.sortOrder === 'asc' ? a.rating - b.rating : b.rating - a.rating);
            } else if (this.sortBy === 'transactions') {
                users.sort((a, b) => this.sortOrder === 'asc' ? a.transactions - b.transactions : b.transactions - a.transactions);
            } else if (this.sortBy === 'name') {
                users.sort((a, b) => this.sortOrder === 'asc' ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name));
            }

            return users;
        },

        totalPages() {
            if (this.sortedAndFilteredUsers.length === 0) {
                return 0;
            }
            return Math.ceil(this.sortedAndFilteredUsers.length / this.usersPerPage);
        },

        paginatedUsers() {
            const start = (this.currentPage - 1) * this.usersPerPage;
            const end = start + this.usersPerPage;
            return this.sortedAndFilteredUsers.slice(start, end);
        },
        pageNumbersToShow() {
            const totalPages = this.totalPages;
            const pages = [];
            const maxPagesToShow = 5;

            if (totalPages <= maxPagesToShow) {
                for (let i = 1; i <= totalPages; i++) {
                    pages.push(i);
                }
            } else {
                if (this.currentPage > 3) {
                    pages.push(1);
                    if (this.currentPage > 4) pages.push('...');
                }
                for (let i = Math.max(1, this.currentPage - 1); i <= Math.min(totalPages, this.currentPage + 1); i++) {
                    pages.push(i);
                }
                if (this.currentPage < totalPages - 2) {
                    if (this.currentPage < totalPages - 3) pages.push('...');
                    pages.push(totalPages);
                }
            }

            return pages;
        }

    },
    watch: {
        searchQuery() {
            this.currentPage = 1; // Reset to first page on search
        },
        sortBy() {
            this.currentPage = 1; // Reset to first page on sort change
        },
        sortOrder() {
            this.currentPage = 1; // Reset to first page on sort order change
        },
        totalPages(newTotalPages) {
            if (this.currentPage > newTotalPages && newTotalPages > 0) {
                this.currentPage = newTotalPages; // Adjust current page if it exceeds total pages
            }
            else if (this.currentPage > newTotalPages && newTotalPages === 0) {
                this.currentPage = 1; // Reset to first page if no users are found
            }
        }
    },
    methods: {
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
            }
        },
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        goToPage(page) {
            if (typeof page === 'number' && page > 0 && page <= this.totalPages) {
                this.currentPage = page;
            }
        },
        toggleSortOrder() {
            this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
        },
        getRatingColorClass(rating) {
            if (rating <= 3.3) return 'bg-red-600';
            else if (rating <= 6.6) return 'bg-yellow-500';
            else return 'bg-[#8FC773]';
        },
        async fetchedUsers() {
            console.log('Fetching users...');
            this.fetchError = null; 
            try {
                const response = await fetch('/api/profile/fetch/all', {
                    method: 'GET',
                    credentials: 'include'
                });
                if (!response.ok) {
                    console.error('Network response was not ok:', response.statusText);
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log('Fetched data:', data);

                let rawUsers = data['profile'];
                console.log('Raw users:', rawUsers);

                // for (const user of rawUsers) {
                //     console.log('User:', user);
                //     // append to allUsers
                //     this.allUsers.push(user);
                // }

                //TODO: complete the data fetching logic
                this.allUsers = rawUsers.map((user, index) => {
                    return {
                        id: index + 1, 
                        name: user.profile_name || 'Unknown Name', // Fallback name if not available
                        role: 'Unknown Role',
                        avatarUrl: 'https://via.placeholder.com/150', // Fallback avatar URL
                        transactions: Math.floor(Math.random() * 20) + 1, // Random number of transactions for demo
                        rating: parseFloat((Math.random() * 7 + 3).toFixed(1)), // Random rating for demo
                        // joinedDate: 'Unknown Date',
                    };
                });
                console.log('Fetched users success:', this.allUsers);

                this.fetchError = null;
            }
            catch (error) {
                this.fetchError = 'Failed to fetch users. Please try again later.';
            }
        },
    },
    mounted() {
        this.fetchedUsers();
    }
};
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