usuarios={}

    

while True:
    opcion=input("Bienvenido! Que desea hacer?\n1-Iniciar Sesion\n2-Ingresar usuarios\n3-Mostrar usuarios\n4-Cambiar pin\n5-Salir\n")
    if opcion == "1":
        nombre=input("Por favor digite su numero de usuario: ")
        clave=input("Por favor digite su clave: ")
        if (nombre, clave) in usuarios:
            print("Acceso exitoso!")
        else: print("Acceso denegado")
    elif opcion == "2":
        usuario = input("Por favor ingrese el nombre de usuario: ")
        correo=input("Por favor ingrse su correo electronico: ")
        pin = input("Por favor ingrese el PIN: ")
        nuevo_usuario = {usuario, pin}
        usuarios[usuario] = pin
        print("El ususario ha sido registrado exitosamente!")
    elif opcion == "3":
        usuario_encontrado = False
        for key in usuarios:
            print(f"{key}:{usuarios[key]}")
        usuario_encontrado = True
        if not usuario_encontrado:
            print("No hay usuarios registrados")
            break
    elif opcion == "4":
        usuario=input("Por favor digite el usuario a editar: ")
        nuevo_pin=input("Por favor digite el nuevo pin: ")
        if usuario in usuarios:
            usuarios[usuario] = nuevo_pin
            print(f"Se ha actualizado la contraseña del usuario '{usuario}'.")
        else:
            print(f"El usuario '{usuario}' no existe en el diccionario.")
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")