"""
Clase concreta Cajonera.
"""
from models.categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_cajones: int = 3, tiene_ruedas: bool = False):
        super().__init__(nombre, material, color, precio_base, 0, num_cajones, False)
        self._tiene_ruedas = tiene_ruedas

    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = bool(value)

    def calcular_precio(self) -> float:
        """
        Calcula el precio de la cajonera según sus características.
        """
        precio = self.precio_base
        precio += 70 * self.num_cajones
        if self.tiene_ruedas:
            precio += 50
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa de la cajonera.
        """
        descripcion = f"Cajonera {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\nCajones: {self.num_cajones}"
        descripcion += f"\nRuedas: {'Sí' if self.tiene_ruedas else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Cajonera {self.nombre} ({self.num_cajones} cajones{' con ruedas' if self.tiene_ruedas else ''})"