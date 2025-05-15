import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-top-bar',
  imports: [CommonModule, MatButtonModule, MatIconModule],
  templateUrl: './top-bar.component.html',
  styleUrl: './top-bar.component.css'
})
export class TopBarComponent {
activePanel: 'social' | 'settings' | 'account' | null = null;

  togglePanel(panel: 'social' | 'settings' | 'account'): void {
    this.activePanel = this.activePanel === panel ? null : panel;
  }
}
