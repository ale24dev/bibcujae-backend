import {
  Injectable,
  BadRequestException,
  NotFoundException,
} from '@nestjs/common';
import { RoleRepository } from './role.repository';
import { InjectRepository } from '@nestjs/typeorm';
import { RoleEntity } from './role.entity';

@Injectable()
export class RoleService {
  constructor(
    @InjectRepository(RoleRepository)
    private readonly _roleRepository: RoleRepository,
  ) {}

  async get(id: number): Promise<RoleEntity> {
    if (!id) {
      throw new BadRequestException('id must be sent');
    }

    const role: RoleEntity = await this._roleRepository.findOne(id, {
      where: { status: 'ACTIVE' },
    });

    if (!role) {
      throw new NotFoundException();
    }

    return role;
  }

  async getAll(): Promise<RoleEntity[]> {
    const roles: RoleEntity[] = await this._roleRepository.find({
      where: { status: 'ACTIVE' },
    });

    return roles;
  }

  async create(role: RoleEntity): Promise<RoleEntity> {
    const savedRole: RoleEntity = await this._roleRepository.save(role);
    return savedRole;
  }

  async update(id: number, role: RoleEntity): Promise<void> {
    await this._roleRepository.update(id, role);
  }

  // async delete(id: number): Promise<void> {
  //   const roleExists = await this._roleRepository.findOne(id, {
  //     where: { status: 'ACTIVE' },
  //   });

  //   if (!roleExists) {
  //     throw new NotFoundException();
  //   }

  //   await this._roleRepository.update(id, { status: 'INACTIVE' });
  // }
}
