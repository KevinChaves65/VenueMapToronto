import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Venue } from '../../../models/venues';
import { Event } from '../../../models/events';
import { EventService } from '../../../services/event.service';
import { EventCardComponent } from '../event-card/event-card.component';
import { MapService } from '../../../services/map.service';


@Component({
  selector: 'app-venue-card',
  standalone: true,
  imports: [CommonModule, EventCardComponent],
  templateUrl: './venue-card.component.html',
  styleUrls: ['./venue-card.component.css']
})
export class VenueCardComponent  {
  @Input() venue!: Venue;
  @Output() eventSelected = new EventEmitter<Event>();

  events: Event[] = [];
  showEvents: boolean = false;
  selectedEvent: Event | null = null;
  eventsLoaded = false;

  constructor(private eventService: EventService, private mapService: MapService) {}

  centerMapOnVenue(venue: Venue): void {
  this.mapService.flyTo(venue.longitude, venue.latitude);
  }

  toggleEvents(): void {
    this.showEvents = !this.showEvents;

    if (this.showEvents && !this.eventsLoaded && this.venue?.eventIds?.length) {
      this.eventService.getEventsByIds(this.venue.eventIds).subscribe(events => {
        this.events = events;
        this.eventsLoaded = true;
      });
    }

    this.selectedEvent = null;
  }
  openEvent(event: Event): void {
    this.eventSelected.emit(event);
  }

  closeEvent = (): void => {
    this.selectedEvent = null;
  };
}
