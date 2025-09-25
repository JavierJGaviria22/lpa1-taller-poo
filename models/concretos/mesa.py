"""
Clase concreta Mesa.
"""
from models.categorias.superficies import Superficie

class Mesa(Superficie):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 area: float, forma: str = "rectangular", altura: float = 75, extensible: bool = False):
        super().__init__(nombre, material, color, precio_base, area, forma, altura)
        self._extensible = extensible

    @property
    def extensible(self) -> bool:
        """Indica si la mesa es extensible."""
        return self._extensible

    @extensible.setter
    def extensible(self, value: bool) -> None:
        self._extensible = bool(value)

    def calcular_precio(self) -> float:
        """
        Calcula el precio de la mesa según sus características.
        """
        precio = self.precio_base
        precio += self.area * 100  # precio por m2
        if self.forma.lower() == "circular":
            precio += 150
        if self.extensible:
            precio += 200
        if self.altura > 80:
            precio += 50
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa de la mesa.
        """
        descripcion = f"Mesa {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_superficie()}"
        descripcion += f"\nExtensible: {'Sí' if self.extensible else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Mesa {self.nombre} ({'extensible' if self.extensible else 'fija'})"