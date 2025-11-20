// src/lib/services/artistService.ts
import type { Artist } from '../models/artists';
import type { Event } from '../models/events';

const API_BASE_URL = 'http://localhost:3000';

let cachedArtists: Artist[] = [];

export async function getArtists(): Promise<Artist[]> {
  if (cachedArtists.length > 0) return cachedArtists;

  const res = await fetch(`${API_BASE_URL}/artists`);
  if (!res.ok) throw new Error(`Failed to fetch artists: ${res.status}`);

  cachedArtists = await res.json();
  return cachedArtists;
}


export async function getArtistById(id: string): Promise<Artist | null> {
  const artists = await getArtists();
  return artists.find(a => a.A_id === id) || null;
}

export function getEventsForArtist(artist: Artist, allEvents: Event[]): Event[] {
  return allEvents.filter(e => e.lineup.includes(artist.A_id));
}
export function clearArtistCache() {
  cachedArtists = [];
}
