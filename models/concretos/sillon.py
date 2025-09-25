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
                 tiene_respaldo: bool = True, material_tapizado: str = "tela",
                 es_reclinable: bool = False, tiene_reposapies: bool = False):
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self._es_reclinable = es_reclinable
        self._tiene_reposapies = tiene_reposapies

    @property
    def es_reclinable(self) -> bool:
        return self._es_reclinable

    @es_reclinable.setter
    def es_reclinable(self, value: bool) -> None:
        self._es_reclinable = bool(value)

    @property
    def tiene_reposapies(self) -> bool:
        return self._tiene_reposapies

    @tiene_reposapies.setter
    def tiene_reposapies(self, value: bool) -> None:
        self._tiene_reposapies = bool(value)

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
        if self.es_reclinable:
            precio += 200
        if self.tiene_reposapies:
            precio += 100
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del sillón.
        """
        descripcion = f"Sillón {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nReclinable: {'Sí' if self.es_reclinable else 'No'}"
        descripcion += f", Reposapiés: {'Sí' if self.tiene_reposapies else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Sillón {self.nombre} ({'reclinable' if self.es_reclinable else 'fijo'})"