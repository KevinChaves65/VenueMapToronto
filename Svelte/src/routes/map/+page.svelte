<script lang="ts">
  import Sidebar from '$lib/components/sidebar.svelte';
  import Topbar from '$lib/components/navbar.svelte';
  import MapView from '$lib/components/mapView.svelte';
</script>

<div class="flex h-screen w-full overflow-hidden">
  <Sidebar />
  <div class="flex-1 relative">
    <Topbar />
    <MapView />
  </div>
</div>