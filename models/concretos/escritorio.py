"""
Clase concreta Escritorio.
"""
from models.categorias.superficies import Superficie

class Escritorio(Superficie):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 area: float, forma: str = "rectangular", altura: float = 75,
                 tiene_cajones: bool = False, cantidad_cajones: int = 0):
        super().__init__(nombre, material, color, precio_base, area, forma, altura)
        self._tiene_cajones = tiene_cajones
        self._cantidad_cajones = cantidad_cajones if tiene_cajones else 0

    @property
    def tiene_cajones(self) -> bool:
        """Indica si el escritorio tiene cajones."""
        return self._tiene_cajones

    @tiene_cajones.setter
    def tiene_cajones(self, value: bool) -> None:
        self._tiene_cajones = bool(value)
        if not self._tiene_cajones:
            self._cantidad_cajones = 0

    @property
    def cantidad_cajones(self) -> int:
        """Cantidad de cajones en el escritorio."""
        return self._cantidad_cajones

    @cantidad_cajones.setter
    def cantidad_cajones(self, value: int) -> None:
        if not self.tiene_cajones:
            self._cantidad_cajones = 0
        else:
            if value < 0:
                raise ValueError("La cantidad de cajones no puede ser negativa")
            self._cantidad_cajones = value

    def calcular_precio(self) -> float:
        """
        Calcula el precio del escritorio según sus características.
        """
        precio = self.precio_base
        precio += self.area * 120  # escritorio suele ser más caro por m2
        if self.forma.lower() == "esquinero":
            precio += 200
        if self.tiene_cajones:
            precio += 80 * self.cantidad_cajones
        if self.altura > 80:
            precio += 40
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del escritorio.
        """
        descripcion = f"Escritorio {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_superficie()}"
        descripcion += f"\nCajones: {'Sí' if self.tiene_cajones else 'No'}"
        if self.tiene_cajones:
            descripcion += f", Cantidad: {self.cantidad_cajones}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Escritorio {self.nombre} ({'con cajones' if self.tiene_cajones else 'sin cajones'})"