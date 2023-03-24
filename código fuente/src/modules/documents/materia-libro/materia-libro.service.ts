import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';

import { MateriaLibroRepository } from './materia-libro.repository';

@Injectable()
export class MateriaLibroService {

  constructor(
    @InjectRepository(MateriaLibroRepository)
    private readonly materiaLibroRepository: MateriaLibroRepository,
  ) { }

  // create(createMateriaLibroDto: CreateMateriaLibroDto) {
  //   return 'This action adds a new materiaLibro';
  // }

  async getMateriasByBook(bookId: number) {
    return this.materiaLibroRepository.getMateriasByBook(bookId);
  }

  async getBooksByMateria(materiaId: number) {
    return this.materiaLibroRepository.getBooksByMateria(materiaId);
  }
}
