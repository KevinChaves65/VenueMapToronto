import { Component, ElementRef, HostListener, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { AboutComponent } from '../top-bar-collection/about/about.component';
import { ProfileComponent } from '../top-bar-collection/profile/profile.component';
import { SettingsComponent } from '../top-bar-collection/settings/settings.component';

@Component({
  selector: 'app-top-bar',
  imports: [CommonModule, MatButtonModule, MatIconModule, AboutComponent, SettingsComponent, ProfileComponent],
  templateUrl: './top-bar.component.html',
  styleUrl: './top-bar.component.css'
})
export class TopBarComponent implements OnDestroy{
activePanel: 'social' | 'settings' | 'account' | null = null;
constructor(private eRef: ElementRef) {}

  togglePanel(panel: 'social' | 'settings' | 'account'): void {
    this.activePanel = this.activePanel === panel ? null : panel;
  }
  @HostListener('document:click', ['$event'])
  handleOutsideClick(event: MouseEvent): void {
    if (!this.eRef.nativeElement.contains(event.target)) {
      this.activePanel = null;
    }
  }

  ngOnDestroy(): void {
    // optional cleanup if needed later
  }
}
