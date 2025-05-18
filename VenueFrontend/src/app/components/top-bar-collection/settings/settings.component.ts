import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-settings',
  imports: [CommonModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.css'
})
export class SettingsComponent {
  selectedTheme: 'light' | 'dark' = 'dark';
  selectedMapStyle: 'dark' | 'streets' | 'satellite' = 'dark';
  autoCollapseSidebar: boolean = false;

  constructor() {}
}
