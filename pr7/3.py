"""
Un diccionario en Python es una estructura de datos que almacena pares de clave-valor. 
Es mutable y permite un acceso rápido a los valores mediante las claves. 
Se define utilizando llaves {} y los pares de clave-valor se separan por comas.

Métodos útiles de los diccionarios:

1. get(): Devuelve el valor de una clave, o un valor por defecto si la clave no existe.
2. keys(): Devuelve una vista de las claves del diccionario.
3. values(): Devuelve una vista de los valores del diccionario.
4. items(): Devuelve una vista de los pares clave-valor del diccionario.
5. update(): Actualiza el diccionario con los pares clave-valor de otro diccionario.
6. pop(): Elimina una clave y devuelve su valor.
"""

# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(mi_diccionario)


# Métodos útiles de los diccionarios

# 1. get(): Devuelve el valor de una clave, o un valor por defecto si la clave no existe.
edad = mi_diccionario.get("edad", "No disponible")
print(edad)

profesion = mi_diccionario.get("profesion", "No disponible")
print(profesion)


# 2. keys(): Devuelve una vista de las claves del diccionario.
claves = mi_diccionario.keys()
print(claves)


# 3. values(): Devuelve una vista de los valores del diccionario.
valores = mi_diccionario.values()
print(valores)


# 4. items(): Devuelve una vista de los pares clave-valor del diccionario.
elementos = mi_diccionario.items()
print(elementos)


# 5. update(): Actualiza el diccionario con los pares clave-valor de otro diccionario.
mi_diccionario.update({"profesion": "Ingeniero", "edad": 31})
print(mi_diccionario)


# 6. pop(): Elimina una clave y devuelve su valor.
ciudad = mi_diccionario.pop("ciudad", "No disponible")
print(ciudad)
print(mi_diccionario)
