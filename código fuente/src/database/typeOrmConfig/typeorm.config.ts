import { join } from 'path';
import { TypeOrmModuleOptions } from '@nestjs/typeorm';


export const typeOrmConfig: TypeOrmModuleOptions = {
  type: 'mssql',
  host: 'localhost',
  // port: process.env.RDS_PORT || 5432,
  port: 1433,
  username: 'ale_user',
  password: 'somosonosomos24',
  // database: process.env.RDS_DB_NAME || dbConfig.database,
  database: 'BiblioCujae',
  entities: [join(__dirname, '..', '..', 'modules', '**', '*.entity.{js,ts}')],
  // seeds: ['src/seeds/**/*{.ts,.js}'],
  // factories: ['src/factories/**/*{.ts,.js}'],
  //synchronize: process.env.TYPEORM_SYNC || dbConfig.synchronize,
  synchronize: true,
  migrations: [join(__dirname, '..', 'migrations', '*.{ts,js}')],
  cli: {
    migrationsDir: join('src', 'database', 'migrations'),
  },
};
