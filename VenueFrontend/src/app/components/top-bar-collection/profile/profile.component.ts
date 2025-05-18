import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
@Component({
  selector: 'app-profile',
  imports: [CommonModule, MatButtonModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {
emailNotifications: boolean = false;

  signIn() {
    alert('Sign-in feature coming soon!');
  }

  clearLocalData() {
    localStorage.clear();
    alert('Local data cleared');
  }

  viewUserEvents() {
    alert('Your Events feature coming soon!');
    // Future: navigate to a user's saved events or preferences
  }
}
