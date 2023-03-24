import { EntityRepository, Repository } from 'typeorm';
import { BookEntity } from './entities/book.entity';

@EntityRepository(BookEntity)
export class BookRepository extends Repository<BookEntity> {


    async findBooksByName(query: string): Promise<BookEntity[]> {
        const listBooks = await this.find();
        const searchTerm = query.trim().toLowerCase();
        const filteredBooks = listBooks.filter((book) => {
            if (book.titulo) {
                const bookName = book.titulo.toLowerCase();
                return (
                    bookName.includes(searchTerm) || bookName.startsWith(searchTerm)
                );
            }
        });
        console.log(filteredBooks);
        return filteredBooks.sort((a, b) => a.titulo.localeCompare(b.titulo));
    }

    async searchBooks(
        titulo?: string,
        entrada?: string,
        tipoAutor?: string,
        autor?: string,
        otrosAutores?: string,
        edicion?: string,
        serie?: string,
        notas?: string,
        annoPub?: string,
        mencionResp?: string,
        codDomicilio?: string,
        isbn?: string,
        dewey?: string,
        evento?: string,
        otrosEventos?: string,
        publicacion?: string,
        colacion?: string,
        otrosTitulos?: string,
        folleto?: string,
        referencia?: string,
        letrasEnt?: string,
        letraTitulo?: string,
        clasif?: string,
        idioma?: string,
        pais?: string
    ): Promise<BookEntity[]> {
        const queryBuilder = this.createQueryBuilder("book");
        console.log(titulo);
        if (titulo) {
            console.log("Entre");
            queryBuilder.andWhere("book.titulo LIKE :titulo", { titulo: `%${titulo}%` });
        }
        if (entrada) {
            queryBuilder.andWhere("book.entrada LIKE :entrada", { entrada: `%${entrada}%` });
        }
        if (tipoAutor) {
            queryBuilder.andWhere("book.tipoAutor = :tipoAutor", { tipoAutor });
        }
        if (autor) {
            queryBuilder.andWhere("book.autor LIKE :autor", { autor: `%${autor}%` });
        }
        if (otrosAutores) {
            queryBuilder.andWhere("book.otrosAutores LIKE :otrosAutores", { otrosAutores: `%${otrosAutores}%` });
        }
        if (edicion) {
            queryBuilder.andWhere("book.edicion LIKE :edicion", { edicion: `%${edicion}%` });
        }
        if (serie) {
            queryBuilder.andWhere("book.serie LIKE :serie", { serie: `%${serie}%` });
        }
        if (notas) {
            queryBuilder.andWhere("book.notas LIKE :notas", { notas: `%${notas}%` });
        }
        if (annoPub) {
            queryBuilder.andWhere("book.annoPub = :annoPub", { annoPub });
        }
        if (mencionResp) {
            queryBuilder.andWhere("book.mencionResp LIKE :mencionResp", { mencionResp: `%${mencionResp}%` });
        }
        if (codDomicilio) {
            queryBuilder.andWhere("book.codDomicilio = :codDomicilio", { codDomicilio });
        }
        if (isbn) {
            queryBuilder.andWhere("book.isbn = :isbn", { isbn });
        }
        if (dewey) {
            queryBuilder.andWhere("book.dewey = :dewey", { dewey });
        }
        if (evento) {
            queryBuilder.andWhere("book.evento = :evento", { evento });
        }
        if (otrosEventos) {
            queryBuilder.andWhere("book.otrosEventos LIKE :otrosEventos", { otrosEventos: `%${otrosEventos}%` });
        }
        if (publicacion) {
            queryBuilder.andWhere("book.publicacion = :publicacion", { publicacion });
        }
        if (colacion) {
            queryBuilder.andWhere("book.colacion = :colacion", { colacion });
        }
        if (otrosTitulos) {
            queryBuilder.andWhere("book.otrosTitulos LIKE :otrosTitulos", { otrosTitulos: `%${otrosTitulos}%` });
        }
        if (folleto) {
            queryBuilder.andWhere("book.folleto = :folleto", { folleto });
        }
        if (referencia) {
            queryBuilder.andWhere("book.referencia = :referencia", { referencia });
        }
        if (letrasEnt) {
            queryBuilder.andWhere("book.letrasEnt = :letrasEnt", { letrasEnt });
        }
        if (letraTitulo) {
            queryBuilder.andWhere("book.letraTitulo = :letraTitulo", { letraTitulo });
        }
        if (clasif) {
            queryBuilder.andWhere("book.clasif = :clasif", { clasif });
        }
        if (idioma) {
            queryBuilder.andWhere("book.idioma = :idioma", { idioma });
        }
        if (pais) {
            queryBuilder.andWhere("book.pais = :pais", { pais });
        }

        queryBuilder.orderBy('titulo', "ASC");

        const results = await queryBuilder.getMany();

        return results;
    }
}