<script lang="ts">
	import EventCard from '$lib/components/cards/eventCard.svelte';
	import VenueCard from '$lib/components/cards/venueCard.svelte';
	import ArtistCard from '$lib/components/cards/artistCard.svelte';
	import { sidebarOpen, toggleSidebar } from '$lib/stores/UI';
	import { ChevronLeft, ChevronRight } from 'lucide-svelte';
	import { events } from '$lib/stores/event';
	import { venues } from '$lib/stores/venue';
	import { artists } from '$lib/stores/artist';

	let category = 'Events';
	let categories = ['Events', 'Venues', 'Artists'];
</script>

<aside
	class="fixed md:static z-40 h-full w-[320px] bg-[#14171D] text-white flex flex-col border-r border-[#1E2126]
	transition-transform duration-300 ease-in-out
	md:translate-x-0
	{ $sidebarOpen ? 'translate-x-0' : '-translate-x-full' }"
>
	<!-- Header -->
	<div class="flex items-center justify-between px-4 py-3 border-b border-[#1E2126]">
		<!-- Category selector -->
		<select
			bind:value={category}
			class="bg-[#1C1F26] text-white text-sm p-2 rounded-md outline-none"
		>
			{#each categories as c}
				<option value={c}>{c}</option>
			{/each}
		</select>

		<!-- Collapse Button -->
		<button
			class="p-2 rounded-md bg-[#1C1F26] hover:bg-[#2A2E36] text-gray-300 transition"
			on:click={toggleSidebar}
			aria-label="Collapse sidebar"
		>
			{#if $sidebarOpen}
				<ChevronLeft class="w-4 h-4" />
			{:else}
				<ChevronRight class="w-4 h-4" />
			{/if}
		</button>
	</div>

	<!-- Card Content -->
	<div class="flex-1 overflow-y-auto px-3 py-4 space-y-4">
		{#if category === 'Events'}
				<EventCard/>

		{:else if category === 'Venues'}
				<VenueCard/>

		{:else if category === 'Artists'}
				<ArtistCard/>
		{/if}
	</div>
</aside>
