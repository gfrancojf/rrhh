from django.db import models


# Create your models here.
class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    create_at = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)
    update_at = models.DateField(
        'Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_at = models.DateField(
        'Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Empresa(ModeloBase):
    nempresa = models.CharField(
        'Nombre de la empresa', max_length=60, unique=True)
    acronimo = models.CharField(
        'Acronimo', max_length=60, null=True, blank=True)
    rif = models.CharField('R.I.F', max_length=30, null=True, blank=True)
    imgref = models.ImageField(
        'Imagen de Referencia', upload_to='empresa/', null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nempresa


class Oficina(ModeloBase):
    noficina = models.CharField(
        'Nombre de la Oficina', max_length=60, unique=True)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return self.noficina


class Estante(ModeloBase):
    ubicacion = models.CharField(
        'Ubicacion del Expedientes', max_length=60, unique=True)

    class Meta:
        verbose_name = 'Estante'
        verbose_name_plural = 'Estantes'

    def __str__(self):
        return self.ubicacion


class Cargo(ModeloBase):
    cargo = models.CharField('Cargo', max_length=60, unique=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Empleado(ModeloBase):
    Lista_status = [('A', 'ACTIVO'),
                    ('E', 'EGRESO'),
                    ('J', 'JUBILADO'),
                    ]
    status = models.CharField(
        'Estatus del Empleado', max_length=1, choices=Lista_status, null=False, default='A')
    lista_Genero = [('F', 'FEMENINO'),
                    ('M', 'MASCULINO'),
                    ('O', 'OTROS'),
                    ]
    genero = models.CharField('Genero', max_length=1,
                              choices=lista_Genero, null=False, default='O')
    lista_Nacionalidad = [('V', 'VENEZOLANO'),
                          ('E', 'EXTRANJERO'),
                          ]
    nac = models.CharField('Nacionalidad', max_length=1,
                           choices=lista_Nacionalidad, null=False, default='v')

    cedula = models.CharField('Cedula', max_length=10, null=False, unique=True)
    codpatria = models.CharField(
        'Codigo Patria', max_length=10, null=False, default='0000000000')
    serialpatria = models.CharField(
        'Serial Patria', max_length=10, null=False, default='0000000000')
    primerNombre = models.CharField('Primer Nombre', max_length=60, null=False)
    primerApellido = models.CharField(
        'Primer Apellido', max_length=60, null=False)
    segundoNombre = models.CharField(
        'Segundo Nombre', max_length=60, null=True, blank=True)
    segundoApellido = models.CharField(
        'Segundo Apellido', max_length=60, null=True, blank=True)
    fecha_ingreso = models.DateField('F. de Ingreso', null=False)
    fecha_egreso = models.DateField('F. de Egreso',  null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)

    observacion = models.TextField(
        'Observaciones', max_length=255,  null=True, blank=True)
    doc = models.FileField(null=True, blank=True, upload_to='empresa/doc')

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.cedula
