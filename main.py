from conexion_bd import conectar_bd
from cliente import Cliente
from empleado import Empleado

# Función para validar que la contraseña no contenga caracteres no permitidos
def validar_contraseña(contraseña):
    caracteres_no_permitidos = "$%&/*-ñ"
    if any(c in contraseña for c in caracteres_no_permitidos):
        return False
    return True

# Función para registrar un nuevo usuario en la base de datos
def registrar_usuario():
    conexion = conectar_bd()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = conexion.cursor()
    
    nombre = input("Ingrese su nombre: ")
    
    while True:
        print("Seleccione el tipo de usuario:")
        print("1. Cliente")
        print("2. Empleado")
        tipo_opcion = input("Ingrese 1 o 2: ")
        if tipo_opcion == "1":
            tipo_usuario = "cliente"
            break
        elif tipo_opcion == "2":
            tipo_usuario = "empleado"
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
    while True:
        contraseña = input("Ingrese su contraseña (sin $, %, &, /, *, -, ñ): ")
        if validar_contraseña(contraseña):
            break
        print("Error: La contraseña contiene caracteres no permitidos.")
    
    cursor.execute("INSERT INTO usuarios (nombre, tipo, contraseña) VALUES (%s, %s, %s)",
                   (nombre, tipo_usuario, contraseña))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Usuario registrado exitosamente.")

# Función para iniciar sesión verificando la contraseña
def iniciar_sesion():
    conexion = conectar_bd()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = conexion.cursor()
    
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    
    cursor.execute("SELECT contraseña, tipo FROM usuarios WHERE nombre = %s AND contraseña = %s", (nombre, contraseña))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print("Error: Nombre de usuario o contraseña incorrectos.")
    else:
        tipo_usuario = resultado[1]
        print(f"Inicio de sesión exitoso como {tipo_usuario}.")
        usuario = Cliente(nombre) if tipo_usuario == "cliente" else Empleado(nombre)
        usuario.mostrar_menu()
    
    cursor.close()
    conexion.close()

# Función para mostrar el menú principal
def menu():
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()