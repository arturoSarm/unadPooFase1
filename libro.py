from conexion_bd import conectar_bd

class Libro:
    @staticmethod
    def agregar_libro():
        # Conectar a la base de datos
        conexion = conectar_bd()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        
        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()
        
        # Solicitar al usuario que ingrese los detalles del libro
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        ango_publicacion = input("Ingrese el año de publicación: ")
        cantidad_disponible = input("Ingrese la cantidad disponible: ")
        
        # Convertir los valores de año de publicación y cantidad disponible a enteros
        try:
            ango_publicacion = int(ango_publicacion)
            cantidad_disponible = int(cantidad_disponible)
        except ValueError:
            print("Error: Año de publicación y cantidad disponible deben ser números enteros.")
            cursor.close()
            conexion.close()
            return
        
        # Ejecutar la consulta SQL para insertar los datos del libro en la base de datos
        cursor.execute("INSERT INTO libros (titulo, autor, ango_publicacion, cantidad_disponible) VALUES (%s, %s, %s, %s)",
                       (titulo, autor, ango_publicacion, cantidad_disponible))
        
        # Confirmar (commit) los cambios en la base de datos
        conexion.commit()
        
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()
        
        # Informar al usuario que el libro ha sido agregado exitosamente
        print("Libro agregado exitosamente.")