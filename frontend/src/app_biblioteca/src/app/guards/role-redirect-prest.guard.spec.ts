import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { roleRedirectPrestGuard } from './role-redirect-prest.guard';

describe('roleRedirectPrestGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => roleRedirectPrestGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
