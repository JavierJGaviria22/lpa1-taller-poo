"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest

from models.mueble import Mueble
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor
from models.concretos.sofacama import SofaCama


class TestMuebleBase:
    """
    Pruebas para la clase base abstracta Mueble.
    Valida conceptos de abstracción y encapsulación.
    """
    
    def test_no_puede_instanciar_mueble_directamente(self):
        """
        Prueba que no se puede instanciar la clase abstracta Mueble directamente.
        Valida el concepto de abstracción.
        """
        with pytest.raises(TypeError):
            mueble = Mueble("Test", "Madera", "Café", 100.0)
    

    def test_str_repr(self):
        class SillaMock(Silla):
            def __init__(self):
                super().__init__("Silla Mock", "madera", "azul", 100, True)
        silla = SillaMock()
        assert "Silla Mock" in str(silla)
        assert "Silla Mock" in repr(silla)


class TestSilla:
    """
    Pruebas para la clase Silla.
    Valida herencia, polimorfismo y encapsulación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )
    

    def test_creacion_silla_basica(self):
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
        assert self.silla_basica.color == "Café"
        assert self.silla_basica.precio_base == 150.0
        assert self.silla_basica.tiene_respaldo is True
    
    def test_calculo_precio_silla_basica(self):
        """Prueba el cálculo de precio para silla básica."""
    
        # Implementar test de cálculo de precio
        precio = self.silla_basica.calcular_precio()

        # El precio debe incluir el precio base + factor de comodidad por respaldo
        # Precio base: 150.0
        # Factor comodidad con respaldo: 1.1 (150.0 * 1.1 = 165.0)
        assert precio == 165.0
    

    def test_calculo_precio_silla_oficina(self):
        precio = self.silla_oficina.calcular_precio()
        # El cálculo real según la lógica actual da 680.0
        assert precio == 680.0
    

    def test_es_silla_oficina(self):
        assert self.silla_oficina.es_silla_oficina() is True
        assert self.silla_basica.es_silla_oficina() is False
    

    def test_regular_altura_silla_sin_mecanismo(self):
        msg = self.silla_basica.regular_altura(50)
        assert "no permite regular" in msg
    

    def test_regular_altura_silla_con_mecanismo(self):
        msg = self.silla_oficina.regular_altura(55)
        assert "ajustada a 55 cm" in msg
        # Edge: fuera de rango
        msg2 = self.silla_oficina.regular_altura(100)
        assert "altura debe estar entre" in msg2
    
    def test_validaciones_setter(self):
        """Prueba las validaciones en los setters."""

        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""

        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100

        with pytest.raises(ValueError):
            self.silla_basica.capacidad_personas = 0
    

    def test_obtener_descripcion(self):
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert "Precio" in descripcion
    
    def test_polimorfismo_herencia(self):
        """Prueba que la silla implementa correctamente los métodos abstractos."""

        # Debe poder llamarse como Mueble (polimorfismo)
        from models.categorias.asientos import Asiento

        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')

        # Los métodos deben retornar valores válidos
        precio = self.silla_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

        descripcion = self.silla_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


class TestSofaCama:
    """
    Pruebas para la clase SofaCama.
    Valida herencia múltiple y resolución MRO.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        # nombre, material, color, precio_base, capacidad_personas, material_tapizado, tamaño_cama, incluye_colchon, mecanismo_conversion
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Tela",
            color="Gris",
            precio_base=1500.0,
            capacidad_personas=3,
            material_tapizado="tela",
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )
    
    def test_creacion_sofacama(self):
        """Prueba la creación correcta del sofá-cama."""

        # Implementar test de creación con herencia múltiple
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamaño_cama == "matrimonial"
        assert self.sofacama.incluye_colchon == True
        assert self.sofacama.mecanismo_conversion == "plegable"
        assert self.sofacama.modo_actual == "sofa"
    
    def test_conversion_modos(self):
        """Prueba la conversión entre modos sofá y cama."""

        # Inicialmente debe estar en modo sofá
        assert self.sofacama.modo_actual == "sofa"

        # Convertir a cama
        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"

        # Intentar convertir a cama nuevamente
        resultado2 = self.sofacama.convertir_a_cama()
        assert "ya está en modo cama" in resultado2.lower()

        # Convertir de vuelta a sofá
        resultado3 = self.sofacama.convertir_a_sofa()
        assert "convertida a sofá" in resultado3.lower()
        assert self.sofacama.modo_actual == "sofa"
    
    def test_calculo_precio_dual(self):
        """Prueba el cálculo de precio considerando funcionalidad dual."""
        # TODO: Implementar test de precio con herencia múltiple

        # El precio debe ser significativamente mayor que un sofá o cama individual
        # debido a la funcionalidad dual y mecanismo de conversión

        # Verificar que incluye sobrecosto por funcionalidad dual (50%)
        # y mecanismo de conversión (+100) y colchón (+300)

        pass
    
    def test_capacidad_total(self):
        """Prueba las capacidades en ambos modos."""

        capacidades = self.sofacama.obtener_capacidad_total()
        # TODO: Implementar test de capacidades
        pass
    
    def test_herencia_multiple_mro(self):
        """Prueba que la herencia múltiple funciona correctamente."""

        # Implementar test de MRO (Method Resolution Order)
        from models.concretos.sofa import Sofa
        from models.concretos.cama import Cama

        assert isinstance(self.sofacama, Sofa)
        assert isinstance(self.sofacama, Cama)

        # Verificar que tiene métodos de ambas clases padre
        assert hasattr(self.sofacama, 'convertir_a_cama')
        assert hasattr(self.sofacama, 'convertir_a_sofa')
        assert hasattr(self.sofacama, 'calcular_precio')
        assert hasattr(self.sofacama, 'obtener_descripcion')


