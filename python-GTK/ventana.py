import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


if __name__ == '__main__':

	ventana = Gtk.Window(title='ejemplo')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Btn 1')
	
	boton2 = Gtk.Button('Btn 2 ')

	contenedor = Gtk.VBox()
	contenedor.pack_start(boton, True, True, 0)
	contenedor.pack_end(boton2, True,True, 0)
	ventana.add(contenedor)
	ventana.show_all()

	Gtk.main() 