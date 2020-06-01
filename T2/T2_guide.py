""" TEMAS:
- Cálculos y operaciones:
    Pensamiento computacional en problemas que involucran cálculos
    Orden: funciones, (), /, *, +, -.
    funciones math.sqrt(a) y pow(a, b)
- General:
    Cast de variables
    funcion input()
"""

import math

def main():
    
    NOMBRE = input("Cual es tu nombre entrenador!? ")
    print("Hola ", NOMBRE, ", Pikachu necesita tu ayuda!")
    print("Introduce la ecuacion de tipo ax^2 + bx + c que describe las defensas de Charizard: ")
    
    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
     
    """ Demostracion de calculos matematicos
    x = a + b + c
    x = a + b * c
    x = (a + b) * c
    x = a / b
    x = a / b
    x = math.sqrt(a)
    x = pow(a, b)
    """
     
    # Orden: funciones, (), /, *, +, -.
    x0 = (-b + math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
    x1 = (-b - math.sqrt(pow(b, 2) -4*a*c)) / (2*a)
 
    print("Pikachu, debes atacar en los tiempos: ", x0, " y ", x1, " !")
    
if __name__ == '__main__':
    main()