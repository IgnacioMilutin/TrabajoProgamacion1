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
    VerUserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
