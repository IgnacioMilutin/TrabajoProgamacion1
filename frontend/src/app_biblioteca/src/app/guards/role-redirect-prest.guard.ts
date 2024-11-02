import { CanActivateFn } from '@angular/router';

export const roleRedirectPrestGuard: CanActivateFn = (route, state) => {
  return true;
};
