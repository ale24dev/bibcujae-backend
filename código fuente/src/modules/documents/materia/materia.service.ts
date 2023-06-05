import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CreateMateriaDto } from './dto/create-materia.dto';
import { UpdateMateriaDto } from './dto/update-materia.dto';
import { MateriaRepository } from './materia.repository';

@Injectable()
export class MateriaService {

  @InjectRepository(MateriaRepository)
  private readonly materiaRepository: MateriaRepository;

  create(createMateriaDto: CreateMateriaDto) {
    return 'This action adds a new materia';
  }

  async findAll() {
    return await this.materiaRepository.findAll();
  }

  async findOne(id: number) {
    const materia = await this.materiaRepository.findOne({ where: { materiaId: id } });

    if (!materia) {
      throw new NotFoundException(`No se encontró ningúna materia con id: ${id}`);
    }
    return materia;
  }

  async searchByName(name: string) {
    return await this.materiaRepository.searchByName(name);
  }

  update(id: number, updateMateriaDto: UpdateMateriaDto) {
    return `This action updates a #${id} materia`;
  }

  remove(id: number) {
    return `This action removes a #${id} materia`;
  }
}
