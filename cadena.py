#dado el texto 'esto es una prueva ' imprimir una cadena formateada de la sig. manera:

#'esto es una prueva '

#-imprimir cuentas letras 'e' tiene la cadena
#-capitalizar cadena
#-imprir longitud de cadena 
#-reemplazar
dato = (input("Ingrese un texto: "))
fruta = dato
cuenta = 0
for carac in fruta:
    if carac == "e":
        cuenta += 1
print("caracteres de e: ",cuenta)
print("Capitalizar:",dato.upper())
print("Longitud: ",len(dato))
print("Reemplazando: ", dato.replace("o","0"))
    
