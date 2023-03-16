import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { AuthModule } from './src/modules/auth/auth.module';
import { UserModule } from './src/modules/user/user.module';
import { ImageModule } from 'src/modules/images/image.module';
import { BookModule } from 'src/modules/documents/book/book.module';
import { typeOrmConfig } from './src/database/typeOrmConfig/typeorm.config';
import { MateriaModule } from 'src/modules/materia/materia.module';


@Module({
  imports: [
    TypeOrmModule.forRoot(typeOrmConfig),
    /*ServeStaticModule.forRoot({
      //renderPath: "public",
      rootPath: join(__dirname, '..', 'public'),
     // exclude: ["/api*"],
  }),*/
    AuthModule,
    UserModule,
    ImageModule,
    BookModule,
    MateriaModule
  ],
  controllers: [],
  providers: [],
})
export class AppModule { }
