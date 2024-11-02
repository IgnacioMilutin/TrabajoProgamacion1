import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Libro } from '../libro.model';

@Injectable({
  providedIn: 'root',
})
export class LibrosService {
  private apiUrl = 'http://127.0.0.1:4567/libros';

  constructor(private http: HttpClient) {}

  getLibros(): Observable<{
    libros: Libro[];
    page: number;
    pages: number;
    total: number;
  }> {
    return this.http.get<{
      libros: Libro[];
      page: number;
      pages: number;
      total: number;
    }>(this.apiUrl);
  }
}
