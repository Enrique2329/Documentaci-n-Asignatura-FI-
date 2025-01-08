import matplotlib.pyplot as plt

class DataPlotter:
    """
    La clase DataPlotter permite crear diferentes tipos de gráficos (línea, dispersión, barras) utilizando datos proporcionados.
    
    Atributos:
        x (list): Lista de valores para el eje X.
        y (list): Lista de valores para el eje Y.
        line_color (str): Color de la línea en los gráficos (por defecto 'blue').
        line_width (float): Grosor de la línea (por defecto 2).
        line_style (str): Estilo de la línea (por defecto '-').
        marker (str): Tipo de marcador (por defecto None).
    """

    def __init__(self, x, y):
        """
        Inicializa la clase con datos x e y.
        
        :param x: Lista de valores en el eje x
        :param y: Lista de valores en el eje y
        """
        self.x = x
        self.y = y
        self.line_color = 'blue'  # Color de la línea por defecto
        self.line_width = 2       # Grosor de la línea por defecto
        self.line_style = '-'     # Estilo de la línea por defecto
        self.marker = None        # Marcador por defecto

    def set_properties(self, color='blue', width=2, style='-', marker=None):
        """
        Configura las propiedades de la gráfica.
        
        :param color: Color de la línea (str)
        :param width: Grosor de la línea (float)
        :param style: Estilo de la línea (str)
        :param marker: Tipo de marcador (str)
        """
        self.line_color = color
        self.line_width = width
        self.line_style = style
        self.marker = marker

    def plot(self, title='Gráfica', xlabel='Eje X', ylabel='Eje Y', grid=True):
        """
        Crea una gráfica con las propiedades configuradas.
        
        :param title: Título de la gráfica (str)
        :param xlabel: Etiqueta del eje X (str)
        :param ylabel: Etiqueta del eje Y (str)
        :param grid: Muestra una cuadrícula si es True (bool)
        """
        plt.figure(figsize=(8, 6))
        plt.plot(self.x, self.y, color=self.line_color, linewidth=self.line_width,
                 linestyle=self.line_style, marker=self.marker)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True)
        plt.show()

    def scatter(self, title='Diagrama de Dispersión', xlabel='Eje X', ylabel='Eje Y', grid=True):
        """
        Crea un diagrama de dispersión con las propiedades configuradas.
        
        :param title: Título de la gráfica (str)
        :param xlabel: Etiqueta del eje X (str)
        :param ylabel: Etiqueta del eje Y (str)
        :param grid: Muestra una cuadrícula si es True (bool)
        """
        plt.figure(figsize=(8, 6))
        plt.scatter(self.x, self.y, color=self.line_color, s=self.line_width * 10, marker=self.marker)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True)
        plt.show()

    def bar(self, title='Gráfico de Barras', xlabel='Eje X', ylabel='Eje Y', grid=True):
        """
        Crea un gráfico de barras con las propiedades configuradas.
        
        :param title: Título de la gráfica (str)
        :param xlabel: Etiqueta del eje X (str)
        :param ylabel: Etiqueta del eje Y (str)
        :param grid: Muestra una cuadrícula si es True (bool)
        """
        plt.figure(figsize=(8, 6))
        plt.bar(self.x, self.y, color=self.line_color, width=0.8)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True, axis='y')
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]

    plotter = DataPlotter(x_data, y_data)

    # Configurar propiedades y mostrar diferentes gráficos
    plotter.set_properties(color='red', width=3, style='--', marker='o')
    plotter.plot(title='Gráfica Lineal', xlabel='Tiempo', ylabel='Valor')

    plotter.set_properties(color='green', marker='x')
    plotter.scatter(title='Gráfica de Dispersión', xlabel='Tiempo', ylabel='Valor')

    plotter.set_properties(color='purple')
    plotter.bar(title='Gráfico de Barras', xlabel='Categoría', ylabel='Frecuencia')
