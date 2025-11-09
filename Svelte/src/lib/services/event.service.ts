import type { Event } from '../models/events';

const API_BASE_URL = 'http://localhost:8000';

/**
 * Fetches all events from the API.
 */
export async function getEvents(): Promise<Event[]> {
	const response = await fetch(`${API_BASE_URL}/events`);
	if (!response.ok) {
		throw new Error('Failed to fetch events');
	}
	return await response.json();
}

/**
 * Fetches a selection of events by their IDs.
 */
export async function getEventsByIds(ids: string[]): Promise<Event[]> {
	const response = await fetch(`${API_BASE_URL}/events?ids=${ids.join(',')}`);
	if (!response.ok) {
		throw new Error('Failed to fetch events by IDs');
	}
	return await response.json();
}