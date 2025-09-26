import { Routes } from '@angular/router';
import { EventCardComponent } from './components/side-bar-collection/event-card/event-card.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { MapPageComponent } from './pages/map-page/map-page.component';
import { SignInPageComponent } from './pages/sign-in-page/sign-in-page.component';
import { SignUpPageComponent } from './pages/sign-up-page/sign-up-page.component';
import { AboutPageComponent } from './pages/about-page/about-page.component';

export const routes: Routes = [
    { path: 'events/:title', component: EventCardComponent},
    { path: '', component: LandingPageComponent },
    { path: 'map', component: MapPageComponent },
    { path: 'signin', component: SignInPageComponent },
    { path: 'signup', component: SignUpPageComponent },
    { path: 'about', component: AboutPageComponent }
];
