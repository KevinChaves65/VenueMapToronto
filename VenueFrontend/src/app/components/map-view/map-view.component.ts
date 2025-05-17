import { Component, OnInit } from '@angular/core';
import { environment } from '../../../enviroments/enviroments';
import { Venue } from '../../models/venues';
import { VenueService } from '../../services/venue.service';
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
  addVenueDot(): void {
  this.venues.forEach(venue => {
    new mapboxgl.Marker({ color: 'limegreen' }) 
      .setLngLat([venue.longitude, venue.latitude])
      .addTo(this.map);
  });
}
    ngOnInit(): void {
    this.initMap();

    this.venueService.getVenues().subscribe(data => {
      this.venues = data;
      this.addVenueDot();
    });
  }
}