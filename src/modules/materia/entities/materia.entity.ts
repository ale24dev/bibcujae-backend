import { Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity({ name: "xmateria" })
export class MateriaEntity {

    @PrimaryGeneratedColumn({ name: "materia_id" })
    materiaId: number;

    @Column({ nullable: false, length: "MAX" })
    name: string;
}
