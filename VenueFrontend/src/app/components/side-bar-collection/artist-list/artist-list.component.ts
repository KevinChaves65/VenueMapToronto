import { Component, OnInit } from '@angular/core';
import { ArtistService } from '../../../services/artist.service';
import { Artist } from '../../../models/artists';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ArtistCardComponent } from '../artist-card/artist-card.component';
import { MatDialog } from '@angular/material/dialog';
@Component({
  standalone: true,
  selector: 'app-artist-list',
  imports: [CommonModule, FormsModule],
  templateUrl: './artist-list.component.html',
  styleUrls: ['./artist-list.component.css']
})
export class ArtistListComponent implements OnInit {
allArtists: Artist[] = [];
  filteredArtists: Artist[] = [];

  searchTerm = '';
  selectedGenre = '';
  genres: string[] = [];

  constructor(private artistService: ArtistService, private dialog: MatDialog) {}

ngOnInit(): void {
  this.artistService.getArtists().subscribe(artists => {
    console.log('Loaded artists:', artists); 
    this.allArtists = artists;
    this.genres = [...new Set(artists.map(a => a.genre))];
    this.applyFilters();
  });
}

  applyFilters(): void {
    this.filteredArtists = this.allArtists.filter(artist =>
      (!this.selectedGenre || artist.genre === this.selectedGenre) &&
      (!this.searchTerm || artist.name.toLowerCase().includes(this.searchTerm.toLowerCase()))
    );
  }
  openArtistModal(artist: Artist): void {
    this.dialog.open(ArtistCardComponent, {
      width: '500px',
      data: { artist }
    });
  }
}
