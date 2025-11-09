// src/lib/stores/events.ts
import { writable } from 'svelte/store';
import { getEvents } from '../services/event.service';
import type { Event } from '../models/events';

export const events = writable<Event[]>([]);
export const isLoadingEvents = writable(false);
export const eventError = writable<string | null>(null);

export async function loadEvents() {
  try {
    isLoadingEvents.set(true);
    const data = await getEvents();
    events.set(data);
  } catch (err) {
    eventError.set((err as Error).message);
  } finally {
    isLoadingEvents.set(false);
  }
}
