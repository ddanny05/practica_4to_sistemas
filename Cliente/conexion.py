import mysql.connector 
from mysql.connector import Error

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',  # Cambiar si es necesario
            user='root',  # Reemplaza con tu usuario de la base de datos
            password='088266619Da.di',  # Reemplaza con tu contraseña de la base de datos
            database='Cliente'  # Nombre de la base de datos creada con Django
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Prueba de conexión
if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        conexion.close()