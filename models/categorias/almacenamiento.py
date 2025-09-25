
"""
Clase abstracta para muebles de almacenamiento (armarios, cajoneras, etc).
"""

from ..mueble import Mueble
from abc import abstractmethod

class Almacenamiento(Mueble):
	"""
	Clase abstracta para muebles que almacenan objetos.
	Agrupa características comunes de armarios, cajoneras, etc.
	"""
	def __init__(self, nombre: str, material: str, color: str, precio_base: float,
				 num_puertas: int = 0, num_cajones: int = 0, tiene_espejos: bool = False):
		super().__init__(nombre, material, color, precio_base)
		self._num_puertas = num_puertas
		self._num_cajones = num_cajones
		self._tiene_espejos = tiene_espejos

	@property
	def num_puertas(self) -> int:
		return self._num_puertas

	@num_puertas.setter
	def num_puertas(self, value: int) -> None:
		if value < 0:
			raise ValueError("El número de puertas no puede ser negativo")
		self._num_puertas = value

	@property
	def num_cajones(self) -> int:
		return self._num_cajones

	@num_cajones.setter
	def num_cajones(self, value: int) -> None:
		if value < 0:
			raise ValueError("El número de cajones no puede ser negativo")
		self._num_cajones = value

	@property
	def tiene_espejos(self) -> bool:
		return self._tiene_espejos

	@tiene_espejos.setter
	def tiene_espejos(self, value: bool) -> None:
		self._tiene_espejos = bool(value)

	def obtener_info_almacenamiento(self) -> str:
		info = f"Puertas: {self.num_puertas}, Cajones: {self.num_cajones}"
		info += f", Espejos: {'Sí' if self.tiene_espejos else 'No'}"
		return info

	@abstractmethod
	def calcular_precio(self) -> float:
		pass

	@abstractmethod
	def obtener_descripcion(self) -> str:
		pass
