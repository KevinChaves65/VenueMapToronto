import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { Venue } from '../models/venues';

@Injectable({
    providedIn: 'root'
  })
  export class VenueService {
    private venuesUrl = 'assets/data/venues.json';
  
    constructor(private http: HttpClient) {}
  
    getVenues(): Observable<Venue[]> {
      return this.http.get<{ venues: Venue[] }>(this.venuesUrl).pipe(
        map(response => response.venues)
      );
    }
    getVenuesGeoJSON(): Observable<any> {
    return this.getVenues().pipe(
      map(venues => ({
        type: 'FeatureCollection',
        features: venues.map(venue => ({
          type: 'Feature',
          geometry: {
            type: 'Point',
            coordinates: [venue.longitude, venue.latitude]
          },
          properties: {
            id: venue.V_id,
            name: venue.venue,
            address: venue.address
          }
        }))
      }))
    );
  }
  }
