from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Venta, Sucursal, Proveedor, Categoria, Videojuego, Inventario
from django.http import HttpResponse

# Vista de inicio
def inicio_videojuegos(request):
    return render(request, 'cliente/inicio.html')

# Agregar Cliente
def agregar_cliente(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        empleado_obj = None
        if empleado_id:
            try:
                empleado_obj = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                empleado_obj = None

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion,
            empleado_asignado=empleado_obj,
            producto_interes=producto_interes,
            imagen=imagen
        )
        return redirect('ver_clientes')

    return render(request, 'cliente/agregar_cliente.html', {'empleados': empleados})

# Ver Clientes
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# Actualizar Cliente
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        cliente.producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        if empleado_id:
            try:
                cliente.empleado_asignado = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                cliente.empleado_asignado = None
        else:
            cliente.empleado_asignado = None

        if imagen:
            cliente.imagen = imagen

        cliente.save()
        return redirect('ver_clientes')

    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente, 'empleados': empleados})

# Borrar Cliente
def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# Agregar Empleado
def agregar_empleado(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        cliente_id = request.POST.get('cliente_referido')
        producto_asignado = request.POST.get('producto_asignado')
        imagen = request.FILES.get('imagen')

        cliente_obj = None
        if cliente_id:
            try:
                cliente_obj = Cliente.objects.get(id=cliente_id)
            except Cliente.DoesNotExist:
                cliente_obj = None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            cliente_referido=cliente_obj,
            producto_asignado=producto_asignado,
            imagen=imagen
        )
        return redirect('ver_empleados')

    return render(request, 'cliente/agregar_empleado.html', {'clientes': clientes})

# Ver Empleados
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'cliente/ver_empleados.html', {'empleados': empleados})

# Actualizar Empleado
def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        cliente_id = request.POST.get('cliente_referido')
        empleado.producto_asignado = request.POST.get('producto_asignado')
        imagen = request.FILES.get('imagen')

        if cliente_id:
            try:
                empleado.cliente_referido = Cliente.objects.get(id=cliente_id)
            except Cliente.DoesNotExist:
                empleado.cliente_referido = None
        else:
            empleado.cliente_referido = None

        if imagen:
            empleado.imagen = imagen

        empleado.save()
        return redirect('ver_empleados')

    return render(request, 'cliente/actualizar_empleado.html', {'empleado': empleado, 'clientes': clientes})

# Borrar Empleado
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'cliente/borrar_empleado.html', {'empleado': empleado})

# Agregar Venta
def agregar_venta(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        empleado_id = request.POST.get('empleado')
        producto = request.POST.get('producto')
        monto_total = request.POST.get('monto_total')
        metodo_pago = request.POST.get('metodo_pago')
        folio = request.POST.get('folio')

        cliente_obj = get_object_or_404(Cliente, id=cliente_id)
        empleado_obj = None
        if empleado_id:
            empleado_obj = get_object_or_404(Empleado, id=empleado_id)

        Venta.objects.create(
            cliente=cliente_obj,
            empleado=empleado_obj,
            producto=producto,
            monto_total=monto_total,
            metodo_pago=metodo_pago,
            folio=folio
        )
        return redirect('ver_ventas')

    return render(request, 'cliente/agregar_venta.html', {'clientes': clientes, 'empleados': empleados})

# Ver Ventas
def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'cliente/ver_ventas.html', {'ventas': ventas})

# Actualizar Venta
def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        venta.cliente = get_object_or_404(Cliente, id=request.POST.get('cliente'))
        empleado_id = request.POST.get('empleado')
        venta.empleado = get_object_or_404(Empleado, id=empleado_id) if empleado_id else None
        venta.producto = request.POST.get('producto')
        venta.monto_total = request.POST.get('monto_total')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.folio = request.POST.get('folio')
        venta.save()
        return redirect('ver_ventas')

    return render(request, 'cliente/actualizar_venta.html', {'venta': venta, 'clientes': clientes, 'empleados': empleados})

