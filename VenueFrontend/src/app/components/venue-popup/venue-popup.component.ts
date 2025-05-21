import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Event } from '../../models/events';
import { EventService } from '../../services/event.service';
@Component({
  selector: 'app-venue-popup',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './venue-popup.component.html',
  styleUrl: './venue-popup.component.css'
})
export class VenuePopupComponent {
  @Input() venue!: any;
  @Input() events: Event[] = [];
  @Input() position: { x: number; y: number } | null = null;
  @Output() close = new EventEmitter<void>();
  showEvents = false;

  constructor(private eventService: EventService) {}

  viewEvents(): void {
    this.showEvents = !this.showEvents;

    if (this.showEvents && this.events.length === 0 && this.venue.eventIds?.length) {
      this.eventService.getEventsByIds(this.venue.eventIds).subscribe(events => {
        this.events = events;
      });
    }
  }
}
