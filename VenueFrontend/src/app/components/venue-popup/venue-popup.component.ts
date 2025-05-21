import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Event } from '../../models/events';
import { EventService } from '../../services/event.service';
import { EventCardComponent } from '../side-bar-collection/event-card/event-card.component';
@Component({
  selector: 'app-venue-popup',
  standalone: true,
  imports: [CommonModule, EventCardComponent],
  templateUrl: './venue-popup.component.html',
  styleUrl: './venue-popup.component.css'
})
export class VenuePopupComponent {
  @Input() venue!: any;
  @Input() events: Event[] = [];
  @Input() position: { x: number; y: number } | null = null;
  @Output() close = new EventEmitter<void>();
  showEvents = false;
  selectedEvent: Event | null = null;
  constructor(private eventService: EventService) {}

  viewEvents(): void {
    this.showEvents = !this.showEvents;

    if (this.showEvents && this.events.length === 0 && this.venue.eventIds?.length) {
      this.eventService.getEventsByIds(this.venue.eventIds).subscribe(events => {
        this.events = events;
      });
    }
  }

openEvent(event: Event): void {
  this.selectedEvent = event;
}

closeEvent = (): void => {
  this.selectedEvent = null;
};
}
