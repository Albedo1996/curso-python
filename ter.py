variable_uno='hola'
variable_dos=1
variable_tres=2.3 

# concatenacion 

cadena='cadena uno'+'cadena dos'

# interpolacion
otra_cadena='hola{}'.format('un valor')
variable_cuatro = 'hola {0} {1}'.format('val' , 'val2')
var='hola {variable} {variable}'.format(variable='val',variable2='val2')

def mi_funcion(val):
    print('dentro de mi_funcion')#un comentario
    print(otra_cadena)
    print(variable_cuatro)
    print(var)    

if __name__=='__main__':
	import argparse
	parser=argparse.ArgumentParser() 
	parser.add_argument('nombre')
	parser.add_argument('apellido')
	args =parser.parse_args()
	print(args.nombre)
	print(args.apellido)
	print(variable_cuatro.format(args.nombre, args.apellido))
   