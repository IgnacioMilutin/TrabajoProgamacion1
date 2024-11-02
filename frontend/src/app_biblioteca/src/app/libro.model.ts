export interface Autor {
  id_autor: number;
  nombre: string;
}

export interface Libro {
  id_libro: number;
  titulo: string;
  autores: Autor[];
  editorial: string;
  genero: string;
  unidades: number;
  valoracion_total: number;
  activo: boolean;
}
