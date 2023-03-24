import { Entity, PrimaryGeneratedColumn, ManyToOne, JoinColumn } from 'typeorm';
import { BookEntity } from '../../book/entities/book.entity';
import { MateriaEntity } from '../../materia/entities/materia.entity';

@Entity({ name: 'xmateriaLibro' })
export class MateriaLibroEntity {
    @PrimaryGeneratedColumn({ name: 'materiaLibro_id' })
    materiaLibroId: number;

    @ManyToOne(() => BookEntity, book => book.libroId)
    @JoinColumn({ name: "libro_id" })
    book: BookEntity;
    
    @ManyToOne(() => MateriaEntity, materia => materia.materiaId)
    @JoinColumn({ name: "materia_id" })
    materia: MateriaEntity;

}

