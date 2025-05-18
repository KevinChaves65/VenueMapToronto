import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-venue-popup',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './venue-popup.component.html',
  styleUrl: './venue-popup.component.css'
})
export class VenuePopupComponent {
  @Input() venue!: any;
  @Input() position: { x: number; y: number } | null = null;
  @Output() close = new EventEmitter<void>();
  viewEvents() {
}
}
