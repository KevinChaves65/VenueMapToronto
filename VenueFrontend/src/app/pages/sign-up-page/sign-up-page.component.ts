import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-sign-up-page',
  imports: [CommonModule, FormsModule],
  templateUrl: './sign-up-page.component.html',
  styleUrl: './sign-up-page.component.css'
})
export class SignUpPageComponent {
  name = '';
  email = '';
  password = '';
  error = '';
/// Still need to connect to backend properly

  constructor(private auth: AuthService, private router: Router) {}

  register() {
    this.auth.register({ name: this.name, email: this.email, password: this.password }).subscribe({
      next: () => this.router.navigate(['/signin']),
      error: () => this.error = 'Registration failed. Try again.'
    });
  }
}
