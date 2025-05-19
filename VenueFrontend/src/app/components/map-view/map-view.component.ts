import { Component, OnInit } from '@angular/core';
import { environment } from '../../../enviroments/enviroments';
import { CommonModule } from '@angular/common';
import { Venue } from '../../models/venues';
import { VenueService } from '../../services/venue.service';
import { Feature, Point } from 'geojson';
import { VenuePopupComponent } from '../venue-popup/venue-popup.component';
import * as mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

@Component({
  selector: 'app-map-view',
  standalone: true,
  imports: [VenuePopupComponent, CommonModule],
  templateUrl: './map-view.component.html',
  styleUrls: ['./map-view.component.css']
})
export class MapViewComponent implements OnInit {
  map!: mapboxgl.Map;
  venues: Venue[] = [];
  selectedVenue: any = null;
  selectedLngLat: [number, number] | null = null;
  popupPosition: { x: number, y: number } | null = null;

  constructor(private venueService: VenueService) {}

  initMap(): void {
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/dark-v10',
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

  updatePopupPosition(): void {
  if (this.selectedLngLat) {
    const point = this.map.project(this.selectedLngLat);
    this.popupPosition = { x: point.x, y: point.y };
  }
}

  ngOnInit(): void {
    this.initMap();

    this.map.on('load', () => {
      this.venueService.getVenuesGeoJSON().subscribe(geojson => {
        this.map.addSource('venues', {
          type: 'geojson',
          data: geojson
        });
///marker creation
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
        let hovered = false;
        this.map.on('mouseenter', 'venue-dots', (e) => {
          hovered = true;
          const feature = e.features?.[0] as Feature<Point>;
          const props = feature.properties;
          const coordinates = feature.geometry.coordinates as [number, number];

          this.selectedVenue = props;
        this.selectedLngLat = coordinates;
        this.updatePopupPosition();
        });
        this.map.on('click', (e) => {
          if (!hovered) {
            this.selectedVenue = null;
            this.selectedLngLat = null;
            this.popupPosition = null;
          }
          hovered = false;
        });

        this.map.on('move', () => this.updatePopupPosition());
        this.map.on('zoom', () => this.updatePopupPosition());
      });

      this.map.on('mouseenter', 'venue-dots', () => {
        this.map.getCanvas().style.cursor = 'pointer';
      });

      this.map.on('mouseleave', 'venue-dots', () => {
        this.map.getCanvas().style.cursor = '';
      });
    });
  }
}
