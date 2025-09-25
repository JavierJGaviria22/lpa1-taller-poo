"""
Servicio de catálogo de muebles.
Permite listar, buscar y filtrar muebles disponibles en la tienda.
"""

from typing import List, Optional
from ..models.mueble import Mueble

class Catalogo:
	"""
	Clase que gestiona el catálogo de muebles.
	"""
	def __init__(self, muebles: Optional[List[Mueble]] = None):
		self._muebles = muebles if muebles is not None else []

	def agregar_mueble(self, mueble: Mueble) -> str:
		if not isinstance(mueble, Mueble):
			return "Solo se pueden agregar objetos de tipo Mueble."
		self._muebles.append(mueble)
		return f"Mueble '{mueble.nombre}' agregado al catálogo."

	def listar_muebles(self) -> List[Mueble]:
		return self._muebles.copy()

	def buscar_por_nombre(self, nombre: str) -> List[Mueble]:
		if not nombre or not nombre.strip():
			return []
		nombre_lower = nombre.lower().strip()
		return [m for m in self._muebles if nombre_lower in m.nombre.lower()]

	def filtrar_por_material(self, material: str) -> List[Mueble]:
		if not material or not material.strip():
			return []
		material_lower = material.lower().strip()
		return [m for m in self._muebles if m.material.lower() == material_lower]

	def filtrar_por_precio(self, precio_min: float = 0, precio_max: float = float('inf')) -> List[Mueble]:
		resultados = []
		for m in self._muebles:
			try:
				precio = m.calcular_precio()
				if precio_min <= precio <= precio_max:
					resultados.append(m)
			except Exception:
				continue
		return resultados

	def obtener_descripciones(self) -> List[str]:
		return [m.obtener_descripcion() for m in self._muebles]