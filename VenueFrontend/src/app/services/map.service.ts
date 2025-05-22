import { Injectable } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';

@Injectable({ providedIn: 'root' })
export class MapService {
  private map!: mapboxgl.Map;

  setMap(map: mapboxgl.Map): void {
    this.map = map;
  }
  flyTo(lng: number, lat: number): void {
    if (this.map) {
      this.map.flyTo({
        center: [lng, lat],
        zoom: 15,
        speed: 1.2,
        curve: 1.42,
        essential: true
      });
    }
  }
}