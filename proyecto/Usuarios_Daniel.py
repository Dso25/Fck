import string
import os
def cargar_usuarios():
    try:
        ruta_archivo = os.path.join("Usuarios", "usuarios.txt")
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
            usuarios = [linea.strip().split(",") for linea in lineas]
        return usuarios
    except FileNotFoundError:
        return []

usuarios=cargar_usuarios()

def mostrar_usuarios(usuarios):
    for indice, usuario in enumerate(usuarios):
        nombre = usuario[0]
        correo = usuario[1]
        print(f"ID: {indice} - Nombre: {nombre} - Correo: {correo}")
    print("")

def guardar_usuarios(usuarios):
    ruta_archivo = os.path.join("Usuarios", "usuarios.txt")
    with open(ruta_archivo, "w") as archivo:
        for usuario in usuarios:
            linea = ",".join(usuario) + "\n"
            archivo.write(linea)

def login(usuarios):

    intentos = 3

    while intentos > 0:

        nombre = input("\nIngrese su nombre: ")
        pin = input("\nIngrese su PIN: ")

        for usuario in usuarios:

            if usuario[0] == nombre and usuario[2] == pin:
                print("\n***** Inicio de sesión exitoso. *****\n")
                return
     
        print("\n***** Credenciales incorrectas. Intente nuevamente. *****\n")
        intentos -= 1
        
    print("\n***** Ha excedido el número de intentos permitidos. Por favor, ejecute el programa nuevamente. *****\n")  

def imprimir_casita():
    print("\n")
    print("                            _..-:-.._")
    print("                     _..--''    :    ``--.._")
    print("              _..--''           :           ``--.._")
    print("         _..-''                  :                .'``--.._")
    print("  _..--'' `.                     :              .'         |")
    print(" |          `.              _.-''|``-._       .'           |")
    print(" |            `.       _.-''     |     ``-._.'       _.-.  |")
    print(" |   |`-._      `._.-''          |  ;._     |    _.-'   |  |")
    print(" |   |    `-._    |     _.-|     |  |  `-.  |   |    _.-'  |")
    print(" |_   `-._    |   |    |   |     |  `-._ |  |   |_.-'   _.-'   ..."+"         Bienvenido al smart home de Luis Antonio")
    print("   `-._   `-._|   |    |.  |  _.-'-._   `'  |       _.-'   ..::::::..")
    print("       `-._       |    |  _|-'  *    `-._   |   _.-'   ..::::::::''")
    print("           `-._   |   _|-'.::. \|/  *    `-.|.-'   ..::::::::''")
    print("               `-.|.-' *`:::::::.. \|/  *      ..::::::::''")
    print("                      \|/  *`:::::::.. \|/ ..::::::::''")
    print("                          \|/  *`:::::::.::::::::''")
    print("                              \|/  *`::::::::''")
    print("                                  \|/  `:''")
    print("\n")

def agregar_usuario():
    while True:
        nombre = input("\nIngrese el nombre: ")
        correo = input("\nIngrese el correo electrónico: ")
        pin = input("\nIngrese el PIN (debe tener 5 dígitos): ")

        if nombre.strip() == "" or correo.strip() == "" or pin.strip() == "":
            print("\nError: No se permiten campos vacíos. Por favor, ingrese los datos nuevamente.\n")
        elif len(pin) != 5 or not pin.isdigit():
            print("\nError: El PIN debe tener exactamente 5 dígitos. Por favor, ingrese un PIN válido.\n")
        else:
            usuarios.append([nombre, correo, pin])
            guardar_usuarios(usuarios)
            print("\n****** Usuario agregado exitosamente. ******\n")
            break

def editar_usuario():
    print("\n***** Usuarios Existentes: *****\n")
    mostrar_usuarios (usuarios)
    id_usuario = int(input("\nIngrese el ID del usuario a editar: "))
    if id_usuario >= 0 and id_usuario < len(usuarios):
        usuario = usuarios[id_usuario]

        print("\n****** Información actual del usuario ******\n")
        print(f"Nombre: {usuario[0]} - Correo: {usuario[1]}")

        pin_actual = input("\nIngrese el PIN actual del usuario: ")
        if pin_actual == usuario[2]:
            nombre = input("\nIngrese el nuevo nombre (dejar en blanco para mantener el actual): ")
            if nombre.strip() == "":
                nombre = usuario[0]

            correo = input("\nIngrese el nuevo correo electrónico (dejar en blanco para mantener el actual): ")
            if correo.strip() == "":
                correo = usuario[1]

            pin_nuevo = input("\nIngrese el nuevo PIN (dejar en blanco para mantener el actual): ")
            if pin_nuevo.strip() == "":
                pin_nuevo = usuario[2]

            # Validar que el nombre no contenga solo espacios o caracteres especiales
            if not all(caracter in string.ascii_letters + string.digits for caracter in nombre):
                print("\n****** El nombre ingresado no es válido. El usuario no pudo ser editado ******\n")
                return

            usuarios[id_usuario] = [nombre, correo, pin_nuevo]
            guardar_usuarios(usuarios)
            print("\n****** Usuario actualizado exitosamente. ******\n")
        else:
            print("\n****** PIN incorrecto. No se puede editar el usuario. ******\n")
    else:
        print("\n****** ID de usuario inválido. ******\n")

def eliminar_usuario():
    id_usuario = int(input("\nIngrese el ID del usuario a eliminar: "))
    if id_usuario >= 0 and id_usuario < len(usuarios):
        del usuarios[id_usuario]
        guardar_usuarios(usuarios)
        print("\n****** Usuario eliminado exitosamente. ******\n")

    else:
        print("\n****** ID de usuario inválido. ******\n")   

def menu_usuarios():
    while True:
        print("\n***** MENU USUARIOS *****\n" + "\n1) Editar usuario." + "\n2) Eliminar usuario." + "\n3) Agregar usuario." + "\n4) Volver al menú principal.")
        equis = input("\nSeleccione una opción: ")
        if equis == "1":
            editar_usuario()
        elif equis == "2":
            eliminar_usuario()
        elif equis == "3":
            agregar_usuario()
        elif equis == "4":
            print("\n**** MENU SMART HOME *****\n" + "\n1) Menu propiedades." + "\n2) Menu usuarios." + "\n3) Salir.")
            break
        else:
            print("\n***** Opción no válida, intente nuevamente. *****\n")


