import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { AuthModule } from './src/modules/auth/auth.module';
import { UserModule } from './src/modules/user/user.module';
import { typeOrmConfig } from './src/database/typeOrmConfig/typeorm.config';
import { ImageModule } from 'src/modules/images/image.module';
import { BookModule } from 'src/modules/book/book.module';


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
    BookModule
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
