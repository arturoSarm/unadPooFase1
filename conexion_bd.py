import mysql.connector

# Función para establecer la conexión con la base de datos con manejo de errores
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin1234",
            database="biblioteca"
        )
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None