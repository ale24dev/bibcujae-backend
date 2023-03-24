import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { MateriaLibroService } from './materia-libro.service';
import { MateriaLibroController } from './materia-libro.controller';
import { MateriaLibroRepository } from './materia-libro.repository';

@Module({
  imports: [TypeOrmModule.forFeature([MateriaLibroRepository])],
  controllers: [MateriaLibroController],
  providers: [MateriaLibroService]
})
export class MateriaLibroModule { }
