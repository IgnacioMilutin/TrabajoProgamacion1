import { Component } from '@angular/core';
import { Libro } from '../../libro.model';
import { LibrosService } from '../../services/libros.service';

@Component({
  selector: 'app-libros',
  templateUrl: './libros.component.html',
  styleUrl: './libros.component.css',
})
export class LibrosComponent {
  libros: Libro[] = [];

  constructor(private librosService: LibrosService) {}

  ngOnInit(): void {
    this.librosService.getLibros().subscribe(
      (response) => {
        this.libros = response.libros;
        console.log(this.libros); // Verifica que los datos se están cargando
      },
      (error) => {
        console.error('Error al cargar los libros:', error); // Log de errores en caso de que haya un fallo en la API
      }
    );
  }
}
