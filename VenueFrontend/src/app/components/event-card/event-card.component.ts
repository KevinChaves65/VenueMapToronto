import { Component, Inject, Input, Optional} from '@angular/core';
import { CommonModule } from '@angular/common';
import { Event } from '../../models/events';
import { MAT_DIALOG_DATA, MatDialog } from '@angular/material/dialog';
import { ArtistService } from '../../services/artist.service';
import { ArtistCardComponent } from '../artist-card/artist-card.component';
import { Artist } from '../../models/artists';
import { MatCardActions } from '@angular/material/card';
@Component({
  selector: 'app-event-card',
  imports: [CommonModule, MatCardActions],
  templateUrl: './event-card.component.html',
  styleUrl: './event-card.component.css'
})
export class EventCardComponent {
  
  @Input() event!: Event;
  @Input() fallbackImageUrl: string = '';
  @Input() close: () => void = () => {};
  constructor(
    private dialog: MatDialog,
    private artistService: ArtistService,
    @Optional() @Inject(MAT_DIALOG_DATA) public dialogData: any
  ) {}
  ngOnInit() {
    // If event/fallbackImageUrl not passed via @Input, use dialog data
    if (this.dialogData) {
      this.event = this.dialogData.event;
      this.fallbackImageUrl = this.dialogData.fallbackImageUrl || '';
    }
  }

  openArtistModal(artistName: string): void {
    this.artistService.getArtists().subscribe((artists: Artist[]) => {
      const match = artists.find(a => a.name.toLowerCase() === artistName.toLowerCase());
      if (match) {
        this.dialog.open(ArtistCardComponent, {
          width: '500px',
          data: { artist: match }
        });
      }
    });
  }
}