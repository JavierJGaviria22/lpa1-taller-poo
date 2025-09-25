# TODO: Importar las clases padre
from models.concretos.sofa import Sofa
from models.concretos.cama import Cama

class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        # Inicializa Sofa (que a su vez inicializa Mueble)
        super().__init__(nombre, material, color, precio_base, capacidad_personas, True, material_tapizado)
        # Inicializa atributos específicos de cama
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = incluye_colchon
        # Inicializa atributos únicos del sofá-cama
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Puede ser "sofa" o "cama"

    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion

    @mecanismo_conversion.setter
    def mecanismo_conversion(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El mecanismo de conversión no puede estar vacío")
        self._mecanismo_conversion = value.strip()

    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual

    @property
    def tamaño_cama(self) -> str:
        """Getter para el tamaño de la cama."""
        return self._tamaño_cama

    @tamaño_cama.setter
    def tamaño_cama(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El tamaño de cama no puede estar vacío")
        self._tamaño_cama = value.strip()

    @property
    def incluye_colchon(self) -> bool:
        """Getter para si incluye colchón."""
        return self._incluye_colchon

    @incluye_colchon.setter
    def incluye_colchon(self, value: bool) -> None:
        self._incluye_colchon = bool(value)

    def convertir_a_cama(self) -> str:
        """Convierte el sofá en cama."""
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"
        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    def convertir_a_sofa(self) -> str:
        """Convierte la cama en sofá."""
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"
        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"

    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        """
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        precio *= 1.5  # 50% más caro por ser dual
        if self.mecanismo_conversion.lower() == "electrico":
            precio += 200
        elif self.mecanismo_conversion.lower() == "hidraulico":
            precio += 150
        else:  # manual/plegable
            precio += 100
        if self.incluye_colchon:
            precio += 300
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.
        """
        descripcion = f"Sofá-cama {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nTamaño de cama: {self.tamaño_cama}"
        descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        descripcion += f"\nModo actual: {self.modo_actual}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        """
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1
        }
        return capacidades

    def puede_usar_como_cama(self) -> bool:
        """Verifica si actualmente puede usarse como cama."""
        return self._modo_actual == "cama"

    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self._modo_actual == "sofa"

    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        """
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"