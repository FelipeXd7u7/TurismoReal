from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',index, name='index'),
    #path('registro/',registro_usuario, name='registro_usuario'),
    path('registro/',registro_usuario, name='registro_usuario'),
    path('registroCliente/',registro_cliente, name='registro_cliente'),
    
    #Departamentos
    
    path('departamento1/',departamento1, name='departamento1'),
    path('departamento2/',departamento2, name='departamento2'),
    path('departamento3/',departamento3, name='departamento3'),
    path('departamento4/',departamento4, name='departamento4'),
    path('departamento5/',departamento5, name='departamento5'),
    path('departamento6/',departamento6, name='departamento6'),
    path('departamento7/',departamento7, name='departamento7'),
    path('departamento8/',departamento7, name='departamento8'),
    path('departamento9/',departamento7, name='departamento9'),
    path('departamento10/',departamento7, name='departamento10'),

    path('depa1/',depa1, name='depa1'),

    
    
    #Ignorar Test
    #path('login',login_required,{'template_name':'login.html'}, name='login'),
    path('Test/',Test, name='Test'),
    path('Checkin/',Checkin, name='Checkin'),
]

urlpatterns+= staticfiles_urlpatterns()