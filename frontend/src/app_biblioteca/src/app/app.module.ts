import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { NavComponent } from './components/nav/nav.component';
import { FooterComponent } from './components/footer/footer.component';
import { LibroComponent } from './pages/libro/libro.component';
import { LibrosComponent } from './pages/libros/libros.component';
import { LoginComponent } from './pages/login/login.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { ResenaComponent } from './pages/resena/resena.component';
import { AbmComponent } from './components/usuarios/abm/abm.component';
import { VerUserComponent } from './components/usuarios/ver-user/ver-user.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { BarraBusquedaComponent } from './components/shared/barra-busqueda/barra-busqueda.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorPageComponent,
    NavComponent,
    FooterComponent,
    LibroComponent,
    LibrosComponent,
    LoginComponent,
    PrestamosComponent,
    UsuariosComponent,
    ResenaComponent,
    AbmComponent,
    VerUserComponent,
    UsuarioComponent,
    BarraBusquedaComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
