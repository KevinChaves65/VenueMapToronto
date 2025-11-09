import { writable } from 'svelte/store';
import { getArtists } from '../services/artist.service';
import type { Artist } from '../models/artists';

export const artists = writable<Artist[]>([]);
export const isLoading = writable(false);
export const error = writable<string | null>(null);

export async function loadArtists() {
  try {
    isLoading.set(true);
    const data = await getArtists();
    artists.set(data);
  } catch (err) {
    error.set((err as Error).message);
  } finally {
    isLoading.set(false);
  }
}
