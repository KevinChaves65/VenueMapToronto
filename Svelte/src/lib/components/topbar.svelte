<script lang="ts">
	import { Search, Filter } from 'lucide-svelte';
	let activeFilter = 'Label 1';
	let filters = ['Label 1', 'Label 2', 'Label 3', 'Label 4'];
</script>

<nav
	class="flex items-center justify-between bg-[#1C1F26] px-4 py-3 border-b shadow-sm text-sm"
>
	<!-- Left: Search + Filters -->
	<div class="flex items-center gap-3 flex-1">
		<!-- Search Bar -->
		<div
			class="flex items-center gap-2 bg-[#262A33] text-gray-300 rounded-md px-3 py-2 w-64 focus-within:ring-2"
		>
			<Search class="w-4 h-4 opacity-70" />
			<input
				type="text"
				placeholder="Search"
				class="bg-transparent outline-none flex-1 text-sm placeholder-gray-500"
			/>
		</div>

		<!-- Filter Icon -->
		<button
			class="p-2 rounded-md bg-[#262A33] hover:bg-[#2F343D] text-gray-300 transition"
			title="Filter"
		>
			<Filter class="w-4 h-4" />
		</button>

		<!-- Filter Buttons -->
		<div class="flex items-center gap-2">
			{#each filters as label}
				<button
					class="px-3 py-1.5 rounded-full font-medium transition border border-transparent
          {label === activeFilter
            ? 'bg-[#D3E2EC] text-[#0F172A]'
            : 'bg-[#EAE6F2]/10 text-[#E5E7EB] hover:bg-[#343A44]'}"
					on:click={() => (activeFilter = label)}
				>
					{label}
				</button>
			{/each}
		</div>
	</div>

	<!-- Right: Notification + Profile -->
	<div class="flex items-center gap-4 ml-4">
		<!-- Notification -->
		<button
			class="relative p-2 rounded-full bg-[#262A33] hover:bg-[#2F343D] text-gray-300 transition"
		>
		settings
		</button>

		<!-- Profile Placeholder -->
		<div
			class="w-8 h-8 rounded-full bg-[#D1D5DB] flex items-center justify-center text-gray-700 text-xs font-semibold"
		>
			<img
				src="/images/profile-placeholder.jpg"
				alt="User"
				class="w-8 h-8 rounded-full object-cover"
			/>
		</div>
	</div>
</nav>
