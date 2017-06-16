

if __name__ == '__main__':
    nombre = input("digita tu name")
    apellido = input("digita tu apellido")
    edad = int(input("deigita tu edad"))
    cumple = 100 - edad
    cumplira = 2017 + cumple
    mensaje = "<< {nombre} >>, cumplira 100 en el: {anio}"

    print(mensaje.format(nombre=nombre, anio=cumplira))
