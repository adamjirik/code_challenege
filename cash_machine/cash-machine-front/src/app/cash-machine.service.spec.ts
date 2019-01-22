import { TestBed } from '@angular/core/testing';

import { CashMachineService } from './cash-machine.service';

describe('CashMachineService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CashMachineService = TestBed.get(CashMachineService);
    expect(service).toBeTruthy();
  });
});
