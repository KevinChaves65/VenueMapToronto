<script lang="ts">
	import { page } from '$app/state';
	import Navbar from '$lib/componants/navbar.svelte';
	import Footer from '$lib/componants/footer.svelte';
	import Error404 from '$lib/error-pages/404.svelte';
	
	// Check if it's a 404 error
	$: is404 = page.status === 404;
	$: errorMessage = is404 
		? "Page Not Found" 
		: "Something went wrong";
	$: errorDescription = is404
		? "The page you're looking for seems to have wandered off stage."
		: page.error?.message || "We're experiencing some technical difficulties. Please try again later.";
</script>

<Navbar />

{#if is404}
	<!-- Use the modern 404 component -->
	<Error404 />
{:else}
	<!-- Generic error display -->
	<div class="flex min-h-[calc(100vh-200px)] items-center justify-center px-[5%] py-20">
		<div class="text-center">
			<h1 class="mb-4 text-6xl font-bold text-primary md:text-8xl">
				{page.status || 500}
			</h1>
			<h2 class="mb-4 text-2xl font-semibold text-tertiary md:text-3xl">
				{errorMessage}
			</h2>
			<p class="mx-auto mb-8 max-w-md text-lg text-tertiary-light">
				{errorDescription}
			</p>
			<div class="flex flex-col items-center justify-center gap-4 sm:flex-row">
				<button
					href="/"
					class="rounded-lg bg-primary px-6 py-2.5 font-semibold text-white transition-all duration-200 hover:bg-primary-dark"
				>
					Go Home
				</button>
				<button
					on:click={() => window.history.back()}
					class="rounded-lg border-2 border-secondary-dark bg-transparent px-6 py-2.5 font-semibold text-tertiary transition-all duration-200 hover:bg-secondary-dark"
				>
					Go Back
				</button>
			</div>
		</div>
	</div>
{/if}

