"""
Clase concreta Armario.
"""
from models.categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_puertas: int = 2, num_cajones: int = 0, tiene_espejos: bool = False):
        super().__init__(nombre, material, color, precio_base, num_puertas, num_cajones, tiene_espejos)

    # Los getters y setters ya están implementados en la clase base Almacenamiento

    def calcular_precio(self) -> float:
        """
        Calcula el precio del armario según sus características.
        """
        precio = self.precio_base
        precio += 200 * self.num_puertas
        precio += 80 * self.num_cajones
        if self.tiene_espejos:
            precio += 250
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del armario.
        """
        descripcion = f"Armario {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\nPuertas: {self.num_puertas}, Cajones: {self.num_cajones}"
        descripcion += f"\nEspejos: {'Sí' if self.tiene_espejos else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Armario {self.nombre} ({self.num_puertas} puertas{' con espejos' if self.tiene_espejos else ''})"