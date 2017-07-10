import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
def imprimir_algo(Btn):
	print Btn
	print 'hola world'

if __name__ == '__main__':

	ventana = Gtk.Window(title='ejemplo')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Btn 1')
	boton.connect('clicked', imprimir_algo)
	boton2 = Gtk.Button('Btn 2 ')
	boton3 = Gtk.Button('Btn 3 ')
	boton4 = Gtk.Button('Btn 4')



	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)
	contenedor.attach(
		boton, #elemento
		0, #columna
		0, #fila
		3, #Nro columna a usar
		1, #filas a uasr
		)
	contenedor.attach(boton2,1,1,1,1)
	contenedor.attach(boton3,2,1,1,1)
	contenedor.attach(boton4,0,3,1,1)
	ventana.add(contenedor)

	ventana.show_all()

	Gtk.main()

	