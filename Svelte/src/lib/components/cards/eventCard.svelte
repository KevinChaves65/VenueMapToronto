<script lang="ts">
	import { CalendarDays, Music2, MapPin } from 'lucide-svelte';

	export let event = {
		name: 'Event Title',
		date: 'August 1, 2026',
		genre: 'Rock',
		distance: '12km Away',
		image: ''
	};

	function handleError(e: Event) {
		const target = e.target as HTMLImageElement;
		target.src = '/images/placeholder.png';
	}
</script>

<div class="bg-[#14171D] text-white rounded-2xl overflow-hidden shadow-lg border border-[#1E2126] w-full">
	<!-- Image -->
	<div class="bg-gray-300 h-40 flex items-center justify-center">
		<img
			src={event.image}
			alt={event.name}
			class="w-full h-full object-cover"
			on:error={handleError}
		/>
	</div>

	<!-- Info -->
	<div class="p-4 space-y-2">
		<h3 class="font-semibold text-lg leading-snug">{event.name}</h3>

		<div class="flex items-center gap-2 text-sm">
			<CalendarDays class="w-4 h-4 text-gray-400" />
			<span>{event.date}</span>
		</div>

		<div class="flex items-center gap-2 text-sm">
			<Music2 class="w-4 h-4 text-gray-400" />
			<span>{event.genre}</span>
		</div>

		<div class="flex items-center gap-2 text-sm">
			<MapPin class="w-4 h-4 text-gray-400" />
			<span>{event.distance}</span>
		</div>

		<button
			class="w-full mt-4 bg-white text-black py-2 rounded-md font-medium hover:bg-gray-200 transition"
		>
			Get Tickets
		</button>
	</div>
</div>
