import { Component, ChangeDetectionStrategy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SideBarComponent } from "../../components/side-bar/side-bar.component";
import { TopBarComponent } from "../../components/top-bar/top-bar.component";
import { MapViewComponent } from "../../components/map-view/map-view.component";

@Component({
  selector: 'app-map-page',
  standalone: true,
  imports: [CommonModule, SideBarComponent, TopBarComponent, MapViewComponent],
  templateUrl: './map-page.component.html',
  styleUrl: './map-page.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class MapPageComponent {

}
