from django.db import models
from django.contrib import admin


class Empleado(models.Model):
    imagen = models.ImageField(upload_to='empleados/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    cliente_referido = models.ForeignKey('Cliente', on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    producto_asignado = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='clientes_asignados')
    producto_interes = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='ventas_realizadas')
    producto = models.CharField(max_length=200)
    fecha_venta = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=100)
    folio = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Venta {self.folio} - {self.cliente}"

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    calle = models.CharField(max_length=255)
    CP = models.CharField(max_length=10)

    def __str__(self):
        return self.direccion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    edad_minima = models.IntegerField()
    clasificacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    imagen = models.ImageField(upload_to='videojuegos/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    descripcion = models.TextField()
    ano_lanzamiento = models.IntegerField()
    compania = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    nombre_juego = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_juego} - {self.plataforma}"


admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Venta)
admin.site.register(Sucursal)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Videojuego)
admin.site.register(Inventario)
