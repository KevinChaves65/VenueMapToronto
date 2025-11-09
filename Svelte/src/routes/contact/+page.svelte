<script lang="ts">
    import type { PageProps } from './$types';
    import Navbar from '$lib/components/navbar.svelte';
    import Footer from '$lib/components/footer.svelte';

    let { data }: PageProps = $props();
</script>

<Navbar />
<div>Contact</div>