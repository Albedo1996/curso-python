import gi 

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Miventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
	    super(Miventana, self).__init__(*args, **kwargs)
	    self.set_default_size(500, 300)
	    self.connect('delete-event', Gtk.main_quit)

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
    text = Gtk.Entry(text = 'hola world')
    boton = Gtk.Button('botn 1')
    label = Gtk.label('DS')


if __name__=='__main__':
	ventana = Miventana()
	ventana.add(text)
	ventana.add(label)
	ventana.add(boton)
	ventana.show_all()

	Gtk.main()