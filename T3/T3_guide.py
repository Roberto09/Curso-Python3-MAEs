""" Temas Vistos en esta clase:
3. Pensamiento computacional en programas que involucren programación modular.
3.1 Programación modular.
3.2 Construcción de funciones y métodos que requieren cálculos matemáticos
3.3 Solución de problemas que involucren programación modular.
"""

import math

"""3.2 Construcción de funciones y métodos que requieren cálculos matemáticos."""
def formula_cuadratica(a, b, c, operacion_b):
    # formula cuadratica (-b +- sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    if(operacion_b == "suma"):
        return (-b + math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
    else:
        return (-b - math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
    
def formula_cuadratica_simplificada(a, b, c):
    x1 = (-b + math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    x2 = (-b - math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    return x1, x2 

def main():
    
    NOMBRE = input("Cual es tu nombre entrenador!?")
    print("Hola", NOMBRE, ", Pikachu necesita tu ayuda!")
    print("Introduce la ecuacion de tipo ax^2 + bx + c que describe las defensas de Charizard: ")

    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
    
    # Metodo anterior
    x1 = (-b + math.sqrt(pow(b, 2) - (4 * a * c) ) ) / (2*a)
    x2 = (-b - math.sqrt(pow(b, 2) - (4 * a * c) ) ) / (2*a)
    print("Pikachu debe atacar en los tiempos: ", x1, " y ", x2, " !")
    
    
    # Simplificacion de lo anterior utilizando formulas
    x1 = formula_cuadratica(a, b, c, "suma");
    x2 = formula_cuadratica(a, b, c, "resta");
    print("Pikachu debe atacar en los tiempos: ", x1, " y ", x2, " !")
    
    
    # Simplificamos aun mas lo anterior
    x1, x2 = formula_cuadratica_simplificada(a, b, c)
    print("Pikachu debe atacar en los tiempos: ", x1, " y ", x2, " !")
    
if __name__ == "__main__":
    main()