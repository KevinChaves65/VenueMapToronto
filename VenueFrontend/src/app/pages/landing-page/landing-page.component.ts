import { Component, computed, signal, effect, ChangeDetectionStrategy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-landing-page',
  imports: [CommonModule, FormsModule],
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LandingPageComponent {

  readonly images = ['concert1.jpg', 'concert2.jpg', 'concert3.jpg', 
  'concert4.jpg','concert5.jpg', 'concert6.jpg', 'concert7.jpg', 'concert8.jpg', 'concert9.jpg'];

  readonly genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Electronic', 'Classical'];

  maxPrice = 300;
  private index = signal(0);

  // Expose index via computed for template binding
  currentIndex = computed(() => this.index());

  constructor(private router: Router) {
    // Auto-advance every 6 seconds
    if (typeof window !== 'undefined') {
  setInterval(() => {
    this.index.update(i => (i + 1) % this.images.length);
  }, 6000);
}
  }
  goToMap() {
    this.router.navigate(['/map']);
  }
}
