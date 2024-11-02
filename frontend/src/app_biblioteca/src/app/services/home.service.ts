import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class HomeService {
  private apiUrl = '/api/libros'; // Ruta relativa usando el proxy

  constructor(private http: HttpClient) {}

  getLibros(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
