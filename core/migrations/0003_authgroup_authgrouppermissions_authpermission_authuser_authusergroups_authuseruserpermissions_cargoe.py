# Generated by Django 3.1.1 on 2020-10-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20201008_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('id_cargo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cargo', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cargo_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('primer_ape', models.CharField(blank=True, max_length=40, null=True)),
                ('segundo_ape', models.CharField(blank=True, max_length=40, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('correo', models.CharField(max_length=30)),
                ('frecuente', models.BooleanField()),
                ('id_comuna', models.IntegerField(blank=True, null=True)),
                ('id_region', models.IntegerField(blank=True, null=True)),
                ('id_nacionalidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('m_cuadrados', models.CharField(blank=True, max_length=20, null=True)),
                ('banios', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('cantidad_habitacion', models.IntegerField(blank=True, null=True)),
                ('id_estado', models.IntegerField(blank=True, null=True)),
                ('id_region', models.IntegerField(blank=True, null=True)),
                ('id_comuna', models.IntegerField(blank=True, null=True)),
                ('id_inventario', models.IntegerField(blank=True, null=True)),
                ('id_funcionario', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_func', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre_func', models.CharField(blank=True, max_length=20, null=True)),
                ('primer_ape_func', models.CharField(blank=True, max_length=30, null=True)),
                ('segundo_ape_func', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_nac_func', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('sueldo', models.IntegerField()),
                ('fecha_contra', models.DateField(blank=True, null=True)),
                ('id_cargo', models.IntegerField(blank=True, null=True)),
                ('id_nacionalidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoDepartamento',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'estado_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoInmueble',
            fields=[
                ('id_estado_mueble', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'estado_inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('id_estado_reserva', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacturaBoleta',
            fields=[
                ('id_boleta_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('num_factura_boleta', models.IntegerField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'factura_boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_mueble', models.CharField(blank=True, max_length=40, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('id_zona_inmueble', models.IntegerField(blank=True, null=True)),
                ('id_departamento', models.IntegerField(blank=True, null=True)),
                ('id_estado_mueble', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MantencionDepartamento',
            fields=[
                ('id_mantenimiento', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_mante', models.CharField(blank=True, max_length=40, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('id_departamento', models.IntegerField(blank=True, null=True)),
                ('id_boleta_factura', models.IntegerField()),
            ],
            options={
                'db_table': 'mantencion_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nacion',
            fields=[
                ('id_nacionalidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_nacion', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'nacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReservaDepartamento',
            fields=[
                ('id_reserva', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_rev_ini', models.DateField(blank=True, null=True)),
                ('fecha_rev_fin', models.DateField(blank=True, null=True)),
                ('total_rev', models.IntegerField(blank=True, null=True)),
                ('pago_rev', models.IntegerField(blank=True, null=True)),
                ('id_cliente', models.IntegerField(blank=True, null=True)),
                ('id_estado_reserva', models.IntegerField(blank=True, null=True)),
                ('id_pago', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reserva_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiciosBasicos',
            fields=[
                ('id_servicios_basicos', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_servicio', models.CharField(blank=True, max_length=40, null=True)),
                ('total_pago_serv', models.IntegerField(blank=True, null=True)),
                ('id_boleta_factura', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'servicios_basicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiciosExtra',
            fields=[
                ('id_servicios_extra', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'servicios_extra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZonaMueble',
            fields=[
                ('id_zona_inmueble', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_zona', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zona_mueble',
                'managed': False,
            },
        ),
    ]
