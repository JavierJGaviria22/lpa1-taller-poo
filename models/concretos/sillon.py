"""
Clase concreta Sillón.
Hereda de Asiento y representa un sillón individual.
"""

from models.categorias.asientos import Asiento

class Sillon(Asiento):
    """
    Clase concreta para sillón individual.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = "tela"):
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)

    def calcular_precio(self) -> float:
        """
        Calcula el precio del sillón según sus características.
        """
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        if self.material_tapizado and self.material_tapizado.lower() == "cuero":
            precio += 300
        elif self.material_tapizado and self.material_tapizado.lower() == "tela":
            precio += 100
        if self.tiene_respaldo:
            precio += 50
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del sillón.
        """
        descripcion = f"Sillón {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Sillón {self.nombre} individual"