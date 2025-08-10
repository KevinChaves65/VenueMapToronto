import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Artist } from '../models/artists';
import { Event } from '../models/events';
import { map, Observable, of } from 'rxjs';
import { environment } from '../../enviroments/environment'; 

@Injectable({ providedIn: 'root' })
export class ArtistService {
  private url = `${environment.apiBaseUrl}/artists`;
  private cachedArtists: Artist[] = [];

  constructor(private http: HttpClient) {}

  getArtists(): Observable<Artist[]> {
    if (this.cachedArtists.length > 0) {
      return of(this.cachedArtists);
    }

    return this.http.get<Artist[]>(this.url).pipe(
      map(response => {
        this.cachedArtists = response;
        return this.cachedArtists;
      })
    );
  }

  getArtistById(id: string): Observable<Artist | null> {
    return this.getArtists().pipe(
      map(artists => artists.find(artist => artist.A_id === id) || null)
    );
  }

  getEventsForArtist(artist: Artist, allEvents: Event[]): Event[] {
    return allEvents.filter(event => event.lineup.includes(artist.A_id));
  }
}