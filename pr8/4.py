from math import pi

# Clase base para todos los objetos geométricos
class ObjetoGeometrico:
    """
    Clase base para todos los objetos geométricos.
    Se utiliza como clase base para los objetos 2D y 3D.
    """
    def __init__(self):
        pass

# Clase base para objetos bidimensionales
class Objeto2D(ObjetoGeometrico):
    """
    Clase base para objetos geométricos bidimensionales (2D).
    Hereda de la clase ObjetoGeometrico y debe implementar los métodos
    para calcular el perímetro y el área en las subclases.
    """
    def __init__(self):
        super().__init__()

    def perimetro(self):
        """
        Calcula el perímetro del objeto. Este método debe ser implementado por la subclase.
        
        :raises NotImplementedError: Si no está implementado en la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def area(self):
        """
        Calcula el área del objeto. Este método debe ser implementado por la subclase.
        
        :raises NotImplementedError: Si no está implementado en la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase base para objetos tridimensionales
class Objeto3D(ObjetoGeometrico):
    """
    Clase base para objetos geométricos tridimensionales (3D).
    Hereda de la clase ObjetoGeometrico y debe implementar los métodos
    para calcular el volumen y el área de superficie en las subclases.
    """
    def __init__(self):
        super().__init__()

    def volumen(self):
        """
        Calcula el volumen del objeto. Este método debe ser implementado por la subclase.
        
        :raises NotImplementedError: Si no está implementado en la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def area_superficie(self):
        """
        Calcula el área de superficie del objeto. Este método debe ser implementado por la subclase.
        
        :raises NotImplementedError: Si no está implementado en la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase base para todos los vehículos
class Vehiculo:
    """
    Clase base para vehículos. Proporciona métodos para calcular el costo de viaje y obtener las características.
    
    Atributos:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        consumo_combustible (float): Consumo de combustible en litros por kilómetro.
    """
    def __init__(self, marca, modelo, consumo_combustible):
        """
        Inicializa un vehículo con marca, modelo y consumo de combustible.
        
        :param marca: Marca del vehículo.
        :param modelo: Modelo del vehículo.
        :param consumo_combustible: Consumo de combustible en litros por kilómetro.
        """
        self.marca = marca
        self.modelo = modelo
        self.consumo_combustible = consumo_combustible  # Litros por km

    def costo_viaje(self, distancia, precio_combustible):
        """
        Calcula el costo de un viaje en función de la distancia y el precio del combustible.
        
        :param distancia: Distancia a recorrer en kilómetros.
        :param precio_combustible: Precio del combustible por litro.
        :return: El costo del viaje.
        """
        return distancia * self.consumo_combustible * precio_combustible

    def caracteristicas(self):
        """
        Devuelve las características del vehículo como un string.
        
        :return: Características del vehículo.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Consumo: {self.consumo_combustible} L/km"

# Clase para Automóvil
class Automovil(Vehiculo):
    """
    Representa un automóvil, un tipo de vehículo.
    
    Atributos:
        capacidad_personas (int): Número de personas que el automóvil puede transportar.
    """
    def __init__(self, marca, modelo, consumo_combustible, capacidad_personas):
        """
        Inicializa un automóvil con la marca, modelo, consumo de combustible y capacidad de personas.
        
        :param marca: Marca del automóvil.
        :param modelo: Modelo del automóvil.
        :param consumo_combustible: Consumo de combustible en litros por kilómetro.
        :param capacidad_personas: Capacidad del automóvil en número de personas.
        """
        super().__init__(marca, modelo, consumo_combustible)
        self.capacidad_personas = capacidad_personas

    def caracteristicas(self):
        """
        Devuelve las características del automóvil como un string, incluyendo la capacidad de personas.
        
        :return: Características del automóvil.
        """
        return super().caracteristicas() + f", Capacidad: {self.capacidad_personas} personas"

# Clase para Camión
class Camion(Vehiculo):
    """
    Representa un camión, un tipo de vehículo con capacidad de carga.
    
    Atributos:
        capacidad_carga (float): Capacidad de carga en toneladas.
    """
    def __init__(self, marca, modelo, consumo_combustible, capacidad_carga):
        """
        Inicializa un camión con la marca, modelo, consumo de combustible y capacidad de carga.
        
        :param marca: Marca del camión.
        :param modelo: Modelo del camión.
        :param consumo_combustible: Consumo de combustible en litros por kilómetro.
        :param capacidad_carga: Capacidad de carga del camión en toneladas.
        """
        super().__init__(marca, modelo, consumo_combustible)
        self.capacidad_carga = capacidad_carga  # En toneladas

    def puede_transportar(self, carga):
        """
        Determina si el camión puede transportar una carga dada.
        
        :param carga: Carga que se desea transportar en toneladas.
        :return: True si el camión puede transportar la carga, False en caso contrario.
        """
        return carga <= self.capacidad_carga

    def caracteristicas(self):
        """
        Devuelve las características del camión como un string, incluyendo la capacidad de carga.
        
        :return: Características del camión.
        """
        return super().caracteristicas() + f", Capacidad de carga: {self.capacidad_carga} toneladas"

# Clase para Motocicleta
class Motocicleta(Vehiculo):
    """
    Representa una motocicleta, un tipo de vehículo.
    
    Atributos:
        tipo (str): Tipo de motocicleta (por ejemplo, "Deportiva", "Scooter").
    """
    def __init__(self, marca, modelo, consumo_combustible, tipo):
        """
        Inicializa una motocicleta con la marca, modelo, consumo de combustible y tipo.
        
        :param marca: Marca de la motocicleta.
        :param modelo: Modelo de la motocicleta.
        :param consumo_combustible: Consumo de combustible en litros por kilómetro.
        :param tipo: Tipo de motocicleta (por ejemplo, "Deportiva", "Scooter").
        """
        super().__init__(marca, modelo, consumo_combustible)
        self.tipo = tipo  # Por ejemplo: "Deportiva", "Scooter"

    def caracteristicas(self):
        """
        Devuelve las características de la motocicleta como un string, incluyendo el tipo de motocicleta.
        
        :return: Características de la motocicleta.
        """
        return super().caracteristicas() + f", Tipo: {self.tipo}"

# Ejemplo de uso
if __name__ == "__main__":
    auto = Automovil(marca="Toyota", modelo="Corolla", consumo_combustible=0.06, capacidad_personas=5)
    print(auto.caracteristicas())
    print("Costo de viaje (100 km, $1.5/L):", auto.costo_viaje(100, 1.5))

    camion = Camion(marca="Volvo", modelo="FH16", consumo_combustible=0.3, capacidad_carga=20)
    print(camion.caracteristicas())
    print("¿Puede transportar 15 toneladas?", camion.puede_transportar(15))
    print("Costo de viaje (200 km, $1.5/L):", camion.costo_viaje(200, 1.5))

    moto = Motocicleta(marca="Yamaha", modelo="R3", consumo_combustible=0.03, tipo="Deportiva")
    print(moto.caracteristicas())
    print("Costo de viaje (50 km, $1.5/L):", moto.costo_viaje(50, 1.5))
