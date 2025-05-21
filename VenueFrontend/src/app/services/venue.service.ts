import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { Venue } from '../models/venues';

@Injectable({
    providedIn: 'root'
  })
  export class VenueService {
    private venuesUrl = 'assets/data/venues.json';
    private cachedVenues: Venue[] = [];
    constructor(private http: HttpClient) {}
  
    getVenues(): Observable<Venue[]> {
  if (this.cachedVenues.length > 0) {
    return new Observable(observer => {
      observer.next(this.cachedVenues);
      observer.complete();
    });
  }

  return this.http.get<{ venues: Venue[] }>(this.venuesUrl).pipe(
    map(response => {
      this.cachedVenues = response.venues;
      return this.cachedVenues;
    })
  );
}
    getVenueCoordinatesById(venueId: string): [number, number] | null {
  const venue = this.cachedVenues.find(v => v.V_id === venueId);
  return venue && venue.latitude !== undefined && venue.longitude !== undefined
    ? [venue.longitude, venue.latitude]
    : null;
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
          V_id: venue.V_id,
          venue: venue.venue,
          imageUrl: venue.imageUrl,
          address: venue.address,
          eventIds: venue.eventIds
          }
        }))
      }))
    );
  }
  }
