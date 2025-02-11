from usuario import Usuario
from libro import Libro
# Clase Empleado con sus opciones de menú
class Empleado(Usuario):
    def mostrar_menu(self):
        while True:
            print("\n1. Agregar nuevo libro")
            print("2. Gestionar préstamos y devoluciones")
            print("3. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Libro.agregar_libro() # Nos lleva a la función agregar_libro de la clase Libro
            elif opcion == "2":
                print("Función para gestionar préstamos en desarrollo...")
            elif opcion == "3":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.")
