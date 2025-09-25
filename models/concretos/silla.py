"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""
# Importar la clase padre Asiento
from models.categorias.asientos import Asiento

class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    
    Una silla es un asiento individual con características específicas
    como altura regulable, ruedas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la silla
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        """
        Constructor de la silla.
        
        Args:
            altura_regulable: Si la silla puede regular su altura
            tiene_ruedas: Si la silla tiene ruedas
            Otros argumentos heredados de Asiento
        """
        # Llamar al constructor padre con capacidad fija de 1 persona
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        # Inicializar atributos específicos de la silla
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas
        self._altura_actual = 45  # altura estándar en cm

    # Implementar propiedades para los nuevos atributos
    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable
    
    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable."""
        self._altura_regulable = bool(value)

    @property
    def tiene_ruedas(self) -> bool:
        """Getter para si tiene ruedas."""
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para si tiene ruedas."""
        self._tiene_ruedas = bool(value)

    @property
    def altura_actual(self) -> int:
        """Getter para la altura actual de la silla."""
        return self._altura_actual

    @altura_actual.setter
    def altura_actual(self, value: int) -> None:
        """Setter para la altura actual de la silla."""
        if value < 35 or value > 60:
            raise ValueError("La altura debe estar entre 35 y 60 cm")
        self._altura_actual = value

    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        
        Returns:
            float: Precio final de la silla
        """
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        if self.material_tapizado and self.material_tapizado.lower() == "cuero":
            precio += 150
        elif self.material_tapizado and self.material_tapizado.lower() == "tela":
            precio += 50
        if self.altura_regulable:
            precio += 80
        if self.tiene_ruedas:
            precio += 60
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        
        Returns:
            str: Descripción completa de la silla
        """
        descripcion = f"Silla {self.nombre} fabricada en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nAltura regulable: {'Sí' if self.altura_regulable else 'No'}"
        descripcion += f", Ruedas: {'Sí' if self.tiene_ruedas else 'No'}"
        descripcion += f"\nAltura actual: {self.altura_actual} cm"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion
    
    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.
        
        Args:
            nueva_altura: Nueva altura en centímetros
            
        Returns:
            str: Mensaje del resultado de la operación
        """
        if not self.altura_regulable:
            return "Esta silla no permite regular la altura."
        try:
            self.altura_actual = nueva_altura
            return f"Altura ajustada a {self.altura_actual} cm."
        except ValueError as e:
            return str(e)
    
    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        
        Returns:
            bool: True si es silla de oficina
        """
        # Una silla es de oficina si tiene ruedas Y altura regulable
        return self.tiene_ruedas and self.altura_regulable