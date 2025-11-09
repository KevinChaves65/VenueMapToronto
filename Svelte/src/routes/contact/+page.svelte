<script lang="ts">
    import type { PageProps } from './$types';
    import Navbar from '$lib/componants/navbar.svelte';
    import Footer from '$lib/componants/footer.svelte';

    let { data }: PageProps = $props();
</script>

<Navbar />
<div>Contact</div>