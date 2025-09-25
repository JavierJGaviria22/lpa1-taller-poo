
import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor

def crear_silla():
		# nombre, material, color, precio_base, tiene_respaldo, material_tapizado, altura_regulable, tiene_ruedas
		return Silla(
			nombre="Silla Test",
			material="madera",
			color="rojo",
			precio_base=100,
			tiene_respaldo=True,
			material_tapizado="tela",
			altura_regulable=True,
			tiene_ruedas=True
		)

def crear_mesa():
		# nombre, material, color, precio_base, forma, capacidad_personas, area_superficie, extensible
		return Mesa(
			nombre="Mesa Test",
			material="madera",
			color="roble",
			precio_base=500,
			forma="rectangular",
			capacidad_personas=4,
			area_superficie=1.5,
			extensible=False
		)

def test_agregar_mueble():
	tienda = TiendaMuebles("Tienda Prueba")
	silla = crear_silla()
	msg = tienda.agregar_mueble(silla)
	assert "agregado" in msg
	assert silla in tienda._inventario

def test_agregar_mueble_invalido():
	tienda = TiendaMuebles()
	msg = tienda.agregar_mueble("no es mueble")
	assert "Solo se pueden agregar" in msg

def test_agregar_comedor():
	tienda = TiendaMuebles()
	mesa = crear_mesa()
	silla = crear_silla()
	comedor = Comedor("Comedor Test", mesa, [silla])
	msg = tienda.agregar_comedor(comedor)
	assert "agregado exitosamente" in msg
	assert comedor in tienda._comedores

def test_buscar_muebles_por_nombre():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	resultados = tienda.buscar_muebles_por_nombre("Silla")
	assert silla in resultados

def test_filtrar_por_precio():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	resultados = tienda.filtrar_por_precio(50, 150)
	assert silla in resultados

def test_filtrar_por_material():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	resultados = tienda.filtrar_por_material("madera")
	assert silla in resultados

def test_obtener_muebles_por_tipo():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	resultados = tienda.obtener_muebles_por_tipo(type(silla))
	assert silla in resultados

def test_calcular_valor_inventario():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	valor = tienda.calcular_valor_inventario()
	assert valor > 0

def test_aplicar_descuento():
	tienda = TiendaMuebles()
	msg = tienda.aplicar_descuento("silla", 10)
	assert "Descuento del 10%" in msg

def test_realizar_venta():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	venta = tienda.realizar_venta(silla, "Cliente Test")
	assert "precio_final" in venta
	assert silla not in tienda._inventario

def test_obtener_estadisticas():
	tienda = TiendaMuebles()
	stats = tienda.obtener_estadisticas()
	assert isinstance(stats, dict)
	assert "total_muebles" in stats

def test_contar_tipos_muebles():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	conteo = tienda._contar_tipos_muebles()
	assert "Silla" in conteo

def test_generar_reporte_inventario():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	reporte = tienda.generar_reporte_inventario()
	assert "INVENTARIO" in reporte.upper()

# Herencia y polimorfismo
def test_herencia_tienda():
	tienda = TiendaMuebles()
	assert isinstance(tienda, TiendaMuebles)
	assert hasattr(tienda, "agregar_mueble")

def test_polimorfismo_muebles():
	tienda = TiendaMuebles()
	class SillaEspecial(Silla):
		def calcular_precio(self):
			return 999
	silla = SillaEspecial("Silla Poli", "plastico", "verde", 80, True, "tela", False, False)
	tienda.agregar_mueble(silla)
	resultados = tienda.filtrar_por_precio(900, 1000)
	assert silla in resultados

# Edge cases y validaciones
def test_buscar_nombre_vacio():
	tienda = TiendaMuebles()
	assert tienda.buscar_muebles_por_nombre("") == []
	assert tienda.buscar_muebles_por_nombre("   ") == []

def test_filtrar_material_vacio():
	tienda = TiendaMuebles()
	assert tienda.filtrar_por_material("") == []
	assert tienda.filtrar_por_material("   ") == []

def test_filtrar_precio_edge():
	tienda = TiendaMuebles()
	silla = crear_silla()
	tienda.agregar_mueble(silla)
	resultados = tienda.filtrar_por_precio(-100, 100)
	assert silla in resultados