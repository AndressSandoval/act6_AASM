# TODO List for Adding New Models and CRUD Interfaces

## Step 1: Add New Models to models.py and Register in admin.py ✅ COMPLETED
- Added SUCURSAL, PROVEEDOR, CATEGORIA, VIDEOJUEGO, INVENTARIO models with exact fields and relationships.
- Registered all new models in admin.site.register.

## Step 2: Add CRUD Views to views.py ✅ COMPLETED
- Added views for SUCURSAL: agregar_sucursal, ver_sucursales, actualizar_sucursal, borrar_sucursal.
- Added views for PROVEEDOR: agregar_proveedor, ver_proveedores, actualizar_proveedor, borrar_proveedor.
- Added views for CATEGORIA: agregar_categoria, ver_categorias, actualizar_categoria, borrar_categoria.
- Added views for VIDEOJUEGO: agregar_videojuego, ver_videojuegos, actualizar_videojuego, borrar_videojuego.
- Added views for INVENTARIO: agregar_inventario, ver_inventarios, actualizar_inventario, borrar_inventario.
- Ensured foreign key selections are handled properly in add/update views.

## Step 3: Add URL Patterns to urls.py ✅ COMPLETED
- Added paths for all new CRUD views, following the existing pattern (e.g., path('agregar_sucursal/', views.agregar_sucursal, name='agregar_sucursal')).

## Step 4: Create Templates ✅ COMPLETED
- Created folder app_Videojuegos/templates/sucursal/ with files: agregar_sucursal.html, ver_sucursales.html, actualizar_sucursal.html, borrar_sucursal.html.
- Created folder app_Videojuegos/templates/proveedor/ with files: agregar_proveedor.html, ver_proveedores.html, actualizar_proveedor.html, borrar_proveedor.html.
- Created folder app_Videojuegos/templates/categoria/ with files: agregar_categoria.html, ver_categorias.html, actualizar_categoria.html, borrar_categoria.html.
- Created folder app_Videojuegos/templates/videojuego/ with files: agregar_videojuego.html, ver_videojuegos.html, actualizar_videojuego.html, borrar_videojuego.html.
- Created folder app_Videojuegos/templates/inventario/ with files: agregar_inventario.html, ver_inventarios.html, actualizar_inventario.html, borrar_inventario.html.
- Based templates on existing cliente templates, adapting field names and foreign key selects.

## Step 5: Update navbar.html
- Add dropdown for Sucursales with Agregar Sucursal and Ver Sucursales.
- Add dropdown for Proveedores with Agregar Proveedor and Ver Proveedores.
- Add dropdown for Inventarios with Agregar Inventario and Ver Inventarios.
- Add dropdown for Categorias with Agregar Categoria and Ver Categorias.
- Add dropdown for Videojuegos with Agregar Videojuego and Ver Videojuegos.

## Step 6: Update inicio.html ✅ COMPLETED
- Added buttons/cards for each new model to link to their ver_ pages.

## Step 7: Followup - Run Migrations and Test ✅ COMPLETED
- Ran python manage.py makemigrations and python manage.py migrate.
- Tested all CRUD interfaces.
