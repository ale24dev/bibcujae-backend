import { EntityRepository, Repository } from 'typeorm';

import { MateriaLibroEntity } from './entities/materia-libro.entity';

@EntityRepository(MateriaLibroEntity)
export class MateriaLibroRepository extends Repository<MateriaLibroEntity> {

    async getMateriasByBook(bookId: number) {
        return await this
            .createQueryBuilder("xmateriaLibro")
            .leftJoinAndSelect("xmateriaLibro.materia", "xmateria")
            .leftJoin("xmateriaLibro.book", "xlibro")
            .where("xlibro.libro_id = :libroId", { libroId: bookId })
            .getMany();
    }

    async getBooksByMateria(materiaId: number) {
        return await this
            .createQueryBuilder("xmateriaLibro")
            .leftJoin("xmateriaLibro.materia", "xmateria")
            .leftJoinAndSelect("xmateriaLibro.book", "xlibro")
            .where("xmateria.materia_id = :materiaId", { materiaId })
            .getMany();
    }
}