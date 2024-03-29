import { EntityRepository, Repository } from "typeorm";
import { MateriaEntity } from "./entities/materia.entity";

@EntityRepository(MateriaEntity)
export class MateriaRepository extends Repository<MateriaEntity> {
    async findAll(): Promise<MateriaEntity[]> {
        return this.find();
    }

    async findById(id: number): Promise<MateriaEntity | undefined> {
        return this.findOne(id);
    }

    async searchByName(name: string): Promise<MateriaEntity[]> {
        const materias = await this.findAll();
        const matResult = materias.filter(materia => materia.name.toLowerCase().includes(name.toLowerCase().trim()));
        const sort = matResult.sort((materiaA, materiaB) => materiaA.name.localeCompare(materiaB.name));
        return sort;
    }

    async createMateria(materia: MateriaEntity): Promise<MateriaEntity> {
        return this.save(materia);
    }

    async updateMateria(materia: MateriaEntity): Promise<MateriaEntity> {
        return this.save(materia);
    }

    async deleteById(id: number): Promise<void> {
        await this.delete(id);
    }
}
