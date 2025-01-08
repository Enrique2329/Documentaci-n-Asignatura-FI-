class Calculadora:
    """
    La clase Calculadora permite realizar operaciones básicas entre dos números: suma, resta, multiplicación y división.
    
    Atributos:
        numero1 (float): El primer número para las operaciones.
        numero2 (float): El segundo número para las operaciones.
    
    Métodos:
        __init__(self, numero1, numero2): Inicializa los números para las operaciones.
        sumar(self): Devuelve la suma de los dos números.
        restar(self): Devuelve la resta entre los dos números.
        multiplicar(self): Devuelve la multiplicación de los dos números.
        dividir(self): Devuelve la división de los dos números, o un error si el segundo número es cero.
    """
    
    def __init__(self, numero1, numero2):
        """
        Inicializa los números para las operaciones.
        
        Parámetros:
            numero1 (float): El primer número.
            numero2 (float): El segundo número.
        """
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        """Devuelve la suma de los dos números."""
        return self.numero1 + self.numero2
    
    def restar(self):
        """Devuelve la resta entre los dos números."""
        return self.numero1 - self.numero2
    
    def multiplicar(self):
        """Devuelve la multiplicación de los dos números."""
        return self.numero1 * self.numero2
    
    def dividir(self):
        """
        Devuelve la división de los dos números.
        
        Si el segundo número es 0, devuelve un mensaje de error.
        """
        if self.numero2 == 0:
            return "Error: Division entre 0 no permitida"
        else:
            return self.numero1 / self.numero2
    

print("Calculadora de operaciones básicas:")

try:
    numero1 = float(input("Introduce el numero 1: "))
    numero2 = float(input("Introduce el numero 2: "))
    calculadora = Calculadora(numero1, numero2)
    print(f"Suma: {calculadora.sumar()}")
    print(f"Resta: {calculadora.restar()}")
    print(f"Multiplicacion: {calculadora.multiplicar()}")
    print(f"Division: {calculadora.dividir()}")
except ValueError:
    print("Introduzca valores validos: ")
