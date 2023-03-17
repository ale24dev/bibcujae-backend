import { Controller, Get, Post, Body, Patch, Param, Delete, Query, ParseIntPipe } from '@nestjs/common';
import { MateriaLibroService } from './materia-libro.service';
import { CreateMateriaLibroDto } from './dto/create-materia-libro.dto';
import { UpdateMateriaLibroDto } from './dto/update-materia-libro.dto';

@Controller('document/materia-libro')
export class MateriaLibroController {
  constructor(private readonly materiaLibroService: MateriaLibroService) { }

  // @Post()
  // create(@Body() createMateriaLibroDto: CreateMateriaLibroDto) {
  //   return this.materiaLibroService.create(createMateriaLibroDto);
  // }

  @Get('/materiasByBook')
  getMateriasByBook(@Query('libro_id', ParseIntPipe) bookId: number) {
    return this.materiaLibroService.getMateriasByBook(bookId);
  }

  @Get('/booksByMateria')
  getBooksByMateria(@Query('materia_id', ParseIntPipe) materiaId: number) {
    return this.materiaLibroService.getBooksByMateria(materiaId);
  }
}
