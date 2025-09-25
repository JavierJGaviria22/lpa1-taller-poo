"""
Clase concreta Sofa.
Hereda de Asiento y representa un sofá tradicional.
"""
from models.categorias.asientos import Asiento

class Sofa(Asiento):
    """
    Clase concreta para sofá.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, tiene_respaldo: bool = True, material_tapizado: str = "tela"):
        super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)

    def calcular_precio(self) -> float:
        """
        Calcula el precio del sofá según sus características.
        """
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        if self.material_tapizado and self.material_tapizado.lower() == "cuero":
            precio += 500
        elif self.material_tapizado and self.material_tapizado.lower() == "tela":
            precio += 200
        if self.capacidad_personas > 3:
            precio += 150 * (self.capacidad_personas - 3)
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del sofá.
        """
        descripcion = f"Sofá {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Sofá {self.nombre} para {self.capacidad_personas} personas"