<script lang="ts">
  export let title = 'Event Title';
  export let date = 'August 1, 2026';
  export let genre = 'Rock';
  export let distance = '12km Away';
</script>

<div class="bg-[#1B1E25] rounded-lg shadow-md p-3 flex flex-col gap-2 hover:bg-[#21242C] transition">
  <div class="bg-[#2A2E36] rounded-md h-32 flex items-center justify-center text-gray-500">
    <img src="/images/placeholder.svg" alt="Event image" class="w-full h-full object-cover rounded-md" />
  </div>

  <h3 class="font-semibold text-white text-base mt-1">{title}</h3>

  <div class="text-gray-400 text-sm space-y-1">
    <div class="flex items-center gap-2">
      <span>📅</span>
      <span>{date}</span>
    </div>
    <div class="flex items-center gap-2">
      <span>🎵</span>
      <span>{genre}</span>
    </div>
    <div class="flex items-center gap-2">
      <span>📍</span>
      <span>{distance}</span>
    </div>
  </div>

  <button class="w-full bg-white text-black rounded-md py-1.5 text-sm mt-2 hover:bg-gray-200">
    Get Tickets
  </button>
</div>
