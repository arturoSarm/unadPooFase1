from usuario import Usuario


# Clase Cliente con sus opciones de menú
class Cliente(Usuario):
    def mostrar_menu(self):
        while True:
            print("\n1. Consultar libros disponibles")
            print("2. Ver historial de préstamos")
            print("3. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                print("Función para consultar libros en desarrollo...")
            elif opcion == "2":
                print("Función para ver historial en desarrollo...")
            elif opcion == "3":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.")