<script lang="ts">
	import { onMount } from 'svelte';

	let aboutHtml = '';
	let missionHtml = '';

	const team = [
		{ name: 'Kevin Chaves', role: 'Co-Founder / Software Developer', LinkedinUrl: 'https://www.youtube.com/watch?v=PDJLvF1dUek', img: '/images/team/kevin.jpg' },
		{ name: 'Daniel Arceo', role: 'Co-Founder / Outreach', LinkedinUrl: 'https://www.youtube.com/watch?v=PDJLvF1dUek', img: '/images/team/dan.jpg' },
		{ name: 'Adolfo David Romero', role: 'Software Developer', LinkedinUrl: 'https://www.youtube.com/watch?v=PDJLvF1dUek', img: '/images/team/david.jpg' },
		{ name: 'Evan', role: 'Software Developer', LinkedinUrl: 'https://www.youtube.com/watch?v=PDJLvF1dUek', img: '/images/team/evan.jpg' },
		{ name: 'Rani', role: 'UI Designer', LinkedinUrl: 'https://www.youtube.com/watch?v=PDJLvF1dUek', img: '/images/team/rani.jpg' }
	];

	onMount(async () => {
		const aboutRes = await fetch('/data/about.md');
		aboutHtml = await aboutRes.text();

		const missionRes = await fetch('/data/mission.md');
		missionHtml = await missionRes.text();
	});
</script>

<div class="min-h-screen w-full font-[Manrope] bg-light text-white flex flex-col items-center px-8 py-16">
	<!-- Header -->
	<div class="max-w-4xl text-center mb-12">
		<h1 class="text-4xl font-extrabold mb-4 text-primary">Showfari</h1>
		<p class="text-lg text-gray-300">{@html aboutHtml}</p>
	</div>

	<!-- Feature Cards -->
	<div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mb-16">
		<div class="bg-[#191F29] p-6 rounded-2xl shadow-lg border border-[#1E2126]">
			<h2 class="text-xl font-bold mb-2 text-primary-light">Curated Genres</h2>
			<p class="text-sm text-gray-400">Explore live events from Rock to Classical — we’ve got something for everyone.</p>
		</div>

		<div class="bg-[#191F29] p-6 rounded-2xl shadow-lg border border-[#1E2126]">
			<h2 class="text-xl font-bold mb-2 text-primary-light">Smart Filtering</h2>
			<p class="text-sm text-gray-400">Set your price range, pick your dates, and let us handle the rest.</p>
		</div>

		<div class="bg-[#191F29] p-6 rounded-2xl shadow-lg border border-[#1E2126]">
			<h2 class="text-xl font-bold mb-2 text-primary-light">Interactive Map</h2>
			<p class="text-sm text-gray-400">Visualize concerts on our beautiful, interactive venue map.</p>
		</div>
	</div>

	<!-- Mission -->
	<div class="max-w-4xl text-center mb-16">
		<h2 class="text-2xl font-bold mb-4 text-primary">Our Mission</h2>
		<p class="text-lg text-gray-300">{@html missionHtml}</p>
		<blockquote class="italic text-primary border-l-4 border-primary pl-4 mt-4 text-lg">
			“Shake ass?” — Dan
		</blockquote>
	</div>

	<!-- Team Section -->
	<div class="text-center max-w-5xl mx-auto mb-16">
		<h2 class="text-2xl font-bold mb-8 text-primary">Meet the Team</h2>
		<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
			{#each team as member}
				<div class="bg-[#191F29] rounded-2xl p-6 shadow-md border border-[#1E2126] flex flex-col items-center">
					<img
						src={member.img}
						alt={member.name}
						class="w-24 h-24 object-cover rounded-full mb-4 border-4 border-primary-dark"
					/>
					<h3 class="text-lg font-semibold">{member.name}</h3>
					<p class="text-sm text-gray-400">{member.role}</p>
					<a href={member.LinkedinUrl} target="_blank" class="mt-3">
						<img src="/icons/linkedin.svg" alt="LinkedIn" class="w-8 h-8 opacity-80 hover:opacity-100 transition" />
					</a>
				</div>
			{/each}
		</div>
	</div>

	<!-- Support -->
	<div class="text-center mb-8">
		<h2 class="text-2xl font-bold">Support us:</h2>
		<a
			href="https://ko-fi.com"
			target="_blank"
			class="text-primary hover:text-primary-light underline transition"
		>
			Buy us a coffee ☕
		</a>
	</div>

	<!-- Contact -->
	<div class="text-center">
		<h2 class="text-2xl">
			Contact us at:
			<a href="mailto:showfari.team@gmail.com" class="text-primary underline hover:text-primary-light">
				showfari.team@gmail.com
			</a>
		</h2>
	</div>
</div>
