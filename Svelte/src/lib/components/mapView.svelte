<script lang="ts">
  import { onMount } from 'svelte';
  import {
    initMap,
    removeMap,
    selectedVenue,
    popupPosition
  } from '$lib/stores/map';

  let mapContainer: HTMLDivElement;

  onMount(async () => {
    await initMap(mapContainer.id);
    return () => removeMap();
  });
</script>

<div class="relative w-full h-full">
  <div bind:this={mapContainer} id="map" class="w-full h-full"></div>

  {#if $selectedVenue && $popupPosition}
    <div
      class="absolute bg-black/80 text-white p-3 rounded-lg shadow-lg min-w-[200px] max-w-[280px]"
      style="left: {$popupPosition.x}px; top: {$popupPosition.y}px; transform: translate(-50%, -110%);"
    >
      <button
        class="absolute top-1 right-2 text-white text-lg"
        on:click={() => selectedVenue.set(null)}
      >
        ×
      </button>
      <h3 class="font-bold text-lg">{$selectedVenue.name}</h3>
      <p class="text-sm text-gray-300">{$selectedVenue.address}</p>
      {#if $selectedVenue.vimage}
        <img
          src={$selectedVenue.vimage}
          alt={$selectedVenue.name}
          class="w-full h-32 object-cover rounded mt-2"
        />
      {/if}
      <button
        class="w-full mt-3 bg-primary text-white rounded py-1 hover:bg-primary-dark"
      >
        View Events
      </button>
    </div>
  {/if}
</div>

<style>
  #map {
    position: absolute;
    inset: 0;
  }
</style>
