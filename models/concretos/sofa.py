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
                 capacidad_personas: int = 3, tiene_respaldo: bool = True, material_tapizado: str = "tela",
                 es_modular: bool = False, incluye_cojines: bool = False):
        super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)
        self._es_modular = es_modular
        self._incluye_cojines = incluye_cojines

    @property
    def es_modular(self) -> bool:
        return self._es_modular

    @es_modular.setter
    def es_modular(self, value: bool) -> None:
        self._es_modular = bool(value)

    @property
    def incluye_cojines(self) -> bool:
        return self._incluye_cojines

    @incluye_cojines.setter
    def incluye_cojines(self, value: bool) -> None:
        self._incluye_cojines = bool(value)

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
        if self.es_modular:
            precio += 400
        if self.incluye_cojines:
            precio += 100
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del sofá.
        """
        descripcion = f"Sofá {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nModular: {'Sí' if self.es_modular else 'No'}"
        descripcion += f", Incluye cojines: {'Sí' if self.incluye_cojines else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Sofá {self.nombre} para {self.capacidad_personas} personas ({'modular' if self.es_modular else 'tradicional'})"