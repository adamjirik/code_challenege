import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CashMachineComponent } from './cash-machine.component';

describe('CashMachineComponent', () => {
  let component: CashMachineComponent;
  let fixture: ComponentFixture<CashMachineComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CashMachineComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CashMachineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
