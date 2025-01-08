from math import pi

# Clase base para todos los objetos geométricos
class ObjetoGeometrico:
    """
    Clase base para todos los objetos geométricos.
    Se usa como clase base para los objetos 2D y 3D.
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

# Clase para el Círculo
class Circulo(Objeto2D):
    """
    Representa un círculo, un objeto bidimensional.
    
    Atributos:
        radio (float): Radio del círculo.
    """
    def __init__(self, radio):
        """
        Inicializa el círculo con el radio dado.
        
        :param radio: El radio del círculo.
        """
        super().__init__()
        self.radio = radio

    def perimetro(self):
        """
        Calcula el perímetro del círculo.
        
        :return: El perímetro del círculo.
        """
        return 2 * pi * self.radio

    def area(self):
        """
        Calcula el área del círculo.
        
        :return: El área del círculo.
        """
        return pi * self.radio**2

# Clase para el Rectángulo
class Rectangulo(Objeto2D):
    """
    Representa un rectángulo, un objeto bidimensional.
    
    Atributos:
        base (float): Base del rectángulo.
        altura (float): Altura del rectángulo.
    """
    def __init__(self, base, altura):
        """
        Inicializa el rectángulo con la base y altura dadas.
        
        :param base: La base del rectángulo.
        :param altura: La altura del rectángulo.
        """
        super().__init__()
        self.base = base
        self.altura = altura

    def perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        
        :return: El perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def area(self):
        """
        Calcula el área del rectángulo.
        
        :return: El área del rectángulo.
        """
        return self.base * self.altura

# Clase para el Triángulo
class Triangulo(Objeto2D):
    """
    Representa un triángulo, un objeto bidimensional.
    
    Atributos:
        lado1 (float): Longitud del primer lado.
        lado2 (float): Longitud del segundo lado.
        lado3 (float): Longitud del tercer lado.
        altura_base (float): Altura correspondiente a la base.
        base (float): Longitud de la base.
    """
    def __init__(self, lado1, lado2, lado3, altura_base, base):
        """
        Inicializa el triángulo con los lados y la base dados.
        
        :param lado1: El primer lado del triángulo.
        :param lado2: El segundo lado del triángulo.
        :param lado3: El tercer lado del triángulo.
        :param altura_base: La altura correspondiente a la base.
        :param base: La base del triángulo.
        """
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura_base = altura_base
        self.base = base

    def perimetro(self):
        """
        Calcula el perímetro del triángulo.
        
        :return: El perímetro del triángulo.
        """
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        """
        Calcula el área del triángulo.
        
        :return: El área del triángulo.
        """
        return (self.base * self.altura_base) / 2

# Clase para la Esfera
class Esfera(Objeto3D):
    """
    Representa una esfera, un objeto tridimensional.
    
    Atributos:
        radio (float): Radio de la esfera.
    """
    def __init__(self, radio):
        """
        Inicializa la esfera con el radio dado.
        
        :param radio: El radio de la esfera.
        """
        super().__init__()
        self.radio = radio

    def volumen(self):
        """
        Calcula el volumen de la esfera.
        
        :return: El volumen de la esfera.
        """
        return (4/3) * pi * self.radio**3

    def area_superficie(self):
        """
        Calcula el área de superficie de la esfera.
        
        :return: El área de superficie de la esfera.
        """
        return 4 * pi * self.radio**2

# Clase para el Cubo
class Cubo(Objeto3D):
    """
    Representa un cubo, un objeto tridimensional.
    
    Atributos:
        lado (float): Longitud de un lado del cubo.
    """
    def __init__(self, lado):
        """
        Inicializa el cubo con el lado dado.
        
        :param lado: El lado del cubo.
        """
        super().__init__()
        self.lado = lado

    def volumen(self):
        """
        Calcula el volumen del cubo.
        
        :return: El volumen del cubo.
        """
        return self.lado**3

    def area_superficie(self):
        """
        Calcula el área de superficie del cubo.
        
        :return: El área de superficie del cubo.
        """
        return 6 * (self.lado**2)

# Clase para el Cilindro
class Cilindro(Objeto3D):
    """
    Representa un cilindro, un objeto tridimensional.
    
    Atributos:
        radio (float): Radio de la base del cilindro.
        altura (float): Altura del cilindro.
    """
    def __init__(self, radio, altura):
        """
        Inicializa el cilindro con el radio y la altura dados.
        
        :param radio: El radio de la base del cilindro.
        :param altura: La altura del cilindro.
        """
        super().__init__()
        self.radio = radio
        self.altura = altura

    def volumen(self):
        """
        Calcula el volumen del cilindro.
        
        :return: El volumen del cilindro.
        """
        return pi * self.radio**2 * self.altura

    def area_superficie(self):
        """
        Calcula el área de superficie del cilindro.
        
        :return: El área de superficie del cilindro.
        """
        return 2 * pi * self.radio * (self.radio + self.altura)

# Ejemplo de uso
if __name__ == "__main__":
    circulo = Circulo(radio=5)
    print("Círculo: Perímetro:", circulo.perimetro(), "Área:", circulo.area())

    rectangulo = Rectangulo(base=4, altura=7)
    print("Rectángulo: Perímetro:", rectangulo.perimetro(), "Área:", rectangulo.area())

    esfera = Esfera(radio=3)
    print("Esfera: Volumen:", esfera.volumen(), "Área superficial:", esfera.area_superficie())

    cubo = Cubo(lado=2)
    print("Cubo: Volumen:", cubo.volumen(), "Área superficial:", cubo.area_superficie())

    cilindro = Cilindro(radio=3, altura=5)
    print("Cilindro: Volumen:", cilindro.volumen(), "Área superficial:", cilindro.area_superficie())
