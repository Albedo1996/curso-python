import argparse


if __name__ == '__main__':
	parser= argparse.ArgumentParser('valor')
	parser.add_argument('Nombre')

args = parser.parse_args()

datos = {
	'Nombre': {
	    'edad': 22,
	    'direccion': 'crusero' 
	    }
    }
    	
if args.Nombre in datos:
	print 'La llave {Nombre} existe en el diccionario'.format(Nombre=args.Nombre)		
else:
	print 'La llave {Nombre} no existe'.format(Nombre=args.Nombre)	

	