import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SideBarComponent } from './components/side-bar/side-bar.component';
import { MapViewComponent } from './components/map-view/map-view.component';
import { TopBarComponent } from './components/top-bar/top-bar.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, SideBarComponent, MapViewComponent, TopBarComponent, LandingPageComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Showfari';
}
