from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from flake.models import Persona

# Registrar el modelo Persona en el panel de administración
admin.site.register(Persona)

# Crear y registrar los grupos de 'Administrador' y 'Tutor'
def create_groups():
    # Crear grupo de Administradores
    admin_group, created = Group.objects.get_or_create(name='Administrador')
    
    # Crear grupo de Tutores
    tutor_group, created = Group.objects.get_or_create(name='Tutor')

    # Asignar permisos si es necesario, por ejemplo:
    # admin_group.permissions.add(Permission.objects.get(codename='can_add_persona'))

# Puedes ejecutar esta función una vez para crear los grupos automáticamente si no existen
# Para ejecutarla puedes agregarla al archivo `apps.py` en el método `ready` de la aplicación.
create_groups()

# Personalización de la interfaz de administración del modelo User
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Mostrar el campo 'groups' en el formulario de edición de usuarios
    filter_horizontal = ('groups',)

# Registrar el modelo User con el UserAdmin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
