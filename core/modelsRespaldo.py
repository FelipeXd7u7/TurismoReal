# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class CargoEmpleado(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nom_cargo = models.CharField(max_length=25)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cargo_empleado'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
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
        

# class RegistroCliente(Cliente):

#     rut = models.CharField(max_length=10)
#     nombre = models.CharField(max_length=40)
#     apaterno = models.CharField(max_length=30)
#     amaterno = models.CharField(max_length=30)
#     correo = models.CharField(max_length=30)
#     direccion = models.CharField(max_length=50)
#     telefono = models.IntegerField()
#     fe_naci = models.DateField()
#     comuna_id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna_id_comuna')
#     nacionalidad_id_nacionalidad = models.ForeignKey('Nacionalidad', models.DO_NOTHING, db_column='nacionalidad_id_nacionalidad')

#     class Meta:
#         managed = False
#         db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=30)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return self.nom_comuna



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


class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    nom_mueble = models.CharField(max_length=40)
    desc = models.CharField(max_length=100)
    activo = models.BooleanField()
    estado_mueble_id_estmueble = models.ForeignKey(EstadoMueble, models.DO_NOTHING, db_column='estado_mueble_id_estmueble')
    zona_mueble_id_zona = models.ForeignKey('ZonaMueble', models.DO_NOTHING, db_column='zona_mueble_id_zona')
    departamento_id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depa')

    class Meta:
        managed = False
        db_table = 'inventario'


class MantencionDepartamento(models.Model):
    id_mantencion = models.IntegerField(primary_key=True)
    desc_mante = models.CharField(max_length=40)
    costo = models.IntegerField()
    activo = models.BooleanField()
    departamento_id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depa')
    fecha_md = models.DateField()
    tipo_gasto_id_gasto = models.ForeignKey('TipoGasto', models.DO_NOTHING, db_column='tipo_gasto_id_gasto', blank=True, null=True)
    factura_boleta_id_factura = models.ForeignKey(FacturaBoleta, models.DO_NOTHING, db_column='factura_boleta_id_factura')

    class Meta:
        managed = False
        db_table = 'mantencion_departamento'


class Nacionalidad(models.Model):
    id_nacionalidad = models.IntegerField(primary_key=True)
    nom_nacion = models.CharField(max_length=30)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nacionalidad'

    def __str__(self):
        return self.nom_nacion

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


class TipoGasto(models.Model):
    id_gasto = models.IntegerField(primary_key=True)
    desc_gasto = models.CharField(max_length=40)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipo_gasto'


class ZonaMueble(models.Model):
    id_zona = models.IntegerField(primary_key=True)
    nom_zonam = models.CharField(max_length=40)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'zona_mueble'
