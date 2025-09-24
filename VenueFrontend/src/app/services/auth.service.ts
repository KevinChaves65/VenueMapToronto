import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private API = '/api/auth'; // proxy to FastAPI

  constructor(private http: HttpClient) {}

  login(data: { email: string; password: string }) {
    return this.http.post(`${this.API}/login`, data);
  }

  register(data: { name: string; email: string; password: string }) {
    return this.http.post(`${this.API}/register`, data);
  }
}