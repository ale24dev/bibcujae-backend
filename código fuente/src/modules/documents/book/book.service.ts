import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { BookRepository } from './book.repository';
import { CreateBookDto } from './dto/create-book.dto';
import { UpdateBookDto } from './dto/update-book.dto';

@Injectable()
export class BookService {
  constructor(
    @InjectRepository(BookRepository)
    private readonly bookRepository: BookRepository,
  ) { }

  create(createBookDto: CreateBookDto) {
  }

  async findAll(page: number, limit: number) {
    const books = await this.bookRepository
      .createQueryBuilder('libro')
      .skip((page - 1) * limit)
      .take(limit)
      .getManyAndCount();
    return books;
  }

  async findBooksByFilter(titulo,
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
  ) {
    const books = await this.bookRepository.searchBooks(
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
  async findByDomCode(codDomicilio: number) {
    return await this.bookRepository.findOne({ where: { codDomicilio: codDomicilio } });
  }

  async findBooksByName(text: string) {
    return await this.bookRepository.findBooksByName(text);
  }

  update(id: number, updateBookDto: UpdateBookDto) {
    return `This action updates a #${id} book`;
  }

  remove(id: number) {
    return `This action removes a #${id} book`;
  }
}
