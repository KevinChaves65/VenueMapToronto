import { writable } from 'svelte/store';
import { getVenues } from '../services/venue.service';
import type { Venue } from '../models/venues';

export const venues = writable<Venue[]>([]);
export const isLoadingVenues = writable(false);
export const venueError = writable<string | null>(null);

export async function loadVenues() {
  try {
    isLoadingVenues.set(true);
    const data = await getVenues();
    venues.set(data);
  } catch (err) {
    venueError.set((err as Error).message);
  } finally {
    isLoadingVenues.set(false);
  }
}
