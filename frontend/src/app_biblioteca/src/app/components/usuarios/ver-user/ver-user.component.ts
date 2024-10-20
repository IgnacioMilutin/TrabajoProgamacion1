import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ver-user',
  templateUrl: './ver-user.component.html',
  styleUrl: './ver-user.component.css',
})
export class VerUserComponent {
  searchQuery = '';
  arrayUsuarios = [
    {
      id: 1,
      nombre: 'Ignacio',
    },
    {
      id: 2,
      nombre: 'Matias',
    },
    {
      id: 3,
      nombre: 'Santiago',
    },
    {
      id: 4,
      nombre: 'Gino',
    },
    {
      id: 5,
      nombre: 'Usuario 5',
    },
  ];
  filteredUsers = [...this.arrayUsuarios];

  constructor(private router: Router) {}
  editarusuario(user: any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/usuario/' + user.id + '/Editar']);
  }
  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredUsers = this.arrayUsuarios.filter((user) =>
      user.nombre.includes(this.searchQuery)
    );
  }
}
