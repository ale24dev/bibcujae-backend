import { PartialType } from '@nestjs/mapped-types';
import { CreateMateriaLibroDto } from './create-materia-libro.dto';

export class UpdateMateriaLibroDto extends PartialType(CreateMateriaLibroDto) {}
