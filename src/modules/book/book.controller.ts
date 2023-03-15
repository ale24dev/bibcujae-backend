import { Controller, Get, Post, Body, Patch, Param, Delete, Query } from '@nestjs/common';

import { BookService } from './book.service';
import { CreateBookDto } from './dto/create-book.dto';
import { UpdateBookDto } from './dto/update-book.dto';
import { BookEntity } from './entities/book.entity';

@Controller('book')
export class BookController {
  constructor(private readonly bookService: BookService) { }

  @Post()
  create(@Body() createBookDto: CreateBookDto) {
    return this.bookService.create(createBookDto);
  }

  @Get("/filter")
  async searchBooks(
    @Query('titulo') titulo: string,
    @Query('entrada') entrada: string,
    @Query('autor') autor: string,
    @Query('otrosAutores') otrosAutores: string,
    @Query('annoPub') annoPub: string,
    @Query('dewey') dewey: string,
    @Query('evento') evento: string,
    @Query('publicacion') publicacion: string,
    @Query('letrasEnt') letrasEnt: string,
    @Query('idioma') idioma: string,
    @Query('tipoAutor') tipoAutor: string,
    @Query('edicion') edicion: string,
    @Query('serie') serie: string,
    @Query('notas') notas: string,
    @Query('pais') pais: string,
    @Query('mencionResp') mencionResp: string,
    @Query('codDomicilio') codDomicilio: string,
    @Query('isbn') isbn: string,
    @Query('otrosEventos') otrosEventos: string,
    @Query('colacion') colacion: string,
    @Query('otrosTitulos') otrosTitulos: string,
    @Query('folleto') folleto: string,
    @Query('referencia') referencia: string,
    @Query('letraTitulo') letraTitulo: string,
    @Query('clasif') clasif: string,
  ): Promise<BookEntity[]> {
    console.log(titulo);
    const books = await this.bookService.findBooksByFilter(
      titulo,
      entrada,
      tipoAutor,
      autor,
      otrosAutores,
      edicion,
      serie,
      notas,
      annoPub,
      mencionResp,
      codDomicilio,
      isbn,
      dewey,
      evento,
      otrosEventos,
      publicacion,
      colacion,
      otrosTitulos,
      folleto,
      referencia,
      letrasEnt,
      letraTitulo,
      clasif,
      idioma,
      pais
    );
    return books;
  }
  @Get()
  async findAll(
    @Query('page') page: number = 1,
    @Query('limit') limit: number = 10,
  ) {
    return await this.bookService.findAll(page, limit);
  }

  @Get('/domcode/:codDomicilio')
  findByDomCode(@Param('codDomicilio') codDomicilio: number) {
    return this.bookService.findByDomCode(codDomicilio);
  }

  @Get('/name/:text')
  findBooksByName(@Param('text') text: string) {
    console.log(text);
    return this.bookService.findBooksByName(text);
  }

  // @Patch(':id')
  // update(@Param('id') id: number, @Body() updateBookDto: UpdateBookDto) {
  //   return this.bookService.update(id, updateBookDto);
  // }

  // @Delete(':id')
  // remove(@Param('id') id: string) {
  //   return this.bookService.remove(+id);
  // }
}
