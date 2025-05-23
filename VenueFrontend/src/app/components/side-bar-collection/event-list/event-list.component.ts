import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Event } from '../../../models/events';
import { EventService } from '../../../services/event.service';
import { FormsModule } from '@angular/forms';
import { Venue } from '../../../models/venues';
import { VenueService } from '../../../services/venue.service';
import { MapService } from '../../../services/map.service';

@Component({
  standalone: true,
  selector: 'app-event-list',
  imports: [CommonModule, FormsModule],
  templateUrl: './event-list.component.html',
  styleUrl: './event-list.component.css'
})
export class EventListComponent implements OnInit {
  venue: Venue[] =[]
  allEvents: Event[] = [];
  filteredEvents: Event[] = [];

  searchTerm = '';
  selectedGenre = '';
  selectedEvent: Event | null = null;
  genres: string[] = [];
  @Output() eventSelected = new EventEmitter<Event>();

  constructor(
  private eventService: EventService, 
  private mapService: MapService,
  private venueService: VenueService) {}

  ngOnInit(): void {
    this.eventService.getEvents().subscribe(events => {
      this.allEvents = events;
      this.genres = [...new Set(events.map(e => e.genre))];
      this.applyFilters();
    });
  }

  applyFilters(): void {
    this.filteredEvents = this.allEvents.filter(event =>
      (!this.selectedGenre || event.genre === this.selectedGenre) &&
      (!this.searchTerm || event.name.toLowerCase().includes(this.searchTerm.toLowerCase()))
    );
  }
  openEvent(event: Event): void {
  this.eventSelected.emit(event);
}

closeEvent = (): void => {
  this.selectedEvent = null;
  document.body.style.overflow = '';
};
  centerMapOnEvent(event: Event): void {
  const coords = this.venueService.getVenueCoordinatesById(event.VenueId);
  if (coords) {
    this.mapService.flyTo(coords[0], coords[1]);
  }
}
}
