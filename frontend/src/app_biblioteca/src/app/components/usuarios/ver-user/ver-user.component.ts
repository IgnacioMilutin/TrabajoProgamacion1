import { Component } from '@angular/core';

@Component({
  selector: 'app-ver-user',
  templateUrl: './ver-user.component.html',
  styleUrl: './ver-user.component.css',
})
export class VerUserComponent {
  arrayUsuarios = [
    {
      id: 1,
      nombre: 'Usuario 1',
    },
    {
      id: 2,
      nombre: 'Usuario 2',
    },
    {
      id: 3,
      nombre: 'Usuario 3',
    },
    {
      id: 4,
      nombre: 'Usuario 4',
    },
    {
      id: 5,
      nombre: 'Usuario 5',
    },
  ];
}
