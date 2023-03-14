import {
  Entity,
  Column,
  Unique,
  OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';
import * as bcrypt from 'bcryptjs';

@Entity({ name: 'xuser' })
export class UserEntity {
  @PrimaryGeneratedColumn()
  id_user: number;

  @Column({ nullable: false })
  username: string;

  @Column({ nullable: false })
  password: string;
  
  @Column({ unique: true, nullable: false })
  email: string;
  
  @Column({ nullable: false })
  salt: string;
  
  constructor(
    username: string,
    password: string,
    email: string,
    salt: string,
  ) {
    this.username = username;
    this.password = password;
    this.email = email;
    this.salt = salt;
  }

  async validatePassword(password: string): Promise<boolean> {
    const hash = await bcrypt.hash(password, this.salt);
    return hash === this.password;
  }
}
