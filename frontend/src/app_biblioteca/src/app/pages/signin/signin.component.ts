import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css'],
})
export class SigninComponent {
  signinForm!: FormGroup;

  constructor(
    private authService: AuthService,
    private router: Router,
    private formBuilder: FormBuilder
  ) {
    this.signinForm = this.formBuilder.group({
      nombreapellido: ['', Validators.required],
      mail: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(4)]],
      telefono: [, Validators.required],
      dni: [, Validators.required],
      activo: [true, Validators.required],
      role: ['user', Validators.required],
    });
  }

  irAlRegistro(dataRegistro: any) {
    this.authService.register(dataRegistro).subscribe({
      next: (rta: any) => {
        alert('Registro exitoso!');
        console.log('Éxito: ', rta);
        localStorage.setItem('token', rta.access_token);
        this.router.navigateByUrl('home');
      },
      error: (err: any) => {
        alert('Error en el registro.');
        console.log('Error: ', err);
        localStorage.removeItem('token');
      },
      complete: () => {
        console.log('Registro finalizado');
      },
    });
  }

  submit() {
    if (this.signinForm.valid) {
      console.log('Datos del formulario: ', this.signinForm.value);
      this.irAlRegistro(this.signinForm.value);
    } else {
      alert('Por favor, completa todos los campos.');
    }
  }
}
