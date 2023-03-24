import { Module } from '@nestjs/common';
import { MateriaService } from './materia.service';
import { MateriaController } from './materia.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { MateriaRepository } from './materia.repository';

@Module({
  imports: [TypeOrmModule.forFeature([MateriaRepository])],
  controllers: [MateriaController],
  providers: [MateriaService]
})
export class MateriaModule { }
