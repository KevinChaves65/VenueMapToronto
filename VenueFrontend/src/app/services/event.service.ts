import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Event } from '../models/events';
import { map, Observable, of } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class EventService {
  private eventsUrl = 'http://localhost:8000/events'; // Or use environment.apiUrl
  private cachedEvents: Event[] = [];

  constructor(private http: HttpClient) {}

  getEvents(): Observable<Event[]> {
    if (this.cachedEvents.length > 0) {
      return of(this.cachedEvents);
    }

    return this.http.get<Event[]>(this.eventsUrl).pipe(
      map(response => {
        this.cachedEvents = response;
        return this.cachedEvents;
      })
    );
  }

  getEventById(id: string): Observable<Event | null> {
    return this.getEvents().pipe(
      map(events => events.find(event => event.E_id === id) || null)
    );
  }

  getEventsByIds(ids: string[]): Observable<Event[]> {
    return this.getEvents().pipe(
      map(events => events.filter(event => ids.includes(event.E_id)))
    );
  }

  getEventBySlug(slug: string): Observable<Event | null> {
    return this.getEvents().pipe(
      map(events => events.find(event =>
        event.name.toLowerCase().replace(/\s+/g, '-') === slug.toLowerCase()
      ) || null)
    );
  }
}