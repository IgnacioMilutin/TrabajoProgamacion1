import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  libros: any[] = []; // Lista de libros obtenidos desde el backend

  constructor(private homeService: HomeService) {}

  ngOnInit(): void {
    this.obtenerLibros();
  }

  obtenerLibros(): void {
    this.homeService.getLibros().subscribe(
      (data: any) => {
        this.libros = data; // Asignar la lista de libros recibida a la variable `libros`
      },
      (error) => {
        console.error('Error al obtener libros:', error);
      }
    );
  }
}
