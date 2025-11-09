import { writable } from 'svelte/store';

// This is a generic type. Replace `any` with your map library's map instance type,
// e.g., mapboxgl.Map or L.Map
type MapInstance = any;

export const mapInstance = writable<MapInstance>(null);

/**
 * A helper function to fly to a specific location on the map.
 *for plotting points 
 * @param longitude
 * @param latitude
 */
export function flyTo(longitude: number, latitude: number) {
	mapInstance.subscribe((map) => {
		map?.flyTo({ center: [longitude, latitude], zoom: 15 });
	})();
}