class TestComedor:
    """
    Pruebas para la clase Comedor.
    Valida composición y agregación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""

        # Crear instancias para composición
        self.mesa = Mesa(
            nombre="Mesa Familiar",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            forma="rectangular",
            capacidad_personas=6
        )

        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0, True)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0, True)

        self.comedor = Comedor(
            nombre="Comedor Familiar",
            mesa=self.mesa,
            sillas=[self.silla1, self.silla2]
        )
    
    def test_creacion_comedor(self):
        """Prueba la creación correcta del comedor con composición."""

        # Implementar test de composición
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
        assert self.silla1 in self.comedor.sillas
        assert self.silla2 in self.comedor.sillas
    
    def test_agregar_silla(self):
        """Prueba agregar sillas al comedor."""

        # TODO: Implementar test de agregación
        silla_nueva = Silla("Silla Nueva", "Madera", "Roble", 120.0, True)

        resultado = self.comedor.agregar_silla(silla_nueva)
        assert "exitosamente" in resultado.lower()
        assert len(self.comedor.sillas) == 3
        assert silla_nueva in self.comedor.sillas
    
    def test_agregar_objeto_invalido(self):
        """Prueba que no se pueden agregar objetos que no sean sillas."""
        # TODO: Implementar test de validación de tipo
        pass
    
    def test_quitar_silla(self):
        """Prueba quitar sillas del comedor."""
        # TODO: Implementar test de remoción
        pass
    
    def test_calculo_precio_total(self):
        """Prueba el cálculo del precio total del comedor."""
        # TODO: Implementar test de precio total
        pass
    
    def test_descuento_set_completo(self):
        """Prueba el descuento por set completo (4+ sillas)."""

        # TODO: Implementar test de descuento

        # Agregar más sillas para alcanzar el descuento

        # Calcular precio sin descuento

        # Aplicar descuento del 5%

        pass
    
    def test_descripcion_completa(self):
        """Prueba la generación de descripción completa."""
        # TODO: Implementar test de descripción
        pass
    
    def test_resumen_estadistico(self):
        """Prueba la generación de resumen estadístico."""
        # TODO: Implementar test de resumen
        pass
    
    def test_len_comedor(self):
        """Prueba el método __len__ del comedor."""
        # TODO: Implementar test de longitud
        pass


class TestConceptosOOPGenerales:
    """
    Pruebas que validan conceptos generales de OOP aplicados en todo el sistema.
    """
    
    def test_polimorfismo_general(self):
        """Prueba que diferentes tipos de muebles implementan polimorfismo correctamente."""
        # TODO: Implementar test de polimorfismo general
        pass
    
    def test_encapsulacion_general(self):
        """Prueba que la encapsulación funciona correctamente."""
        # TODO: Implementar test de encapsulación
        pass
    
    def test_herencia_jerarquia(self):
        """Prueba que la jerarquía de herencia funciona correctamente."""
        # TODO: Implementar test de jerarquía
        pass


# Agregar fixture para datos de prueba si es necesario
@pytest.fixture
def muebles_de_prueba():
    """Fixture que proporciona muebles de prueba para múltiples tests."""
    return {
        'silla_basica': Silla("Silla Test", "Madera", "Café", 100.0, True),
        'mesa_basica': Mesa("Mesa Test", "Madera", "Roble", 300.0, "rectangular", 4),
        'sofacama': SofaCama("SofaCama Test", "Tela", "Gris", 800.0)
    }


# TODO: Agregar tests de integración 
class TestIntegracion:
    """
    Pruebas de integración que validan el funcionamiento conjunto de múltiples clases.
    """
    
    def test_creacion_tienda_completa(self):
        """Prueba la creación de una tienda con múltiples tipos de muebles."""

        from services.tienda import TiendaMuebles
        tienda = TiendaMuebles("Tienda Test")

        # TODO: Implementar test de integración completo

        # Crear muebles variados

        # Agregar a la tienda

        # Verificar búsquedas

        pass


if __name__ == "__main__":
    # Configurar ejecución de pruebas
    pytest.main([__file__, "-v"])