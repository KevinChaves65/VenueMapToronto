// src/lib/services/venueService.ts
import type { Venue } from '../models/venues';

const API_BASE_URL = 'http://localhost:3000';

let cachedVenues: Venue[] = [];

/**
 * Fetch all venues (with caching)
 */
export async function getVenues(): Promise<Venue[]> {
  if (cachedVenues.length > 0) return cachedVenues;

  const res = await fetch(`${API_BASE_URL}/venues`);
  if (!res.ok) throw new Error(`Failed to fetch venues: ${res.status}`);

  cachedVenues = await res.json();
  return cachedVenues;
}

/**
 * Get venue coordinates by ID
 */
export function getVenueCoordinatesById(venueId: string): [number, number] | null {
  const venue = cachedVenues.find(v => v.V_id === venueId);
  return venue && venue.latitude !== undefined && venue.longitude !== undefined
    ? [venue.longitude, venue.latitude]
    : null;
}

/**
 * Generate GeoJSON structure for map use
 */
export async function getVenuesGeoJSON(): Promise<any> {
  const venues = await getVenues();

  return {
    type: 'FeatureCollection',
    features: venues.map(v => ({
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: [v.longitude, v.latitude]
      },
      properties: {
        V_id: v.V_id,
        name: v.name,
        vimage: v.vimage,
        address: v.address,
        eventIds: v.eventIds
      }
    }))
  };
}

/**
 * Clear cache manually (optional)
 */
export function clearVenueCache() {
  cachedVenues = [];
}
