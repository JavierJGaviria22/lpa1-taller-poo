
"""
Clase abstracta para muebles que sirven como superficies de trabajo o del hogar.
Ejemplos: mesas, escritorios, etc.
"""

from ..mueble import Mueble
from abc import abstractmethod

class Superficie(Mueble):
	"""
	Clase abstracta para muebles que proporcionan una superficie de uso.
	Agrupa características comunes de mesas, escritorios, etc.
	"""
	def __init__(self, nombre: str, material: str, color: str, precio_base: float,
				 forma: str, area_superficie: float):
		super().__init__(nombre, material, color, precio_base)
		self._forma = forma  # Ejemplo: rectangular, redonda, cuadrada
		self._area_superficie = area_superficie  # en metros cuadrados

	@property
	def forma(self) -> str:
		return self._forma

	@forma.setter
	def forma(self, value: str) -> None:
		if not value or not value.strip():
			raise ValueError("La forma no puede estar vacía")
		self._forma = value.strip()

	@property
	def area_superficie(self) -> float:
		return self._area_superficie

	@area_superficie.setter
	def area_superficie(self, value: float) -> None:
		if value <= 0:
			raise ValueError("El área debe ser mayor a 0")
		self._area_superficie = value

	def obtener_info_superficie(self) -> str:
		info = f"Forma: {self.forma}, Área: {self.area_superficie} m²"
		return info

	@abstractmethod
	def calcular_precio(self) -> float:
		pass

	@abstractmethod
	def obtener_descripcion(self) -> str:
		pass
