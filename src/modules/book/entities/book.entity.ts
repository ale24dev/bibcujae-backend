import { Entity, Column, PrimaryColumn, PrimaryGeneratedColumn } from 'typeorm';

@Entity({ name: "xlibro" })
export class BookEntity {
    @PrimaryGeneratedColumn({ name: "libro_id" })
    libroId: number;

    @Column({ name: "titulo", nullable: true, length: 'MAX' })
    titulo: string;

    @Column({ name: "entrada", nullable: true })
    entrada: string;

    @Column({ nullable: true, name: 'tipo_autor' })
    tipoAutor: string;

    @Column({ nullable: true })
    autor: string;

    @Column({ nullable: true, name: 'otros_autores', length: 'MAX' })
    otrosAutores: string;

    @Column({ nullable: true })
    edicion: string;

    @Column({ nullable: true })
    serie: string;

    @Column({ nullable: true, length: 'MAX' })
    notas: string;

    @Column({ name: 'anno_pub', nullable: true })
    annoPub: string;

    @Column({ name: 'mencion_resp', nullable: true, length: 'MAX' })
    mencionResp: string;

    @Column({ name: 'cod_domicilio', nullable: true })
    codDomicilio: string;

    @Column({ nullable: true })
    isbn: string;

    @Column({ nullable: true })
    dewey: string;

    @Column({ nullable: true })
    evento: string;

    @Column({ name: 'otros_eventos', nullable: true })
    otrosEventos: string;

    @Column({ nullable: true })
    publicacion: string;

    @Column({ nullable: true })
    colacion: string;

    @Column({ name: 'otros_titulos', nullable: true })
    otrosTitulos: string;

    @Column({ nullable: true })
    folleto: string;

    @Column({ nullable: true })
    referencia: string;

    @Column({ nullable: true })
    letrasEnt: string;

    @Column({ nullable: true })
    letraTitulo: string;

    @Column({ nullable: true })
    clasif: string;

    @Column({ nullable: true })
    idioma: string;

    @Column({ nullable: true })
    pais: string;
}
