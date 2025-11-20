<script lang="ts">
	import { Music2 } from 'lucide-svelte';

	export let artist = {
		name: 'Artist Name',
		genre: 'Rock',
		image: ''
	};

	function handleError(e: Event) {
		const target = e.target as HTMLImageElement;
		target.src = '/images/placeholder.png';
	}
</script>

<div class="bg-[#14171D] text-white rounded-2xl overflow-hidden shadow-lg border border-[#1E2126] w-full">
	<div class="bg-gray-300 h-40 flex items-center justify-center">
		<img
			src={artist.image}
			alt={artist.name}
			class="w-full h-full object-cover"
			on:error={handleError}
		/>
	</div>

	<div class="p-4 space-y-2">
		<h3 class="font-semibold text-lg leading-snug">{artist.name}</h3>

		<div class="flex items-center gap-2 text-sm">
			<Music2 class="w-4 h-4 text-gray-400" />
			<span>{artist.genre}</span>
		</div>

		<button
			class="w-full mt-4 bg-white text-black py-2 rounded-md font-medium hover:bg-gray-200 transition"
		>
			View Artist
		</button>
	</div>
</div>
