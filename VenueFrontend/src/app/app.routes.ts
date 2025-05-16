import { Routes } from '@angular/router';
import { EventCardComponent } from './components/side-bar-collection/event-card/event-card.component';

export const routes: Routes = [
    {path: 'events/:title', component: EventCardComponent}
];
