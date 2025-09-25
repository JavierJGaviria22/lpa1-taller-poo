
import pytest
from models.composicion.comedor import Comedor
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla

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

def crear_silla():
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

def test_comedor_agregar_silla():
	mesa = crear_mesa()
	silla = crear_silla()
	comedor = Comedor("Comedor Prueba", mesa, [silla])
	nueva_silla = Silla("Silla Nueva", "metal", "azul", 120, True, "cuero", False, False)
	msg = comedor.agregar_silla(nueva_silla)
	assert "agregada" in msg
	assert nueva_silla in comedor.sillas

def test_comedor_quitar_silla():
	mesa = crear_mesa()
	silla1 = crear_silla()
	silla2 = Silla("Silla2", "metal", "azul", 120, True, "cuero", False, False)
	comedor = Comedor("Comedor Prueba", mesa, [silla1, silla2])
	msg = comedor.quitar_silla(0)
	assert "removida" in msg
	assert silla1 not in comedor.sillas

def test_comedor_precio_total():
	mesa = crear_mesa()
	silla1 = crear_silla()
	silla2 = Silla("Silla2", "metal", "azul", 120, True, "cuero", False, False)
	comedor = Comedor("Comedor Prueba", mesa, [silla1, silla2])
	total = comedor.calcular_precio_total()
	assert total > 0

def test_comedor_descripcion_completa():
	mesa = crear_mesa()
	silla1 = crear_silla()
	comedor = Comedor("Comedor Prueba", mesa, [silla1])
	desc = comedor.obtener_descripcion_completa()
	assert "COMEDOR" in desc.upper()
	assert "MESA" in desc.upper()
	assert "SILLA" in desc.upper()

def test_comedor_capacidad_maxima():
	mesa = crear_mesa()
	comedor = Comedor("Comedor Prueba", mesa, [])
	capacidad = comedor._calcular_capacidad_maxima()
	assert isinstance(capacidad, int)
	assert capacidad > 0

def test_comedor_resumen():
	mesa = crear_mesa()
	silla1 = crear_silla()
	comedor = Comedor("Comedor Prueba", mesa, [silla1])
	resumen = comedor.obtener_resumen()
	assert "nombre" in resumen
	assert "precio_total" in resumen

# Herencia y polimorfismo
def test_comedor_herencia():
	mesa = crear_mesa()
	silla = crear_silla()
	comedor = Comedor("Comedor Herencia", mesa, [silla])
	assert isinstance(comedor, Comedor)
	assert hasattr(comedor, "agregar_silla")
	assert hasattr(comedor, "calcular_precio_total")

def test_polimorfismo_sillas():
	mesa = crear_mesa()
	class SillaEspecial(Silla):
		def obtener_descripcion(self):
			return "Silla Especial"
	silla = SillaEspecial("Silla Poli", "plastico", "verde", 80, True, "tela", False, False)
	comedor = Comedor("Comedor Poli", mesa, [silla])
	desc = comedor.obtener_descripcion_completa()
	assert "Silla Especial" in desc

# Edge cases y validaciones
def test_quitar_silla_vacia():
	mesa = crear_mesa()
	comedor = Comedor("Comedor Edge", mesa, [])
	msg = comedor.quitar_silla()
	assert "No hay sillas" in msg

def test_agregar_silla_invalida():
	mesa = crear_mesa()
	comedor = Comedor("Comedor Edge", mesa, [])
	msg = comedor.agregar_silla("no es silla")
	assert "Solo se pueden agregar" in msg