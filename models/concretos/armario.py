"""
Clase concreta Armario.
"""
from models.categorias.almacenamiento import Almacenamiento

class Armario(Almacenamiento):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad: float, tipo_apertura: str = "puertas", cantidad_puertas: int = 2, tiene_espejo: bool = False):
        super().__init__(nombre, material, color, precio_base, capacidad, tipo_apertura)
        self._cantidad_puertas = cantidad_puertas
        self._tiene_espejo = tiene_espejo

    @property
    def cantidad_puertas(self) -> int:
        """Cantidad de puertas en el armario."""
        return self._cantidad_puertas

    @cantidad_puertas.setter
    def cantidad_puertas(self, value: int) -> None:
        if value < 1:
            raise ValueError("El armario debe tener al menos una puerta")
        self._cantidad_puertas = value

    @property
    def tiene_espejo(self) -> bool:
        """Indica si el armario tiene espejo."""
        return self._tiene_espejo

    @tiene_espejo.setter
    def tiene_espejo(self, value: bool) -> None:
        self._tiene_espejo = bool(value)

    def calcular_precio(self) -> float:
        """
        Calcula el precio del armario según sus características.
        """
        precio = self.precio_base
        precio += self.capacidad * 90  # precio por litro de capacidad
        precio += 100 * self.cantidad_puertas
        if self.tiene_espejo:
            precio += 250
        if self.tipo_apertura.lower() == "corrediza":
            precio += 120
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Devuelve la descripción completa del armario.
        """
        descripcion = f"Armario {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_descripcion()}"
        descripcion += f"\nCantidad de puertas: {self.cantidad_puertas}"
        descripcion += f"\nEspejo: {'Sí' if self.tiene_espejo else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def __str__(self) -> str:
        return f"Armario {self.nombre} ({self.cantidad_puertas} puertas{' con espejo' if self.tiene_espejo else ''})"