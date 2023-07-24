def menu_usuarios():

    usuarios=[]

    while True:
        opcion=input("Bienvenido! Que desea hacer?\nA-Iniciar Sesion\nB-Ingresar usuarios\nC-Mostrar usuarios\nD-Salir\n")
        if opcion == "A":
            nombre=input("Por favor digite su numero de usuario: ")
            clave=input("Por favor digite su clave: ")
            if (nombre, clave) in usuarios:
                print("Acceso exitoso!")
            else: print("Acceso denegado")
        elif opcion == "B":
            usuario = input("Porfavor ingrese el nombre de usuario: ")
            correo=input("Por favor ingrse su correo electronico: ")
            pin = input("Por favor ingrese el PIN: ")
            nuevo_usuario = (usuario, pin)
            usuarios.append(nuevo_usuario)
            print("El ususario ha sido registrado exitosamente!")
        elif opcion == "C":
            usuario_encontrado = False
            for user in usuarios:
                if user == usuario:
                    print(f"Los usuarios son: {usuarios[0]} ".format(usuario[0]))
                    usuario_encontrado = True
                    break
            if not usuario_encontrado:
                print("No hay usuarios registrados")
        elif opcion == "D":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
