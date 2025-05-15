import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VenueCardComponent } from '../venue-card/venue-card.component';
import { VenueService } from '../../services/venue.service';
import { Venue } from '../../models/venues';
import { MatIcon } from '@angular/material/icon';
@Component({
  selector: 'app-side-bar',
  imports: [CommonModule, VenueCardComponent, MatIcon],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.css'
})
export class SideBarComponent implements OnInit {
  venues: Venue[] = [];
  isCollapsed = false;

  toggleSidebar(): void {
    this.isCollapsed = !this.isCollapsed;
  }

  constructor(private venueService: VenueService) {}

  ngOnInit(): void {
    this.venueService.getVenues().subscribe((data) => {
      console.log('Fetched venues:', data);
      this.venues = data;
    });
}
}

