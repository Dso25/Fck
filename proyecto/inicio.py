import Usuarios_R
import Propiedades
import Usuarios_Daniel
usuarios=Usuarios_Daniel.cargar_usuarios()
Propiedades.cargar_propiedades()


def inicio_sesion():

    while True:
        tiene_cuenta = input("\n¿Tienes usuario? (s/n): ")
        if tiene_cuenta.lower() == "s":
            Usuarios_Daniel.login(usuarios)
            break
        elif tiene_cuenta.lower() == "n":
            while True:
                print ("\nlos usurios registrados actualmente son:\n")
                Usuarios_Daniel.mostrar_usuarios(usuarios)
                desea_crear = input("\n¿Desea crear un nuevo usuario? (s/n): ")
                if desea_crear.lower() == "s":
                    Usuarios_Daniel.agregar_usuario(usuarios)
                    Usuarios_Daniel.guardar_usuarios(usuarios)
                    print("\n****** Nuevo inicio de sesion ******\n")
                    Usuarios_Daniel.login(usuarios)
                    return
                elif desea_crear.lower() == "n":
                    while True:
                        desea_salir = input("\n¿Desea salir del programa? (s/n): ")
                        if desea_salir.lower() == "s":
                            print("\n¡Hasta pronto!\n")
                            return
                        elif desea_salir.lower() == "n":
                            break
                        else:
                            print("\nOpción inválida, intente nuevamente.\n")
                    # Preguntar nuevamente si tiene usuario después de seleccionar que no desea salir
                    break
                else:
                    print("\nOpción inválida, intente nuevamente.\n")
        else:
            print("\nOpción inválida, intente nuevamente.\n")

def menu():
    while True:
        print("\n**** MENU SMART HOME *****\n" + "\n1) Menu propiedades." + "\n2) Menu usuarios." + "\n3) Salir.")
        cursor = input("\nSeleccione una opción: ")
        if cursor == "1":
            Propiedades.menu_propiedades()
        elif cursor == "2":
            Usuarios_R.menu_usuarios()
        elif cursor == "3":
            print("\n    ¡Hasta pronto!    \n")
            break
        else:
            print("\n***** Opción no válida, intente nuevamente. *****\n")

Usuarios_Daniel.imprimir_casita()
#inicio_sesion()
menu()

