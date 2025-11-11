<script lang="ts">
  import EventCard from '$lib/components/cards/eventCard.svelte';
  let category = 'Events';
  let categories = ['Events', 'Venues', 'Artists'];
</script>

<aside class="w-[320px] bg-[#14171D] text-white flex flex-col border-r border-[#1E2126]">
  <!-- Top dropdown bar -->
  <div class="flex items-center justify-between px-3 py-3 border-b border-[#1E2126]">
    <select bind:value={category} class="bg-[#1F2229] text-sm rounded-md px-3 py-2 w-full">
      {#each categories as c}
        <option>{c}</option>
      {/each}
    </select>
  </div>

  <!-- Scrollable content -->
  <div class="flex-1 overflow-y-auto px-3 py-4 space-y-4">
    <EventCard />
    <EventCard />
    <EventCard />
  </div>
</aside>
