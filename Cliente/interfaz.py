import tkinter as tk
from tkinter import messagebox
from conexion import conectar_bd

# Función para guardar datos en la base de datos
def guardar_datos():
    if cedula.get() ==  ''or nombre.get() == '' or apellido.get() == '' or telefono.get() == '' or direccion.get() == '':
        messagebox.showerror('Error', 'Todos los campos son obligatorios')
        return

    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO app_cliente (cedula, nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s, %s)",
                (cedula.get(), nombre.get(), apellido.get(), telefono.get(), direccion.get())
            )
            conexion.commit()
            messagebox.showinfo('Correcto', 'Datos guardados correctamente')
        except Exception as e:
            messagebox.showerror('Error', f'Error al guardar los datos: {str(e)}')
        finally:
            cursor.close()
            conexion.close()
    borrar_datos()

# Función para borrar los campos de entrada
def borrar_datos():
    cedula.set('')
    nombre.set('')
    apellido.set('')
    telefono.set('')
    direccion.set('')

# Construcción de la ventana
ventana = tk.Tk()
ventana.title('Sistema de Registro de Clientes')
ventana.geometry('400x300')

# Variables
cedula = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()

# Etiquetas y entradas
labels = ['Cédula:', 'Nombre:', 'Apellido:', 'Teléfono:', 'Dirección:']
variables = [cedula, nombre, apellido, telefono, direccion]

for i, (text, var) in enumerate(zip(labels, variables)):
    tk.Label(ventana, text=text).grid(row=i, column=0, padx=10, pady=5, sticky='e')
    tk.Entry(ventana, textvariable=var).grid(row=i, column=1, padx=10, pady=5)

# Botones
boton_guardar = tk.Button(ventana, text='Guardar', command=guardar_datos)
boton_borrar = tk.Button(ventana, text='Borrar', command=borrar_datos)

boton_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)
boton_borrar.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
