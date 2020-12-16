# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargoEmpleado(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nom_cargo = models.CharField(max_length=25)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cargo_empleado'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    dv_run = models.BooleanField()
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fe_naci = models.DateField()
    frecuente = models.FloatField()
    activo = models.BooleanField()
    comuna_id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna_id_comuna')
    nacionalidad_id_nacionalidad = models.ForeignKey('Nacionalidad', models.DO_NOTHING, db_column='nacionalidad_id_nacionalidad')

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=30)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Departamento(models.Model):
    id_depa = models.IntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=60)
    numero_depa = models.IntegerField()
    precio = models.IntegerField()
    m_cuadrados = models.DecimalField(max_digits=7, decimal_places=2)
    banios = models.IntegerField()
    desc_depa = models.CharField(max_length=300)
    canti_habi = models.IntegerField()
    est_depa_id_estdepa = models.ForeignKey('EstadoDepartamento', models.DO_NOTHING, db_column='est_depa_id_estdepa')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    empleado_id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    run_empleado = models.IntegerField()
    dv_empleado = models.BooleanField()
    nom_empleado = models.CharField(max_length=30)
    apaterno_empleado = models.CharField(max_length=30)
    amaterno_empleado = models.CharField(max_length=30)
    correo_empleado = models.CharField(max_length=50)
    fe_naci_empleado = models.DateField()
    direccion_empleado = models.CharField(max_length=60)
    telefono_empleado = models.IntegerField()
    sueldo = models.IntegerField()
    fe_contrato = models.DateField()
    activo = models.BooleanField()
    cargo_empleado_id_cargo = models.ForeignKey(CargoEmpleado, models.DO_NOTHING, db_column='cargo_empleado_id_cargo')
    nacionalidad_id_nacionalidad = models.ForeignKey('Nacionalidad', models.DO_NOTHING, db_column='nacionalidad_id_nacionalidad')

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoDepartamento(models.Model):
    id_estdepartamento = models.IntegerField(primary_key=True)
    desc_estado = models.CharField(max_length=25)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_departamento'


class EstadoMueble(models.Model):
    id_estmueble = models.IntegerField(primary_key=True)
    nom_estado = models.CharField(max_length=20)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'estado_mueble'


class EstadoReserva(models.Model):
    id_estreserva = models.IntegerField(primary_key=True)
    desc_re = models.CharField(max_length=300)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'estado_reserva'


class FacturaBoleta(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    num_fact = models.IntegerField()
    foto = models.BinaryField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'factura_boleta'


class Nacionalidad(models.Model):
    id_nacionalidad = models.IntegerField(primary_key=True)
    nom_nacion = models.CharField(max_length=30)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nacionalidad'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fe_pago = models.DateField()
    detalle = models.CharField(max_length=30)
    total_pago = models.IntegerField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pago'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nom_region = models.CharField(max_length=60)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'region'


class ReservaDepartamento(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    total = models.IntegerField()
    pago_id_pago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='pago_id_pago')
    estado_reserva_id_estreserva = models.ForeignKey(EstadoReserva, models.DO_NOTHING, db_column='estado_reserva_id_estreserva')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    departamento_id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depa')

    class Meta:
        managed = False
        db_table = 'reserva_departamento'


class ServicioDepartamento(models.Model):
    departamento_id_depa = models.OneToOneField(Departamento, models.DO_NOTHING, db_column='departamento_id_depa', primary_key=True)
    servicio_extra_id_servextra = models.ForeignKey('ServicioExtra', models.DO_NOTHING, db_column='servicio_extra_id_servextra')

    class Meta:
        managed = False
        db_table = 'servicio_departamento'
        unique_together = (('departamento_id_depa', 'servicio_extra_id_servextra'),)


class ServicioExtra(models.Model):
    id_servextra = models.IntegerField(primary_key=True)
    desc_serv = models.CharField(max_length=80)
    activo = models.BooleanField()
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio_extra'

