<script lang="ts">
	import '../app.css';
	import '../styles.scss';
	import favicon from '$lib/assets/wob.png';
	import '$lib/actions/navigate'; // Auto-enables href on buttons

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>


{@render children()}