# Borrar Venta
def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'cliente/borrar_venta.html', {'venta': venta})

# Agregar Sucursal
def agregar_sucursal(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        calle = request.POST.get('calle')
        CP = request.POST.get('CP')

        Sucursal.objects.create(
            direccion=direccion,
            ciudad=ciudad,
            pais=pais,
            calle=calle,
            CP=CP
        )
        return redirect('ver_sucursales')

    return render(request, 'sucursal/agregar_sucursal.html')

# Ver Sucursales
def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

# Actualizar Sucursal
def actualizar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.direccion = request.POST.get('direccion')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.pais = request.POST.get('pais')
        sucursal.calle = request.POST.get('calle')
        sucursal.CP = request.POST.get('CP')
        sucursal.save()
        return redirect('ver_sucursales')

    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

# Borrar Sucursal
def borrar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# Agregar Proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')

        Proveedor.objects.create(
            nombre=nombre,
            contacto=contacto,
            telefono=telefono
        )
        return redirect('ver_proveedores')

    return render(request, 'proveedor/agregar_proveedor.html')

# Ver Proveedores
def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

# Actualizar Proveedor
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.save()
        return redirect('ver_proveedores')

    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

# Borrar Proveedor
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# Agregar Categoria
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad_minima = request.POST.get('edad_minima')
        clasificacion = request.POST.get('clasificacion')

        Categoria.objects.create(
            nombre=nombre,
            edad_minima=edad_minima,
            clasificacion=clasificacion
        )
        return redirect('ver_categorias')

    return render(request, 'categoria/agregar_categoria.html')

# Ver Categorias
def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

# Actualizar Categoria
def actualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.edad_minima = request.POST.get('edad_minima')
        categoria.clasificacion = request.POST.get('clasificacion')
        categoria.save()
        return redirect('ver_categorias')

    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})

# Borrar Categoria
def borrar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})

# Agregar Videojuego
def agregar_videojuego(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        duracion = request.POST.get('duracion')
        descripcion = request.POST.get('descripcion')
        ano_lanzamiento = request.POST.get('ano_lanzamiento')
        compania = request.POST.get('compania')
        id_categoria = request.POST.get('id_categoria')
        imagen = request.FILES.get('imagen')

        try:
            categoria_obj = Categoria.objects.get(pk=id_categoria)
        except (ValueError, Categoria.DoesNotExist):
            context = {
                'categorias': categorias,
                'error': 'Asegúrese de seleccionar una categoría válida.'
            }
            return render(request, 'videojuego/agregar_videojuego.html', context)

        Videojuego.objects.create(
            nombre=nombre,
            duracion=duracion,
            descripcion=descripcion,
            ano_lanzamiento=ano_lanzamiento,
            compania=compania,
            categoria=categoria_obj,
            imagen=imagen
        )
        return redirect('ver_videojuegos')

    return render(request, 'videojuego/agregar_videojuego.html', {'categorias': categorias})

# Ver Videojuegos
def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'videojuego/ver_videojuegos.html', {'videojuegos': videojuegos})

# Actualizar Videojuego
def actualizar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    categorias = Categoria.objects.all()
    
    context = {
        'videojuego': videojuego,
        'categorias': categorias
    }

    if request.method == 'POST':
        id_categoria = request.POST.get('id_categoria')
        
        try:
            categoria_obj = Categoria.objects.get(pk=id_categoria)
        except (ValueError, Categoria.DoesNotExist):
            context['error'] = 'Asegúrese de seleccionar una categoría válida.'
            return render(request, 'videojuego/actualizar_videojuego.html', context)

        videojuego.nombre = request.POST.get('nombre')
        videojuego.duracion = request.POST.get('duracion')
        videojuego.descripcion = request.POST.get('descripcion')
        videojuego.ano_lanzamiento = request.POST.get('ano_lanzamiento')
        videojuego.compania = request.POST.get('compania')
        videojuego.categoria = categoria_obj
        
        imagen = request.FILES.get('imagen')
        if imagen:
            videojuego.imagen = imagen
            
        videojuego.save()
        return redirect('ver_videojuegos')

    return render(request, 'videojuego/actualizar_videojuego.html', context)

