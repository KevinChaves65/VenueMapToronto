import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Artist } from '../models/artists';
import { Observable, map } from 'rxjs';
import { Event } from '../models/events';
import { EventService } from './event.service';

@Injectable({ providedIn: 'root' })
export class ArtistService {
  private url = 'assets/data/artist.json';

  constructor(private http: HttpClient, private eventService: EventService) {}

  getArtists(): Observable<Artist[]> {
    return this.http.get<{ artists: Artist[] }>(this.url).pipe(
      map(res => res.artists)
    );
  }

  getArtistById(A_id: number): Observable<Artist | undefined> {
    return this.getArtists().pipe(
      map(artists => artists.find(artist => artist.A_id === A_id))
    );
  }

  getEventsforArtist(artist: Artist): Observable<Event[]>{
    return this.eventService.getAllEvents().pipe(
      map(events =>
        events.filter(event => event.lineUp.includes(artist.name))
      )
    );
  }
}
