"""
Clase concreta Mesa.
"""
from models.categorias.superficies import Superficie


class Mesa(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str = "rectangular", capacidad_personas: int = 4, area_superficie: float = 1.5, extensible: bool = False):
        super().__init__(nombre, material, color, precio_base, forma, area_superficie)
        self._capacidad_personas = capacidad_personas
        self._extensible = extensible

    @property
    def capacidad_personas(self) -> int:
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        if value < 1:
            raise ValueError("La mesa debe tener capacidad para al menos 1 persona")
        self._capacidad_personas = value

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
        precio += self.area_superficie * 100  # precio por m2
        if self.forma.lower() in ["circular", "redonda"]:
            precio += 150
        if self.extensible:
            precio += 200
        # Capacidad: cada persona extra suma 50
        if self.capacidad_personas > 4:
            precio += 50 * (self.capacidad_personas - 4)
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa de la mesa.
        """
        descripcion = f"Mesa {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_superficie()}"
        descripcion += f"\nCapacidad: {self.capacidad_personas} personas"
        descripcion += f"\nExtensible: {'Sí' if self.extensible else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Mesa {self.nombre} para {self.capacidad_personas} personas ({'extensible' if self.extensible else 'fija'})"