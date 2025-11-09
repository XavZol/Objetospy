#While for 

pregunta = 'Agrega un numero y te dire si es par o impar\r\n'
pregunta += ' (Escribe cerrar para salir de la aplicacion ) \r\n'
preguntar = True

while preguntar:
    
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        # 1. Convierte a entero SOLO si no es "cerrar"
        numero = int(numero) 

        # 2. Revisa si es par/impar DENTRO del else
        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else: 
            print(f'El numero {numero} es impar')

print("¡Hasta luego!") # Mensaje de salida opcional