import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';
// import { decode } from 'jwt-decode';
@Injectable({
  providedIn: 'root',
})
export class AuthService {
  url = '/api';
  constructor(private httpClient: HttpClient, private router: Router) {}

  login(dataLogin: any): Observable<any> {
    // let dataLogin = {
    //   mail: 'sb.escuderini@gmail.com',
    //   password: '1234',
    // };
    return this.httpClient
      .post(this.url + '/auth/login', dataLogin)
      .pipe(take(1));
  }

  register(dataRegistro: any): Observable<any> {
    // let dataLogin = {
    //   mail: 'sb.escuderini@gmail.com',
    //   password: '1234',
    // };
    return this.httpClient
      .post(this.url + '/auth/signin', dataRegistro)
      .pipe(take(1));
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('home');
  }

  //   getUserDetails() {
  //     const token = localStorage.getItem('token');
  //     if (token) {
  //       const decodedToken: any = decode(token);
  //       return { role: decodedToken.role, id_usuario: decodedToken.id_usuario };
  //     }
  //     return null;
  //   }
}
