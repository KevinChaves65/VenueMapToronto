import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VenueCardComponent } from './venue-card.component';

describe('VenueCardComponent', () => {
  let component: VenueCardComponent;
  let fixture: ComponentFixture<VenueCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VenueCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VenueCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
