"""
Clase concreta Cama.
"""
from models.mueble import Mueble

class Cama(Mueble):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tamaño: str = "matrimonial", incluye_colchon: bool = True):
        super().__init__(nombre, material, color, precio_base)
        self._tamaño = tamaño
        self._incluye_colchon = incluye_colchon

    @property
    def tamaño(self) -> str:
        """Tamaño de la cama (individual, matrimonial, queen, king)."""
        return self._tamaño

    @tamaño.setter
    def tamaño(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El tamaño de la cama no puede estar vacío")
        self._tamaño = value.strip()

    @property
    def incluye_colchon(self) -> bool:
        """Indica si la cama incluye colchón."""
        return self._incluye_colchon

    @incluye_colchon.setter
    def incluye_colchon(self, value: bool) -> None:
        self._incluye_colchon = bool(value)

    def calcular_precio(self) -> float:
        """
        Calcula el precio de la cama según sus características.
        """
        precio = self.precio_base
        if self.tamaño.lower() == "queen":
            precio += 400
        elif self.tamaño.lower() == "king":
            precio += 600
        elif self.tamaño.lower() == "matrimonial":
            precio += 200
        elif self.tamaño.lower() == "individual":
            precio += 0
        else:
            precio += 100
        if self.incluye_colchon:
            precio += 350
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa de la cama.
        """
        descripcion = f"Cama {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\nTamaño: {self.tamaño}"
        descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Cama {self.nombre} ({self.tamaño})"