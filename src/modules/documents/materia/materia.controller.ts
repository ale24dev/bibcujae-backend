import { Controller, Get, Post, Body, Patch, Param, Delete, Query } from '@nestjs/common';
import { MateriaService } from './materia.service';
import { CreateMateriaDto } from './dto/create-materia.dto';
import { UpdateMateriaDto } from './dto/update-materia.dto';

@Controller('document/materia')
export class MateriaController {
  constructor(private readonly materiaService: MateriaService) { }

  @Post()
  create(@Body() createMateriaDto: CreateMateriaDto) {
    return this.materiaService.create(createMateriaDto);
  }

  @Get()
  async findAll() {
    return await this.materiaService.findAll();
  }

  @Get('/id/:id')
  async findOne(@Param('id') id: string) {
    return await this.materiaService.findOne(+id);
  }
  @Get('/name')
  async searchByName(@Query('name') name: string) {
    return await this.materiaService.searchByName(name);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateMateriaDto: UpdateMateriaDto) {
    return this.materiaService.update(+id, updateMateriaDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.materiaService.remove(+id);
  }
}
