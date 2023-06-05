import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { MateriaLibroEntity } from "../../materia-libro/entities/materia-libro.entity";

@Entity({ name: "xmateria" })
export class MateriaEntity {

    @PrimaryGeneratedColumn({ name: "materia_id" })
    materiaId: number;

    @Column({ nullable: false, length: "MAX" })
    name: string;

    @OneToMany(() => MateriaLibroEntity, xmateriaLibro => xmateriaLibro.materia)
    xmateriaLibros: MateriaLibroEntity[];
}
