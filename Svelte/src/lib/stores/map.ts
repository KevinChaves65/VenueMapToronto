import { writable, get } from 'svelte/store';
import mapboxgl from 'mapbox-gl';
import { getVenuesGeoJSON } from '$lib/services/venue.service';
import { env } from '$env/dynamic/public';

// --- Writable Stores ---
export const map = writable<mapboxgl.Map | null>(null);
export const selectedVenue = writable<any>(null);
export const popupPosition = writable<{ x: number; y: number } | null>(null);
export const selectedLngLat = writable<[number, number] | null>(null);

// --- Initialize the map ---
export async function initMap(containerId: string) {
  mapboxgl.accessToken = 'pk.eyJ1IjoiYXJjZW9kYW4iLCJhIjoiY205cm91dzRuMDNsbDJscTJqNHJ0bGhwbSJ9.XNBPCiKK8SsdTeZxldYsdA';

  const mapInstance = new mapboxgl.Map({
    container: containerId,
    style: 'mapbox://styles/mapbox/dark-v10',
    center: [-79.407552, 43.65215],
    zoom: 13,
    pitch: 45,
    bearing: -17.6
  });

  map.set(mapInstance);

  mapInstance.on('load', async () => {
    // Terrain setup
    mapInstance.addSource('mapbox-dem', {
      type: 'raster-dem',
      url: 'mapbox://mapbox.terrain-rgb',
      tileSize: 512,
      maxzoom: 14
    });

    mapInstance.setTerrain({ source: 'mapbox-dem', exaggeration: 1.5 });

    // Load and render venues
    const geojson = await getVenuesGeoJSON();

    mapInstance.addSource('venues', {
      type: 'geojson',
      data: geojson
    });

    mapInstance.addLayer({
      id: 'venue-dots',
      type: 'circle',
      source: 'venues',
      paint: {
        'circle-radius': 6,
        'circle-color': '#00FF00',
        'circle-stroke-width': 2,
        'circle-stroke-color': '#ffffff'
      }
    });

    setupInteractions(mapInstance);
  });

  return mapInstance;
}

// --- Interaction Logic ---
function setupInteractions(mapInstance: mapboxgl.Map) {
  let hovered = false;

  mapInstance.on('mouseenter', 'venue-dots', (e) => {
    hovered = true;
    const feature = e.features?.[0];
    if (!feature) return;

    const coords = feature.geometry.coordinates as [number, number];
    selectedVenue.set(feature.properties);
    selectedLngLat.set(coords);
    updatePopupPosition(mapInstance);
  });

  mapInstance.on('click', () => {
    if (!hovered) {
      selectedVenue.set(null);
      selectedLngLat.set(null);
      popupPosition.set(null);
    }
    hovered = false;
  });

  mapInstance.on('move', () => updatePopupPosition(mapInstance));
  mapInstance.on('zoom', () => updatePopupPosition(mapInstance));

  mapInstance.on('mouseenter', 'venue-dots', () => {
    mapInstance.getCanvas().style.cursor = 'pointer';
  });

  mapInstance.on('mouseleave', 'venue-dots', () => {
    mapInstance.getCanvas().style.cursor = '';
  });

  // Double-click zoom
  mapInstance.on('dblclick', (e) => {
    const features = mapInstance.queryRenderedFeatures(e.point, {
      layers: ['venue-dots']
    });

    if (features.length > 0) {
      const coords = (features[0].geometry as any).coordinates as [number, number];
      mapInstance.flyTo({
        center: coords,
        zoom: mapInstance.getZoom() + 5,
        speed: 1.2,
        curve: 1.42,
        essential: true
      });
    }
  });
}

// --- Helper ---
function updatePopupPosition(mapInstance: mapboxgl.Map) {
  const lngLat = get(selectedLngLat);
  if (lngLat) {
    const point = mapInstance.project(lngLat);
    popupPosition.set({ x: point.x, y: point.y });
  }
}
export function removeMap() {
  const m = get(map);
  if (m) {
    m.remove();
    map.set(null);
  }
}
