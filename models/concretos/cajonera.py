"""
Clase concreta Cajonera.
"""
from models.categorias.almacenamiento import Almacenamiento

class Cajonera(Almacenamiento):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad: float, tipo_apertura: str = "cajones", cantidad_cajones: int = 3):
        super().__init__(nombre, material, color, precio_base, capacidad, tipo_apertura)
        self._cantidad_cajones = cantidad_cajones

    @property
    def cantidad_cajones(self) -> int:
        """Cantidad de cajones en la cajonera."""
        return self._cantidad_cajones

    @cantidad_cajones.setter
    def cantidad_cajones(self, value: int) -> None:
        if value < 1:
            raise ValueError("La cajonera debe tener al menos un cajón")
        self._cantidad_cajones = value

    def calcular_precio(self) -> float:
        """
        Calcula el precio de la cajonera según sus características.
        """
        precio = self.precio_base
        precio += self.capacidad * 80  # precio por litro de capacidad
        precio += 60 * self.cantidad_cajones
        if self.tipo_apertura.lower() == "push":
            precio += 40
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa de la cajonera.
        """
        descripcion = f"Cajonera {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_descripcion()}"
        descripcion += f"\nCantidad de cajones: {self.cantidad_cajones}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Cajonera {self.nombre} ({self.cantidad_cajones} cajones)"