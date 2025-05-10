import { Component, Inject, OnInit } from '@angular/core';
import { Artist } from '../../models/artists';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { Event } from '../../models/events';
import { EventService } from '../../services/event.service';
import { ArtistService } from '../../services/artist.service';
@Component({
  selector: 'app-artist-card',
  imports: [CommonModule, MatButtonModule, MatCardModule, MatDialogModule],
  templateUrl: './artist-card.component.html',
  styleUrl: './artist-card.component.css'
})
export class ArtistCardComponent implements OnInit {
  events: Event[] = [];
  artist!: Artist;

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: { artist: Artist },
    private artistService: ArtistService
  ) {
    this.artist = data.artist;
  }
  ngOnInit(): void {
    this.artistService.getEventsforArtist(this.artist).subscribe(events => {
      this.events = events;
    });
  }
}
