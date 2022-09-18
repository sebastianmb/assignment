import tkinter as tk
from turtle import width

def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label ='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label = 'Crear registro en BD')
    menu_inicio.add_command(label = 'Eliminar registro en BD')
    menu_inicio.add_command(label = 'Salir', command= root.destroy)

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root )
        self._root = root
        
        self.pack()
        self.config(width= 500, height=500,bg="#b7f0d8")
        self.recepcion()
    
    def recepcion(self):
        self.label_planilla= tk.Label(self, text='Registro Planilla')
        self.label_planilla.grid(row = 0, column = 0)
        