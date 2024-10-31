import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  loginForm!: FormGroup;
  constructor(
    private authService: AuthService,
    private router: Router,
    private fromBuilder: FormBuilder
  ) {
    this.loginForm = this.fromBuilder.group({
      mail: ['sb.escuderini@gmail.com', Validators.required],
      password: ['1234', Validators.required],
    });
  }
  irAlLogin(dataLogin: any) {
    this.authService.login(dataLogin).subscribe({
      next: (rta: any) => {
        alert('Credenciales correctas!!!');
        console.log('Exito: ', rta);
        localStorage.setItem('token', rta.access_token);
        this.router.navigateByUrl('home');
      },
      error: (err: any) => {
        alert('Usuario o contraseña incorrecta.');
        console.log('Exito: ', err);
        localStorage.removeItem('token');
      },
      complete: () => {
        console.log('Fianlizo');
      },
    });
  }

  submit() {
    if (this.loginForm.valid) {
      console.log('Datos del formulario: ', this.loginForm.value);
      this.irAlLogin(this.loginForm.value);
    } else {
      alert('No se ingresaron datos');
    }
  }
}
