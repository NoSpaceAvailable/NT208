<template>
    <div class="min-h-screen p-4 md:p-8 bg-[url('/src/images/community_wallpaper.png')] bg-cover bg-center font-['Inter',_sans-serif] relative">
        <!-- Controls: Search and Sort -->
        <div class="absolute inset-0 bg-black/60 z-0"></div>


        <div class="max-w-3xl mx-auto mb-10 relative z-10">
             
            <form class="mb-6" @submit.prevent>
                <label for="default-search" class="mb-2 text-sm font-medium text-gray-300 sr-only">Search</label>
                <div class="relative">
                    <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                        <svg class="w-5 h-5 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                        </svg>
                    </div>
                    <input
                        type="search"
                        id="default-search"
                        v-model="searchQuery"
                        class="block w-full p-4 ps-10 text-base text-white border-2 border-[#2D2D2D] rounded-lg bg-[#131313]/80 focus:ring-2 focus:ring-[#8FC773]/70 focus:border-[#8FC773] placeholder-gray-500 transition-colors duration-300"
                        placeholder="Search User by Name..."
                    />
                </div>
            </form>
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div class="flex items-center space-x-3">
                    <label for="sort-by" class="text-sm font-bold text-white">Sort by:</label>
                    <select
                        id="sort-by"
                        v-model="sortBy"
                        class="bg-[#131313]/80 text-white border-2 border-[#2D2D2D] rounded-md py-2 px-3 text-sm focus:ring-2 focus:ring-[#8FC773]/70 focus:border-[#8FC773] appearance-none transition-colors duration-300"
                        style="background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%238FC773%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'); background-repeat: no-repeat; background-position: right 0.7rem center; background-size: 0.7em auto; padding-right: 2.5rem;"
                    >
                        <option value="default">Relevance</option>
                        <option value="rating">Reputation</option>
                        <option value="transactions">Activity</option>
                        <option value="name">User Name</option>
                    </select>
                </div>
                <button
                    @click="toggleSortOrder"
                    class="flex items-center justify-center sm:justify-start space-x-2 px-4 py-2 text-sm font-semibold text-gray-200 bg-[#131313]/80 border-2 border-[#2D2D2D] rounded-md hover:bg-[#2D2D2D] hover:border-[#8FC773] hover:text-[#8FC773] transition-all duration-300"
                >
                    <svg v-if="sortOrder === 'asc'" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M14.707 10.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 12.586V5a1 1 0 012 0v7.586l2.293-2.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
                    <svg v-else class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 7.414V15a1 1 0 11-2 0V7.414L6.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
                    <span>{{ sortOrder === 'asc' ? 'Low to High' : 'High to Low' }}</span>
                </button>
            </div>
        </div>

        <!-- Community Section Title -->
        <div class="max-w-4xl mx-auto text-center mb-10 relative z-10">
            <h1 class="text-4xl md:text-5xl font-bold text-yellow-200 uppercase tracking-wider" style="text-shadow: 0 0 5px #8FC773, 0 0 10px #8FC773, 0 0 15px #000;">
                Community Roster
            </h1>
            <p class="text-lg text-gray-300 mt-2">Discover and connect with fellow gamers.</p>
        </div>

        <!-- Loading/Error/Content Area -->
        <div class="max-w-4xl mx-auto">
            <!-- Loading State -->
            <div v-if="isLoading" class="text-center text-gray-300 py-20"> </div>

            <!-- Error State -->
            <div v-else-if="fetchError" class="text-center bg-[#1A1A1A]/90 border-2 border-red-500/50 p-8 rounded-lg shadow-xl"> </div>

            <!-- Content -->
            <template v-else>
                <div v-if="paginatedUsers.length > 0" class="space-y-6">
                    <div
                        v-for="user in paginatedUsers"
                        :key="user.id"
                        class="bg-gradient-to-br from-[#1a1a1a]/90 to-[#101010]/90 backdrop-blur-sm rounded-lg shadow-2xl overflow-hidden border-2 border-[#2D2D2D] hover:border-[#8FC773]/70 transition-all duration-300 group relative"
                    >
                        <div class="absolute top-0 left-0 h-1.5 w-1/5 bg-[#8FC773] group-hover:w-full transition-all duration-500 ease-out rounded-tr-md rounded-bl-md"></div> 

                        <div class="flex flex-col sm:flex-row items-stretch">
                            <div class="flex-shrink-0 w-full sm:w-auto sm:min-w-[200px] md:min-w-[240px] bg-[#101010]/60 p-6 flex flex-col items-center justify-center text-center border-b-2 sm:border-b-0 sm:border-r-2 border-[#2D2D2D] group-hover:border-[#8FC773]/30 transition-colors">
                                <img :src="user.avatarUrl" :alt="user.name + ' avatar'"
                                     class="w-24 h-24 sm:w-28 sm:h-28 rounded-full object-cover border-4 border-[#4A4A4A] group-hover:border-[#8FC773] transition-colors duration-300 shadow-lg" />
                                <h3 class="mt-4 text-lg sm:text-xl font-bold text-white group-hover:text-[#8FC773] transition-colors duration-300 truncate w-full px-1">
                                    {{ user.name }}
                                </h3>
                                <p class="text-xs sm:text-sm text-gray-400 group-hover:text-gray-200 transition-colors">{{ user.role }}</p>
                            </div>

                            <div class="flex-grow p-5 sm:p-6 flex flex-col justify-between">
                                <div>
                                    <div class="grid grid-cols-2 gap-x-4 gap-y-2 text-xs sm:text-sm mb-4">
                                        <div class="text-left">
                                            <strong class="block font-semibold text-gray-300">Joined:</strong>
                                            <span class="text-gray-400">{{ user.joinedDate }}</span>
                                        </div>
                                        <div class="text-left">
                                            <strong class="block font-semibold text-gray-300">Activity:</strong>
                                            <span class="text-gray-400">{{ user.transactions.toLocaleString() }} XP</span> 
                                        </div>
                                    </div>
                                    <p v-if="user.bio" class="text-xs text-gray-400 mb-4 leading-relaxed max-h-16 overflow-hidden text-ellipsis">
                                        {{ user.bio.substring(0, 150) }}{{ user.bio.length > 150 ? '...' : '' }}
                                    </p>
                                </div>
                                
                                <div class="mt-auto pt-2">
                                    <div class="w-full mb-4">
                                        <div class="flex justify-between text-xs text-gray-300 mb-1 font-medium">
                                            <span>Reputation</span>
                                            <span>{{ user.rating.toFixed(1) }}/10</span>
                                        </div>
                                        <div class="w-full bg-[#2D2D2D] rounded-full h-3 overflow-hidden border border-[#3A3A3A]">
                                            <div :class="['h-full rounded-full transition-all duration-700 ease-out', getRatingColorClass(user.rating)]"
                                                 :style="{ width: (user.rating / 10 * 100) + '%' }"></div>
                                        </div>
                                    </div>

                                    <a :href="user.profileLink || '#'" target="_blank" rel="noopener noreferrer"
                                       class="block w-full sm:w-auto sm:float-right px-5 py-2.5 text-sm font-bold bg-gradient-to-r from-[#8FC773] to-[#76B35B] text-black rounded-md hover:from-[#A0D987] hover:to-[#8FC773] transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-[#8FC773] focus:ring-offset-2 focus:ring-offset-[#101010]">
                                        View Dossier
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else class="text-center text-gray-400 mt-20 bg-[#131313]/80 p-10 rounded-lg border-2 border-[#2D2D2D]"> No users found </div>
            </template>

            <!-- Pagination Controls -->
            <div v-if="totalPages > 1 && !isLoading && !fetchError" class="mt-12 pt-8 border-t-2 border-[#2D2D2D] flex flex-col sm:flex-row justify-between items-center gap-4"> {/* ... Pagination ... */} </div>
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
            usersPerPage: 6,
            isLoading: true,
            fetchError: null,
        };
    },
    computed: {
        filteredUsers() {
            if (!this.searchQuery) {
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
            let users = [...this.filteredUsers];
            if (this.sortBy !== 'default') {
                users.sort((a, b) => {
                    let valA, valB;
                    switch (this.sortBy) {
                        case 'rating': valA = a.rating; valB = b.rating; break;
                        case 'transactions': valA = a.transactions; valB = b.transactions; break;
                        case 'name':
                            valA = a.name || ''; valB = b.name || '';
                            return this.sortOrder === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
                        default: return 0;
                    }
                    if (typeof valA === 'number' && typeof valB === 'number') {
                        return this.sortOrder === 'asc' ? valA - valB : valB - valA;
                    }
                    return 0;
                });
            }
            return users;
        },
        totalPages() {
            if (!this.sortedAndFilteredUsers || this.sortedAndFilteredUsers.length === 0) return 0;
            return Math.ceil(this.sortedAndFilteredUsers.length / this.usersPerPage);
        },
        paginatedUsers() {
            const start = (this.currentPage - 1) * this.usersPerPage;
            const end = start + this.usersPerPage;
            return this.sortedAndFilteredUsers.slice(start, end);
        },
        pageNumbersToShow() {
            const total = this.totalPages; const current = this.currentPage; const pages = []; const maxPages = 5;
            if (total === 0) return pages;
            if (total <= maxPages + 2) { for (let i = 1; i <= total; i++) pages.push(i); }
            else {
                pages.push(1);
                let C = current; let T = total; let M = maxPages -2;
                let s = C - Math.floor(M/2); let e = C + Math.ceil(M/2) -1;
                if(s <= 1) { s = 2; e = M+1; }
                if(e >= T) { e = T-1; s = T-M; }
                if(s > 2) pages.push('...');
                for (let i = s; i <= e; i++) pages.push(i);
                if (e < T - 1) pages.push('...');
                pages.push(total);
            }
            return pages;
        }
    },
    watch: {
        searchQuery() { this.currentPage = 1; },
        sortBy() { this.currentPage = 1; },
        sortOrder() { this.currentPage = 1; },
        totalPages(newTotal) {
            if (this.currentPage > newTotal && newTotal > 0) this.currentPage = newTotal;
            else if (newTotal === 0) this.currentPage = 1;
        }
    },
    methods: {
        nextPage() { if (this.currentPage < this.totalPages) this.currentPage++; },
        prevPage() { if (this.currentPage > 1) this.currentPage--; },
        goToPage(page) {
            if (typeof page === 'number' && page > 0 && page <= this.totalPages) this.currentPage = page;
        },
        toggleSortOrder() { this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc'; },
        getRatingColorClass(rating) {
            if (rating <= 3.3) return 'bg-red-600';
            if (rating <= 6.6) return 'bg-yellow-500';
            return 'bg-gradient-to-r from-[#8FC773] to-[#6aaa4f]'; // Gaming gradient for high rating
        },
        async fetchUsersFromApi() {
            this.isLoading = true; this.fetchError = null;
            try {
                const response = await fetch('/api/profile/fetch/all');
                if (!response.ok) {
                    const errorData = await response.json().catch(() => ({}));
                    throw new Error(errorData.message || `Server Error: ${response.status}`);
                }
                const data = await response.json();
                let rawUsers = data['profile'];
                if (!Array.isArray(rawUsers)) {
                     console.error("Fetched data's 'profile' key is not an array:", rawUsers);
                     rawUsers = [];
                }

                this.allUsers = rawUsers.map((apiProfile, index) => {
                    let formattedJoinedDate = 'N/A';
                    if (apiProfile.joined_at) {
                        try {
                            formattedJoinedDate = new Date(apiProfile.joined_at).toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
                        } catch (e) { formattedJoinedDate = apiProfile.joined_at; }
                    }
                    const profileId = apiProfile.user_id || apiProfile.wallet_address || `user-${index + 1}`;
                    return {
                        id: profileId,
                        name: apiProfile.profile_name || `User ${index + 1}`,
                        role: apiProfile.role || 'Adventurer', 
                        avatarUrl: apiProfile.avatar_url || `https://robohash.org/mail@ashallendesign.co.uk`,
                        transactions: parseInt(apiProfile.transactions) || Math.floor(Math.random() * 100) + 5, 
                        rating: parseFloat(apiProfile.rating) || parseFloat((Math.random() * 7 + 3).toFixed(1)),
                        joinedDate: formattedJoinedDate,
                        bio: apiProfile.bio || '',
                        profileLink: apiProfile.profile_link || `https://example.com/profile/${profileId}` 
                    };
                });
            } catch (error) {
                console.error("Error fetching community roster:", error);
                this.fetchError = error.message || 'Failed to load user data. The server might be down.';
                this.allUsers = [];
            } finally {
                this.isLoading = false;
            }
        },
    },
    mounted() {
        this.fetchUsersFromApi();
    }
};
</script>

<style scoped>
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #1A1A1A; border-radius: 4px; }
::-webkit-scrollbar-thumb { background: #8FC773; border-radius: 4px; border: 2px solid #1A1A1A; }
::-webkit-scrollbar-thumb:hover { background: #A0D987; }
</style>