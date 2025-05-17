import { Component, OnInit } from '@angular/core';
import { environment } from '../../../enviroments/enviroments';
import { Venue } from '../../models/venues';
import { VenueService } from '../../services/venue.service';
import { Feature, Point } from 'geojson';
import * as mapboxgl from 'mapbox-gl';
import "mapbox-gl/dist/mapbox-gl.css";
@Component({
  selector: 'app-map-view',
  imports: [],
  templateUrl: './map-view.component.html',
  styleUrls: ['./map-view.component.css']
})
export class MapViewComponent implements OnInit {

  map!: mapboxgl.Map;
  venues: Venue [] = [];

  constructor(private venueService: VenueService) {}

  initMap(): void {
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/dark-v10', // no building labels style
      center: [-79.407552, 43.652150], 
      zoom: 13, 
      pitch: 45, 
      bearing: -17.6, 
      accessToken: environment.mapboxToken
    });

    this.map.on('load', () => {
    this.map.addSource('mapbox-dem', {
    type: 'raster-dem',
    url: 'mapbox://mapbox.terrain-rgb',
    tileSize: 512,
    maxzoom: 14
  });

  this.map.setTerrain({ source: 'mapbox-dem', exaggeration: 1.5 });
});
  }
    ngOnInit(): void {
    this.initMap();

    this.map.on('load', () => {
      this.venueService.getVenuesGeoJSON().subscribe(geojson => {
        // Add venue GeoJSON source
        this.map.addSource('venues', {
          type: 'geojson',
          data: geojson
        });

        // Add green circle layer
        this.map.addLayer({
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

        // Click: popup
        this.map.on('click', 'venue-dots', (e) => {
          const feature = e.features?.[0] as Feature<Point>;
          const geometry = feature.geometry as Point;
          const coordinates = geometry.coordinates as [number, number];
          const name = feature.properties?.['name'];

          if (coordinates && name) {
            new mapboxgl.Popup()
              .setLngLat(coordinates)
              .setHTML(`<strong>${name}</strong>`)
              .addTo(this.map);
          }
        });

        // Change on hover
        this.map.on('mouseenter', 'venue-dots', () => {
          this.map.getCanvas().style.cursor = 'pointer';
        });

        this.map.on('mouseleave', 'venue-dots', () => {
          this.map.getCanvas().style.cursor = '';
        });
      });
    });
  }
}