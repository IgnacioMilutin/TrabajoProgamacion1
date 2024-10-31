import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PrestamosService } from '../../services/prestamos.service';

@Component({
  selector: 'app-prestamos',
  templateUrl: './prestamos.component.html',
  styleUrl: './prestamos.component.css',
})
export class PrestamosComponent {
  searchQuery = '';
  arrayPrestamos: any[] = [];
  filteredLoans: any[] = [];

  constructor(
    private router: Router,
    private prestamosService: PrestamosService
  ) {}
  ngOnInit() {
    this.prestamosService.getLoans().subscribe((rta: any) => {
      console.log('prestamos api: ', rta);
      this.arrayPrestamos = rta.prestamos || [];
      this.filteredLoans = [...this.arrayPrestamos];
    });
  }
  editarprestamos(loan: any) {
    console.log('Estoy editando', loan);
    this.router.navigate(['/prestamos/' + loan.id + '/Editar']);
  }
  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredLoans = this.arrayPrestamos.filter((loan) =>
      loan.nombreapellido.includes(this.searchQuery)
    );
  }
}
