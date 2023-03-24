import {
  BaseEntity,
  Entity,
  PrimaryGeneratedColumn,
  Column,
  ManyToMany,
  JoinColumn,
} from 'typeorm';
import { UserEntity } from '../user/user.entity';

@Entity('xxrole')
export class RoleEntity extends BaseEntity {
  @PrimaryGeneratedColumn({name: "id_role"})
  idRole: number;

  @Column({ nullable: false })
  name: string;

  @ManyToMany(type => UserEntity, user => user.roles)
  @JoinColumn()
  users: UserEntity[];
}