# Borrar Videojuego
def borrar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('ver_videojuegos')
    return render(request, 'videojuego/borrar_videojuego.html', {'videojuego': videojuego})

# Agregar Inventario
def agregar_inventario(request):
    videojuegos = Videojuego.objects.all()
    sucursales = Sucursal.objects.all()
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        id_videojuego = request.POST.get('id_videojuego')
        id_direccion = request.POST.get('id_direccion')
        nombre_juego = request.POST.get('nombre_juego')
        plataforma = request.POST.get('plataforma')
        proveedor_id = request.POST.get('proveedor')

        try:
            # Ensure IDs are actual numbers and correspond to existing objects
            videojuego_obj = Videojuego.objects.get(pk=id_videojuego)
            sucursal_obj = Sucursal.objects.get(pk=id_direccion)
            proveedor_obj = Proveedor.objects.get(pk=proveedor_id)
        except (ValueError, Videojuego.DoesNotExist, Sucursal.DoesNotExist, Proveedor.DoesNotExist):
            # This will catch empty strings (ValueError) or invalid IDs (DoesNotExist)
            # Re-render the form. User input is lost but crash is prevented.
            context = {
                'videojuegos': videojuegos,
                'sucursales': sucursales,
                'proveedores': proveedores,
                'error': 'Asegúrese de que todos los campos estén completos y sean válidos.'
            }
            return render(request, 'inventario/agregar_inventario.html', context)

        Inventario.objects.create(
            videojuego=videojuego_obj,
            sucursal=sucursal_obj,
            nombre_juego=nombre_juego,
            plataforma=plataforma,
            proveedor=proveedor_obj
        )
        return redirect('ver_inventarios')

    return render(request, 'inventario/agregar_inventario.html', {'videojuegos': videojuegos, 'sucursales': sucursales, 'proveedores': proveedores})

# Ver Inventarios
def ver_inventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario/ver_inventarios.html', {'inventarios': inventarios})

# Actualizar Inventario
def actualizar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    videojuegos = Videojuego.objects.all()
    sucursales = Sucursal.objects.all()
    proveedores = Proveedor.objects.all()
    
    context = {
        'inventario': inventario,
        'videojuegos': videojuegos,
        'sucursales': sucursales,
        'proveedores': proveedores
    }

    if request.method == 'POST':
        id_videojuego = request.POST.get('id_videojuego')
        id_direccion = request.POST.get('id_direccion')
        proveedor_id = request.POST.get('proveedor')
        nombre_juego = request.POST.get('nombre_juego')
        plataforma = request.POST.get('plataforma')

        try:
            videojuego_obj = Videojuego.objects.get(pk=id_videojuego)
            sucursal_obj = Sucursal.objects.get(pk=id_direccion)
            proveedor_obj = Proveedor.objects.get(pk=proveedor_id)
        except (ValueError, Videojuego.DoesNotExist, Sucursal.DoesNotExist, Proveedor.DoesNotExist):
            context['error'] = 'Asegúrese de que todos los campos estén completos y sean válidos.'
            return render(request, 'inventario/actualizar_inventario.html', context)

        inventario.videojuego = videojuego_obj
        inventario.sucursal = sucursal_obj
        inventario.proveedor = proveedor_obj
        inventario.nombre_juego = nombre_juego
        inventario.plataforma = plataforma
        
        inventario.save()
        return redirect('ver_inventarios')

    return render(request, 'inventario/actualizar_inventario.html', context)

# Borrar Inventario
def borrar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('ver_inventarios')
    return render(request, 'inventario/borrar_inventario.html', {'inventario': inventario})
