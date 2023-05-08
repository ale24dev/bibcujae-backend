from django.db import models


class Book(models.Model):
    libro_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, null=True)
    entrada = models.TextField(null=True)
    tipo_autor = models.CharField(max_length=255, null=True)
    autor = models.CharField(max_length=255, null=True)
    otros_autores = models.TextField(null=True)
    edicion = models.CharField(max_length=255, null=True)
    serie = models.CharField(max_length=255, null=True)
    notas = models.TextField(null=True)
    anno_pub = models.CharField(max_length=255, null=True)
    mencion_resp = models.TextField(null=True)
    cod_domicilio = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=255, null=True)
    dewey = models.CharField(max_length=255, null=True)
    evento = models.CharField(max_length=255, null=True)
    otros_eventos = models.CharField(max_length=255, null=True)
    publicacion = models.CharField(max_length=255, null=True)
    colacion = models.CharField(max_length=255, null=True)
    otros_titulos = models.CharField(max_length=255, null=True)
    folleto = models.CharField(max_length=255, null=True)
    referencia = models.CharField(max_length=255, null=True)
    letras_ent = models.CharField(max_length=255, null=True)
    letra_titulo = models.CharField(max_length=255, null=True)
    clasif = models.CharField(max_length=255, null=True)
    idioma = models.CharField(max_length=255, null=True)
    pais = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "book"

    # def save(self, *args, **kwargs):
    #     # Generar el código único de 13 dígitos
    #     codigo_generado = str(random.randint(1000000000000, 9999999999999))

    #     # Validar que el código generado no exista ya en la base de datos
    #     while Book.objects.filter(barCo=codigo_generado).exists():
    #         codigo_generado = str(random.randint(1000000000000, 9999999999999))

    #     # Asignar el código generado al objeto Libro
    #     self.codigo = codigo_generado

    #     # Llamar al método save del modelo padre para guardar el objeto en la base de datos
    #     super(Libro, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def to_dict(self):
        return {
            'libro_id': self.libro_id,
            'titulo': self.titulo,
            'entrada': self.entrada,
            'tipo_autor': self.tipo_autor,
            'autor': self.autor,
            'otros_autores': self.otros_autores,
            'edicion': self.edicion,
            'serie': self.serie,
            'notas': self.notas,
            'anno_pub': self.anno_pub,
            'mencion_resp': self.mencion_resp,
            'cod_domicilio': self.cod_domicilio,
            'isbn': self.isbn,
            'dewey': self.dewey,
            'evento': self.evento,
            'otros_eventos': self.otros_eventos,
            'publicacion': self.publicacion,
            'colacion': self.colacion,
            'otros_titulos': self.otros_titulos,
            'folleto': self.folleto,
            'referencia': self.referencia,
            'letras_ent': self.letras_ent,
            'letra_titulo': self.letra_titulo,
            'clasif': self.clasif,
            'idioma': self.idioma,
            'pais': self.pais
        }


def bookFromJson(json_data):
    book = Book(
        titulo=json_data.get('titulo'),
        entrada=json_data.get('entrada'),
        tipo_autor=json_data.get('tipo_autor'),
        autor=json_data.get('autor'),
        otros_autores=json_data.get('otros_autores'),
        edicion=json_data.get('edicion'),
        serie=json_data.get('serie'),
        notas=json_data.get('notas'),
        anno_pub=json_data.get('anno_pub'),
        mencion_resp=json_data.get('mencion_resp'),
        cod_domicilio=json_data.get('cod_domicilio'),
        isbn=json_data.get('isbn'),
        dewey=json_data.get('dewey'),
        evento=json_data.get('evento'),
        otros_eventos=json_data.get('otros_eventos'),
        publicacion=json_data.get('publicacion'),
        colacion=json_data.get('colacion'),
        otros_titulos=json_data.get('otros_titulos'),
        folleto=json_data.get('folleto'),
        referencia=json_data.get('referencia'),
        letras_ent=json_data.get('letras_ent'),
        letra_titulo=json_data.get('letra_titulo'),
        clasif=json_data.get('clasif'),
        idioma=json_data.get('idioma'),
        pais=json_data.get('pais')
    )
    return book


def parseParams(request):
    titulo = request.GET.get('titulo')
    entrada = request.GET.get('entrada')
    tipo_autor = request.GET.get('tipo_autor')
    autor = request.GET.get('autor')
    otros_autores = request.GET.get('otros_autores')
    edicion = request.GET.get('edicion')
    serie = request.GET.get('serie')
    notas = request.GET.get('notas')
    anno_pub = request.GET.get('anno_pub')
    mencion_resp = request.GET.get('mencion_resp')
    cod_domicilio = request.GET.get('cod_domicilio')
    isbn = request.GET.get('isbn')
    dewey = request.GET.get('dewey')
    evento = request.GET.get('evento')
    otros_eventos = request.GET.get('otros_eventos')
    publicacion = request.GET.get('publicacion')
    colacion = request.GET.get('colacion')
    otros_titulos = request.GET.get('otros_titulos')
    folleto = request.GET.get('folleto')
    referencia = request.GET.get('referencia')
    letras_ent = request.GET.get('letras_ent')
    letra_titulo = request.GET.get('letra_titulo')
    clasif = request.GET.get('clasif')
    idioma = request.GET.get('idioma')
    pais = request.GET.get('pais')

    # Aquí se puede procesar los datos y retornar una respuesta
    # En este ejemplo, se renderiza una plantilla con los datos procesados
    bookParsed = {
        'titulo': titulo,
        'entrada': entrada,
        'tipo_autor': tipo_autor,
        'autor': autor,
        'otros_autores': otros_autores,
        'edicion': edicion,
        'serie': serie,
        'notas': notas,
        'anno_pub': anno_pub,
        'mencion_resp': mencion_resp,
        'cod_domicilio': cod_domicilio,
        'isbn': isbn,
        'dewey': dewey,
        'evento': evento,
        'otros_eventos': otros_eventos,
        'publicacion': publicacion,
        'colacion': colacion,
        'otros_titulos': otros_titulos,
        'folleto': folleto,
        'referencia': referencia,
        'letras_ent': letras_ent,
        'letra_titulo': letra_titulo,
        'clasif': clasif,
        'idioma': idioma,
        'pais': pais
    }
    return bookParsed
