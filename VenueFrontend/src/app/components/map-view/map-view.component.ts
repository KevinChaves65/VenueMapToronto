import { Component, AfterViewInit } from '@angular/core';
import { environment } from '../../../enviroments/enviroments';
import { Venue } from '../../models/venues';
import { VenueService } from '../../services/venue.service';
import * as mapboxgl from 'mapbox-gl';
import "mapbox-gl/dist/mapbox-gl.css";
@Component({
  selector: 'app-map-view',
  imports: [],
  templateUrl: './map-view.component.html',
  styleUrl: './map-view.component.css'
})
export class MapViewComponent implements AfterViewInit {

  map!: mapboxgl.Map;

  ngAfterViewInit(): void {

    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/arceodan/cmad61o0800ar01s81b842d6a', // basic 3D style
      center: [-79.483006, 43.665544], 
      zoom: 18, 
      pitch: 45, // tilts map 45 degrees
      bearing: -17.6, // rotates map for dynamic view
      accessToken: environment.mapboxToken
    });

    this.map.on('load', () => {
      this.map.setTerrain({
        source: 'mapbox-dem',
        exaggeration: 1.5 // exaggerate terrain height
      });
    })
  }
}