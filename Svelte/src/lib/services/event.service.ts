// src/lib/services/eventService.ts
import type { Event } from '../models/events';

const API_BASE_URL = 'http://localhost:3000';

let cachedEvents: Event[] = [];

/**
 * Fetch all events (with caching)
 */
export async function getEvents(): Promise<Event[]> {
  if (cachedEvents.length > 0) return cachedEvents;

  const res = await fetch(`${API_BASE_URL}/events`);
  if (!res.ok) throw new Error(`Failed to fetch events: ${res.status}`);

  cachedEvents = await res.json();
  return cachedEvents;
}

/**
 * Get a specific event by ID
 */
export async function getEventById(id: string): Promise<Event | null> {
  const events = await getEvents();
  return events.find(e => e.E_id === id) || null;
}

/**
 * Filter events by genre
 */
export async function getEventsByGenre(genre: string): Promise<Event[]> {
  const events = await getEvents();
  return events.filter(e => e.genre.toLowerCase() === genre.toLowerCase());
}

/**
 * Filter events by venue
 */
export async function getEventsByVenue(venueId: string): Promise<Event[]> {
  const events = await getEvents();
  return events.filter(e => e.V_id === venueId);
}

/**
 * Get upcoming events only (based on date)
 */
export async function getUpcomingEvents(): Promise<Event[]> {
  const events = await getEvents();
  const now = new Date();
  return events.filter(e => new Date(e.date) >= now);
}

/**
 * Clear cache manually (optional)
 */
export function clearEventCache() {
  cachedEvents = [];
}
