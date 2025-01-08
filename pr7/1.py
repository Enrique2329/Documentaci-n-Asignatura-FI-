import matplotlib.pyplot as plt
import numpy as np
import math

def grafico_1():
    """
    Grafica la función y = 3x - x^3 en el intervalo [-10, 10].
    """
    x = np.arange(-10, 10, 0.01)
    y = 3 * x - x ** 3
    plt.plot(x, y)
    plt.axis((-5, 5, -5, 5))
    plt.show()

def grafico_2():
    """
    Grafica la función y = x^4 - 2x^2 - 8 en el intervalo [-10, 10].
    """
    x = np.arange(-10, 10, 0.01)
    y = (x ** 4) - 2 * (x ** 2) - 8
    plt.plot(x, y)
    plt.axis((-5, 5, -10, 10))
    plt.show()

def grafico_3():
    """
    Grafica la función y = (x^3) / (x - 1)^2 en el intervalo [-20, 20].
    """
    x = np.arange(-20, 20, 0.01)
    y = (x ** 3) / (x - 1) ** 2
    plt.plot(x, y)
    plt.axis((-10, 10, -20, 20))
    plt.show()

def grafico_4():
    """
    Grafica la función y = (x^4 + 1) / x^2 en el intervalo [-20, 20].
    """
    x = np.arange(-20, 20, 0.01)
    y = ((x ** 4) + 1) / (x ** 2)
    plt.plot(x, y)
    plt.axis((-10, 10, 0, 20))
    plt.show()

def grafico_5():
    """
    Grafica la función y = (x^2) / (2 - x) en el intervalo [-20, 20].
    """
    x = np.arange(-20, 20, 0.01)
    y = (x ** 2) / (2 - x)
    plt.plot(x, y)
    plt.axis((-5, 10, -40, 40))
    plt.show()

def grafico_6():
    """
    Grafica la función y = x / (1 + x^2) en el intervalo [-20, 20].
    """
    x = np.arange(-20, 20, 0.01)
    y = x / (1 + (x ** 2))
    plt.plot(x, y)
    plt.axis((0, 10, 0, 1))
    plt.show()

def grafico_7():
    """
    Grafica la función y = (x^2 - 3x + 2) / (x^2 + 1) en el intervalo [-20, 20].
    """
    x = np.arange(-20, 20, 0.01)
    y = ((x ** 2) - (3 * x) + 2) / ((x ** 2) + 1)
    plt.plot(x, y)
    plt.axis((-10, 10, -5, 5))
    plt.show()

def grafico_8():
    """
    Grafica la función y = x + sqrt(x) en el intervalo [-30, 30].
    """
    x = np.arange(-30, 30, 0.01)
    y = x + (x ** (1 / 2))
    plt.plot(x, y)
    plt.axis((0, 50, 0, 30))
    plt.show()

def grafico_9():
    """
    Grafica la función y = exp(1/x) en el intervalo [-20, 20], sin incluir el valor 0.
    """
    x = np.arange(-20, 20, 0.013)  # Pasos más pequeños para evitar 0
    def calcularnumeroe(x):
        return np.exp(1 / x)
    
    y = calcularnumeroe(x)
    plt.plot(x, y)
    plt.axis((-10, 10, -5, 20))
    plt.show()

def grafico_10():
    """
    Grafica la función y = (x - 1) * exp(-x) en el intervalo [-30, 30].
    """
    x = np.arange(-30, 30, 0.01)
    y = (x - 1) * np.exp(-x)
    plt.plot(x, y)
    plt.axis((-20, 20, -100, 100))
    plt.show()

def grafico_11():
    """
    Grafica la función y = log(x) / x en el intervalo [1, 30].
    """
    x = np.arange(1, 30, 0.01)
    y = np.log(x) / x
    plt.plot(x, y)
    plt.axis((0, 30, 0, 0.5))
    plt.show()

def grafico_12():
    """
    Grafica la función y(x) = sin(4πx) * e^(-5x) en el intervalo [0, 1].
    """
    pi = np.pi
    x = np.arange(0, 1, 0.01)
    y = np.sin(4 * pi * x) * np.exp(-5 * x)
    plt.plot(x, y)
    plt.axis((0, 1, -0.75, 0.75))
    plt.show()

def grafico_13():
    """
    Grafica la función y(x) = cos(2πx) * e^(-x) en el intervalo [0, 5].
    """
    pi = np.pi
    x = np.arange(0, 5, 0.01)
    y = np.cos(2 * pi * x) * np.exp(-x)
    plt.plot(x, y)
    plt.axis((0, 5, -1, 1))
    plt.show()

# Llamar a la función deseada. Por ejemplo:
# grafico_1()    # Llama a la gráfica 1
# grafico_2()    # Llama a la gráfica 2
# grafico_3()    # Llama a la gráfica 3
# ...

