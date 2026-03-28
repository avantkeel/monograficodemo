# Proyecto Django

## Tarea 2: Employee Manager

La carpeta `source/django/core/application/employeemanager` corresponde a la **Tarea 2** del proyecto.  

### Descripción

Esta aplicación dentro del proyecto Django tiene como objetivo gestionar información de empleados de manera sencilla. Permite:

- Listar empleados.
- Agregar nuevos empleados.
- Actualizar datos existentes.

La aplicación está pensada como un **módulo independiente**, para que pueda integrarse fácilmente dentro del proyecto principal. Contiene:

- `models.py` – Define el modelo `Employee` con los campos necesarios (nombre, cargo, salario, etc.).
- `views.py` – Contiene las vistas y endpoints para manejar los empleados.
- `urls.py` – Define las rutas asociadas a la gestión de empleados, por ejemplo `/app/employees/`.
- `templates/` – Plantillas HTML para listar y gestionar empleados (si aplica).
- `admin.py` – Registro de modelos para el panel de administración de Django.
- `migrations/` – Migraciones de base de datos para crear las tablas necesarias.

### Integración en el proyecto

Para usar esta aplicación dentro del proyecto principal:

1. Asegúrate de que `applications.employeemanager` esté incluida en `INSTALLED_APPS` del `settings.py`.
2. Incluye sus URLs en `app/urls.py`:
