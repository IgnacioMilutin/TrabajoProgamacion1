import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { ResenaComponent } from './pages/resena/resena.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { LoginComponent } from './pages/login/login.component';
import { LibrosComponent } from './pages/libros/libros.component';
import { LibroComponent } from './pages/libro/libro.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'error_page', component: ErrorPageComponent },
  { path: 'libro', component: LibroComponent },
  { path: 'libros', component: LibrosComponent },
  { path: 'login', component: LoginComponent },
  { path: 'prestamos', component: PrestamosComponent },
  { path: 'resenas', component: ResenaComponent },
  { path: 'usuario/:id/:tipo_op', component: UsuarioComponent },
  { path: 'usuarios', component: UsuariosComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '**', redirectTo: 'error_page' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
