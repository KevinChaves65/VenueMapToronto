import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Event } from '../../../models/events';
import { EventService } from '../../../services/event.service';
import { EventCardComponent } from '../event-card/event-card.component';
import { FormsModule } from '@angular/forms';
import { Venue } from '../../../models/venues';

@Component({
  standalone: true,
  selector: 'app-event-list',
  imports: [CommonModule, EventCardComponent, FormsModule],
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

  constructor(private eventService: EventService) {}

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
    this.selectedEvent = event;
  }

  closeEvent = (): void => {
    this.selectedEvent = null;
  };
}
