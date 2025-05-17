import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VenueCardComponent } from '../side-bar-collection/venue-card/venue-card.component';
import { VenueService } from '../../services/venue.service';
import { EventService } from '../../services/event.service';
import { ArtistService } from '../../services/artist.service';
import { Venue } from '../../models/venues';
import { Event } from '../../models/events';
import { Artist } from '../../models/artists';
import { MatIcon } from '@angular/material/icon';
import { EventListComponent } from '../side-bar-collection/event-list/event-list.component';
import { ArtistListComponent } from "../side-bar-collection/artist-list/artist-list.component";
@Component({
  selector: 'app-side-bar',
  imports: [CommonModule, VenueCardComponent, MatIcon,EventListComponent, ArtistListComponent],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.css'
})
export class SideBarComponent implements OnInit {

  viewMode: 'venues' | 'events' | 'artists' = 'venues';

  venues: Venue[] = [];
  artists: Artist[] = [];
  events: Event[] = [];
  isCollapsed = false;

  venuesLoaded = false;
  eventsLoaded = false;
  artistsLoaded = false;

  toggleSidebar(): void {
    this.isCollapsed = !this.isCollapsed;
  }

  constructor(
    private venueService: VenueService,
    private artistService: ArtistService,
    private eventService: EventService
  ) {}
  setView(mode: 'venues' | 'events' | 'artists') {
  this.viewMode = mode;

  if (mode === 'venues' && !this.venuesLoaded) {
    this.venueService.getVenues().subscribe(v => {
      this.venues = v;
      this.venuesLoaded = true;
    });
  }

  if (mode === 'events' && !this.eventsLoaded) {
    this.eventService.getEvents().subscribe(e => {
      this.events = e;
      this.eventsLoaded = true;
    });
  }

  if (mode === 'artists' && !this.artistsLoaded) {
    this.artistService.getArtists().subscribe(a => {
      this.artists = a;
      this.artistsLoaded = true;
    });
  }
}


  ngOnInit(): void {
    this.venueService.getVenues().subscribe((data) => {
      this.venues = data;
    });
}
}

