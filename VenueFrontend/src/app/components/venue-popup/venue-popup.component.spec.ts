import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VenuePopupComponent } from './venue-popup.component';

describe('VenuePopupComponent', () => {
  let component: VenuePopupComponent;
  let fixture: ComponentFixture<VenuePopupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VenuePopupComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VenuePopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
