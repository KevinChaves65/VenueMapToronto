<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  // --- Data ---
  const images = [
    'concert1.jpg', 'concert2.jpg', 'concert3.jpg',
    'concert4.jpg', 'concert5.jpg', 'concert6.jpg',
    'concert7.jpg', 'concert8.jpg', 'concert9.jpg'
  ];

  const genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Electronic', 'Classical'];

  // --- Reactive state vars ---
  let currentIndex = 0;
  let maxPrice = 150;
  let selectedGenre = 'All';
  let fromDate = '';
  let toDate = '';

  onMount(() => {
    const interval = setInterval(() => {
      currentIndex = (currentIndex + 1) % images.length;
    }, 6000);
    return () => clearInterval(interval);
  });

  const goToMap = () => goto('/map');
  const goToSignUp = () => goto('/signup');
  const goToSignIn = () => goto('/signin');
</script>

<!-- Main Wrapper -->
<div class="relative w-full h-screen font-[Manrope] overflow-hidden bg">

  <!-- Background Slideshow -->
  <div class="absolute inset-0 z-0">
    {#each images as image, i}
      <img
        src={`/images/landingPics/${image}`}
        alt="Concert slideshow"
        class="absolute inset-0 w-full h-full object-cover transition-opacity duration-1000 rounded-2xl"
        class:opacity-100={i === currentIndex}
        class:opacity-0={i !== currentIndex}
      />
    {/each}
    <div class="absolute inset-0 bg-black/50" />
  </div>

  <div class="relative z-10 flex flex-col h-full text-white">
    <header class="flex justify-between items-center px-10 py-6">
      <h1 class="text-3xl font-extrabold tracking-tight">Showfari</h1>
      <nav class="space-x-6 font-semibold">
        <button class="secondary" on:click={goToSignUp}>Sign up</button>
        <button class="secondary" on:click={goToSignIn}>Sign in</button>
      </nav>
    </header>

    <!-- Hero Card -->
    <main class="flex-grow flex items-center px-10">
      <div class="fg shadow-2xl p-8 rounded-2xl w-[28rem] backdrop-blur-md">
        <h2 class="text-3xl font-extrabold leading-snug">
          Discover live music events in Toronto
        </h2>
        <p class="text-sm mt-1 mb-6 text-secondary-light">
          Filter by genre, date, and price to find your next show.
        </p>

        <!-- Genre -->
        <label class="block text-xs font-medium mb-1">GENRE</label>
        <select bind:value={selectedGenre} class="w-full mb-4">
          <option>All</option>
          {#each genres as genre}
            <option value={genre}>{genre}</option>
          {/each}
        </select>

        <!-- Dates -->
        <div class="flex gap-4 mb-4">
          <div class="flex-1">
            <label class="block text-xs font-medium mb-1">FROM</label>
            <input type="date" bind:value={fromDate} class="w-full" />
          </div>
          <div class="flex-1">
            <label class="block text-xs font-medium mb-1">TO</label>
            <input type="date" bind:value={toDate} class="w-full" />
          </div>
        </div>

        <!-- Price -->
        <label class="block text-xs font-medium mb-1">PRICE</label>
        <div class="flex items-center gap-3 mb-6">
          <input
            type="range"
            min="0"
            max="300"
            step="5"
            bind:value={maxPrice}
            class="flex-1 accent-primary"
          />
          <span class="w-16 text-right text-sm">${maxPrice}</span>
        </div>

        <!-- Button -->
        <button class="w-full bg-primary text-secondary font-semibold py-2 rounded-md" on:click={goToMap}>
          Explore
        </button>
      </div>
    </main>
  </div>
</div>

<style>
  img {
    transition: opacity 1s ease-in-out;
  }
</style>
