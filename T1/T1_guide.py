"""
TEMAS:
- IDE
- Estructura básica de un programa.
    Main
    Procedural
    Función print

- Variables y constantes
    Variables
    Constantes
    Tipos de datos
    Función type
"""

def main():
    # Variables y constantes
    # Esta es una variable
    edad_alumno = 20
    
    # Esta es una constante
    NOMBRE_ALUMNO = "Roberto"

    print(edad_alumno)
    print(NOMBRE_ALUMNO)
    
    # Tipos de datos
    NUMERO_PI = 3.1416
    numero_a = -4 #int
    numero_b = 10.2 #float
    texto = "mensaje de texto" #string
    
    print("Tipo numero_a: ", type(numero_a))
    print("Tipo numero_b: ", type(numero_b))
    print("Tipo texto: ", type(texto))

if __name__ == '__main__':
    main()