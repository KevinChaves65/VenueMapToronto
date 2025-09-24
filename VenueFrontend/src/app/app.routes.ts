import { Routes } from '@angular/router';
import { EventCardComponent } from './components/side-bar-collection/event-card/event-card.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { MapPageComponent } from './pages/map-page/map-page.component';
import { AboutPageComponent } from './pages/about-page/about-page.component';

export const routes: Routes = [
    { path: 'events/:title', component: EventCardComponent},
    { path: '', component: LandingPageComponent },
    { path: 'map', component: MapPageComponent },
    { path: 'about', component: AboutPageComponent}
];
