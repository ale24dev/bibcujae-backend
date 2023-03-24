import {
  Controller,
  Get,
  Param,
  Post,
  Body,
  Patch,
  Delete,
  ParseIntPipe,
} from '@nestjs/common';
import { RoleService } from './role.service';
import { RoleEntity } from './role.entity';

@Controller('roles')
export class RoleController {
  constructor(private readonly _roleService: RoleService) {}

  @Get(':id')
  async getRole(@Param('id', ParseIntPipe) id: number): Promise<RoleEntity> {
    const role = await this._roleService.get(id);
    return role;
  }

  @Get()
  async getRoles(): Promise<RoleEntity[]> {
    const roles = await this._roleService.getAll();
    return roles;
  }

  @Post()
  async createRole(@Body() role: RoleEntity): Promise<RoleEntity> {
    const createdRole = await this._roleService.create(role);
    return createdRole;
  }

  @Patch(':id')
  async updateRole(@Param('id', ParseIntPipe) id: number, @Body() role: RoleEntity) {
    await this._roleService.update(id, role);
    return true;
  }

  // @Delete(':id')
  // async deleteRole(@Param('id', ParseIntPipe) id: number) {
  //   await this._roleService.delete(id);
  //   return true;
  // }
}
