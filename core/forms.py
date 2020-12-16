from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, ReservaDepartamento

class CustomUserForm(UserCreationForm):
   pass

DOY = ( '2004','2003','2002','2001','2000','1999','1998','1997','1996','1995','1994','1993','1992','1991',
'1990','1989','1988','1987','1986','1985','1984','1983','1982','1981','1980','1979','1978','1977',
'1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966','1965','1964','1963',
'1962','1961','1960','1959','1958','1957','1956','1955','1954','1953','1952','1951','1950','1949',
'1948','1947','1946','1945','1944','1943','1942','1941','1940','1939','1938','1937','1936','1935',
'1934','1933','1932','1931','1930','1929','1928','1927','1926','1925','1924','1923','1922','1921',
'1920')
   
        
        
        
        

class registrocliente(forms.ModelForm):

    class Meta:
        model = Cliente
        #  fields = ["",""]
        #fields = '__all__'
        fields = ['rut','nombre','apaterno','amaterno','correo','direccion','telefono','fe_naci','comuna_id_comuna','nacionalidad_id_nacionalidad']
        labels = {
        "rut": "Rut",
        "nombre": "Nombre",
        "apaterno": "Primer Apellido",
        "amaterno": "Segundo Apellido",
        "correo": "Correo",
        "direccion": "Direccion",
        "telefono": "Telefono",
        "fe_naci": "Fecha de Nacimiento",
        "comuna_id_comuna": "Comuna",
        "nacionalidad_id_nacionalidad": "Pais"
    }
        widgets = {
            'fe_naci': forms.SelectDateWidget(years=DOY)
            }
        
class FormCheckIn(forms.ModelForm):
    class Meta:
        model = ReservaDepartamento
        fields = [
            'id_reserva',
            'fecha_ini',
            'fecha_fin',
            'cliente_id_cliente',
        ]
        labels ={
            'id_reserva' : 'Reserva ID',
            'fecha_ini' : 'Fecha Inicio',
            'fecha_fin' : 'Fecha Final',
            'cliente_id_cliente' : 'Id del Cliente',
        }
