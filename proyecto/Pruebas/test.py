import os
import Dispositivos

class Habitacion:
    def __init__(self, nombre_habitacion, dispositivos):
        self.nombre_habitacion = nombre_habitacion
        self.dispositivos = []

    def mostrar(self):
        print(f"\n* Habitación: {self.nombre_habitacion}")
        print(f"* Dispositivos: {len(self.dispositivos)}\n\n----------------")

    def editar_nombre(self, nuevo_nombre):
        self.nombre_habitacion = nuevo_nombre

class Propiedad:
    def __init__(self, nombre_propiedad, habitaciones):
        self.nombre_propiedad = nombre_propiedad
        self.habitaciones = []

    def mostrar(self):
        print(f"\nPropiedad: {self.nombre_propiedad}")
        habitaciones_contadas = {}

        for habitacion in self.habitaciones:
            if habitacion.nombre_habitacion not in habitaciones_contadas:
                habitaciones_contadas[habitacion.nombre_habitacion] = 1
            else:
                habitaciones_contadas[habitacion.nombre_habitacion] += 1

        print(f"Habitaciones: {len(habitaciones_contadas)}")
        for habitacion, cantidad in habitaciones_contadas.items():
            print(f"\n* Habitación: {habitacion}")
            print(f"* Dispositivos: {cantidad}\n\n----------------")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def editar_nombre(self, nuevo_nombre):
        self.nombre_propiedad = nuevo_nombre

def ver_propiedad():
    ruta_propiedades = "Propiedades"
    archivo_propiedades = os.path.join(ruta_propiedades, "propiedades.txt")

    if not os.path.exists(archivo_propiedades):
        print("No hay propiedades registradas.")
        return None

    with open(archivo_propiedades, "r") as archivo:
        nombres_propiedades = archivo.read().splitlines()

    if not nombres_propiedades:
        print("No hay propiedades registradas.")
        return None

    for num_propiedad, nombre_propiedad in enumerate(nombres_propiedades, start=1):
        print(f"{num_propiedad}. {nombre_propiedad}")

    seleccion = input("Seleccione el número de la propiedad que desea ver: ")
    try:
        seleccion = int(seleccion)
        if seleccion < 1 or seleccion > len(nombres_propiedades):
            raise ValueError()
    except ValueError:
        print("Selección inválida.")
        return None

    nombre_propiedad_seleccionada = nombres_propiedades[seleccion - 1]
    archivo_propiedad = f"{nombre_propiedad_seleccionada}.txt"
    ruta_archivo = os.path.join(ruta_propiedades, archivo_propiedad)

    if not os.path.exists(ruta_archivo):
        print(f"La propiedad '{nombre_propiedad_seleccionada}' no existe.")
        return None

    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    habitaciones = []
    habitacion_actual = None

    for linea in lineas:
        if linea.startswith("Nombre de la habitacion:"):
            if habitacion_actual is not None:
                habitaciones.append(habitacion_actual)
            habitacion_actual = {"nombre": linea.strip().split(": ")[1], "dispositivos": []}
        elif linea.startswith("Nombre del dispositivo:"):
            dispositivo = linea.strip().split(": ")[1]
            habitacion_actual["dispositivos"].append(dispositivo)

    if habitacion_actual is not None:
        habitaciones.append(habitacion_actual)

    print(f"\n---- Propiedad seleccionada -----")
    print(f"\nPropiedad: {nombre_propiedad_seleccionada}")

    habitaciones_contadas = {}
    for habitacion in habitaciones:
        nombre_habitacion = habitacion["nombre"]
        if nombre_habitacion in habitaciones_contadas:
            habitaciones_contadas[nombre_habitacion] += 1
        else:
            habitaciones_contadas[nombre_habitacion] = 1

    print(f"Habitaciones: {len(habitaciones_contadas)}")

    for nombre_habitacion, repeticiones in habitaciones_contadas.items():
        dispositivos = habitaciones[0]["dispositivos"]
        cantidad_dispositivos = len(dispositivos)
        dispositivos_reales = cantidad_dispositivos * repeticiones
        print(f"\n* Habitación: {nombre_habitacion}")
        print(f"* Dispositivos: {dispositivos_reales}")

    print("----------------")

    return nombre_propiedad_seleccionada

def guardar_propiedades(propiedades):
    try:
        ruta_archivo = os.path.join("Propiedades", "propiedades.txt")

        with open(ruta_archivo, "w") as archivo_propiedades:
            for propiedad in propiedades:
                archivo_propiedades.write(f"{propiedad.nombre_propiedad}\n")
    except IOError:
        print("Error al guardar el archivo de propiedades.")

def cargar_habitaciones(nombre_propiedad):
    habitaciones = []

    try:
        ruta_archivo = os.path.join("Propiedades", f"{nombre_propiedad}.txt")
        dispositivos = Dispositivos.cargar_dispositivos(ruta_archivo)
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()

        habitacion_actual = None

        for linea in lineas:
            if linea.startswith("Nombre de la habitacion:"):
                if habitacion_actual is not None:
                    habitacion = Habitacion(habitacion_actual["nombre"], dispositivos)
                    habitaciones.append(habitacion)
                habitacion_actual = {}
                habitacion_actual["nombre"] = linea.strip().split(": ")[1]
        if habitacion_actual is not None:
            habitacion = Habitacion(habitacion_actual["nombre"], dispositivos)
            habitaciones.append(habitacion)

        return habitaciones

    except FileNotFoundError:
        print(f"No se encontró el archivo de habitaciones de la propiedad '{nombre_propiedad}'. Se creará uno nuevo.")

    return habitaciones

def cargar_propiedades():
    propiedades = []

    try:
        ruta_archivo = os.path.join("Propiedades", "propiedades.txt")

        with open(ruta_archivo, "r") as archivo_propiedades:
            for linea in archivo_propiedades:
                nombre_propiedad = linea.strip()
                habitaciones = cargar_habitaciones(nombre_propiedad)
                propiedad = Propiedad(nombre_propiedad, habitaciones)
                propiedades.append(propiedad)
    except FileNotFoundError:
        print("No se encontró el archivo de propiedades. Se creará uno nuevo.")

    return propiedades

def ver_propiedades(propiedades):
    if not propiedades:
        print("No hay propiedades registradas.")
    else:
        ruta_propiedades = "Propiedades"
        archivo_propiedades = os.path.join(ruta_propiedades, "propiedades.txt")

        if not os.path.exists(archivo_propiedades):
            print("No hay propiedades registradas.")
            return

        with open(archivo_propiedades, "r") as archivo:
            nombres_propiedades = archivo.read().splitlines()

        if not nombres_propiedades:
            print("No hay propiedades registradas.")
            return

        for num_propiedad, nombre_propiedad in enumerate(nombres_propiedades, start=1):
            archivo_propiedad = f"{nombre_propiedad}.txt"
            ruta_archivo = os.path.join(ruta_propiedades, archivo_propiedad)

            if not os.path.exists(ruta_archivo):
                print(f"La propiedad '{nombre_propiedad}' no existe.")
                continue

            with open(ruta_archivo, "r") as archivo:
                lineas = archivo.readlines()

            habitaciones = []
            habitacion_actual = None

            for linea in lineas:
                if linea.startswith("Nombre de la habitacion:"):
                    if habitacion_actual is not None:
                        habitaciones.append(habitacion_actual)
                    habitacion_actual = {"nombre": linea.strip().split(": ")[1], "dispositivos": []}
                elif linea.startswith("Nombre del dispositivo:"):
                    dispositivo = linea.strip().split(": ")[1]
                    habitacion_actual["dispositivos"].append(dispositivo)

            if habitacion_actual is not None:
                habitaciones.append(habitacion_actual)

            print(f"\n---- Propiedad #{num_propiedad} -----")
            print(f"\nPropiedad: {nombre_propiedad}")

            habitaciones_contadas = {}
            for habitacion in habitaciones:
                nombre_habitacion = habitacion["nombre"]
                if nombre_habitacion in habitaciones_contadas:
                    habitaciones_contadas[nombre_habitacion] += 1
                else:
                    habitaciones_contadas[nombre_habitacion] = 1

            print(f"Habitaciones: {len(habitaciones_contadas)}")

            for nombre_habitacion, repeticiones in habitaciones_contadas.items():
                dispositivos = habitaciones[0]["dispositivos"]
                cantidad_dispositivos = len(dispositivos)
                dispositivos_reales = cantidad_dispositivos * repeticiones
                print(f"\n* Habitación: {nombre_habitacion}")
                print(f"* Dispositivos: {dispositivos_reales}")

            print("----------------")

def editar_nombre_propiedad(propiedad):
    print("\n***** EDITAR NOMBRE DE LA PROPIEDAD *****")
    ver_propiedad()

    nuevo_nombre_propiedad = input("\nIngrese el nuevo nombre de la propiedad: ")

    if nuevo_nombre_propiedad:
        # Verificar si el nombre ha cambiado
        if propiedad.nombre_propiedad != nuevo_nombre_propiedad:
            # Renombrar el archivo de la propiedad
            ruta_original = os.path.join("Propiedades", f"{propiedad.nombre_propiedad}.txt")
            ruta_nueva = os.path.join("Propiedades", f"{nuevo_nombre_propiedad}.txt")

            try:
# Actualizar el archivo propiedades.txt
                ruta_archivo_propiedades = os.path.join("Propiedades", "propiedades.txt")
                with open(ruta_archivo_propiedades, "r") as archivo:
                    lineas = archivo.readlines()
                with open(ruta_archivo_propiedades, "w") as archivo:
                    for linea in lineas:
                        if linea.strip() == propiedad.nombre_propiedad:
                            archivo.write(f"{nuevo_nombre_propiedad}\n")
                        else:
                            archivo.write(linea)
                os.rename(ruta_original, ruta_nueva)
                propiedad.nombre_propiedad = nuevo_nombre_propiedad
                print("\n***** Nombre de propiedad editado exitosamente. *****")
            except OSError as e:
                print(f"\n***** Error al renombrar el archivo: {e}. No se realizaron cambios. *****")
        else:
            print("\n***** El nuevo nombre es igual al nombre actual. No se realizaron cambios. *****")
    else:
        print("\n***** Error: Nombre de propiedad inválido. *****")

def editar_propiedad_menu(propiedades):
    print("\n***** EDITAR PROPIEDAD *****")
    ver_propiedades(propiedades)

    if not propiedades:
        print("No hay propiedades registradas.")
        return

    opcion_propiedad = input("\nSeleccione el número de la propiedad que desea editar (o '0' para cancelar): ")
    if not opcion_propiedad.isdigit() or int(opcion_propiedad) < 0 or int(opcion_propiedad) > len(propiedades):
        print("\n***** Error: Opción inválida. *****")
        return

    if opcion_propiedad == '0':
        print("\n***** Edición de propiedad cancelada. *****")
        return

    propiedad = propiedades[int(opcion_propiedad) - 1]

    while True:
        print("\n¿Qué acción desea realizar?")
        print("1) Editar nombre de la propiedad.")
        print("2) Eliminar la propiedad.")
        print("3) Editar habitaciones de la propiedad.")
        print("0) Volver atrás.")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            editar_nombre_propiedad(propiedad)

        elif opcion == "2":
            eliminar_propiedad(propiedades, propiedad)

        elif opcion == "3":
            editar_habitaciones(propiedad)

        elif opcion == "0":
            print("\n***** Volviendo atrás. *****")
            break

        else:
            print("\n***** Opción no válida, intente nuevamente. *****")

    print("\n***** Propiedad editada exitosamente. *****")

            
def agregar_propiedad(propiedades):
    print("\n***** AGREGAR PROPIEDAD *****")

    nombre_propiedad = input("Ingrese el nombre de la propiedad: ")
    habitaciones = []

    num_habitaciones = input("Ingrese el número de habitaciones: ")
    if not num_habitaciones.isdigit():
        print("\n***** Error: Número de habitaciones inválido. *****")
        return

    num_habitaciones = int(num_habitaciones)

    for i in range(num_habitaciones):
        print(f"\nHabitación #{i + 1}")
        nombre_habitacion = input("Ingrese el nombre de la habitación: ")
        num_dispositivos = input("Ingrese el número de dispositivos: ")

        if not num_dispositivos.isdigit():
            print("\n***** Error: Número de dispositivos inválido. *****")
            return

        num_dispositivos = int(num_dispositivos)
        dispositivos = []

        for j in range(num_dispositivos):
            nombre_dispositivo = input(f"Ingrese el nombre del dispositivo #{j + 1}: ")
            Dispositivos.agregar_dispositivo(nombre_habitacion, nombre_dispositivo, nombre_propiedad)

        habitacion = Habitacion(nombre_habitacion, dispositivos)
        habitaciones.append(habitacion)

    propiedad = Propiedad(nombre_propiedad, habitaciones)
    propiedades.append(propiedad)
    guardar_propiedades(propiedades)
    print("\n***** Propiedad agregada exitosamente. *****")

def editar_propiedad(propiedades):
    print("\n***** EDITAR PROPIEDAD *****")
    ver_propiedades(propiedades)

    if not propiedades:
        print("No hay propiedades registradas.")
        return

    opcion_propiedad = input("\nSeleccione el número de la propiedad que desea editar (o '0' para cancelar): ")
    if not opcion_propiedad.isdigit() or int(opcion_propiedad) < 0 or int(opcion_propiedad) > len(propiedades):
        print("\n***** Error: Opción inválida. *****")
        return

    if opcion_propiedad == '0':
        print("\n***** Edición de propiedad cancelada. *****")
        return

    propiedad = propiedades[int(opcion_propiedad) - 1]

    while True:
        print("\n¿Qué acción desea realizar?")
        print("1) Editar nombre de la propiedad.")
        print("2) Editar habitaciones de la propiedad.")
        print("3) Eliminar la propiedad.")
        print("0) Volver atrás.")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nuevo_nombre_propiedad = input("Ingrese el nuevo nombre de la propiedad: ")

            if nuevo_nombre_propiedad:
                # Verificar si el nombre ha cambiado
                if propiedad.nombre_propiedad != nuevo_nombre_propiedad:
                    # Renombrar el archivo de la propiedad
                    ruta_original = os.path.join("Propiedades", f"{propiedad.nombre_propiedad}.txt")
                    ruta_nueva = os.path.join("Propiedades", f"{nuevo_nombre_propiedad}.txt")
                    os.rename(ruta_original, ruta_nueva)
                    propiedad.nombre_propiedad = nuevo_nombre_propiedad
                    print("\n***** Nombre de propiedad editado exitosamente. *****")
                else:
                    print("\n***** El nuevo nombre es igual al nombre actual. No se realizaron cambios. *****")
            else:
                print("\n***** Error: Nombre de propiedad inválido. *****")

        elif opcion == "2":
            # Agregar, editar o eliminar habitaciones
            while True:
                print("\n***** EDITAR HABITACIONES *****")
                propiedad.mostrar()
                print("Seleccione una opción:")
                print("1) Agregar habitación.")
                print("2) Editar nombre de una habitación.")
                print("3) Eliminar una habitación.")
                print("0) Volver atrás.")

                opcion_habitacion = input("\nSeleccione una opción: ")

                if opcion_habitacion == "1":
                    # Agregar habitación
                    nombre_habitacion = input("Ingrese el nombre de la habitación: ")
                    num_dispositivos = input("Ingrese el número de dispositivos: ")

                    if not num_dispositivos.isdigit():
                        print("\n***** Error: Número de dispositivos inválido. *****")
                        continue

                    num_dispositivos = int(num_dispositivos)
                    dispositivos = []

                    for j in range(num_dispositivos):
                        nombre_dispositivo = input(f"Ingrese el nombre del dispositivo #{j + 1}: ")
                        Dispositivos.agregar_dispositivo(nombre_habitacion, nombre_dispositivo, propiedad.nombre_propiedad)

                    habitacion = Habitacion(nombre_habitacion, dispositivos)
                    propiedad.agregar_habitacion(habitacion)
                    guardar_propiedades(propiedades)
                    cargar_propiedades(propiedades)
                    print("\n***** Habitación agregada exitosamente. *****")

                elif opcion_habitacion == "2":
                    # Editar nombre de una habitación
                    if not propiedad.habitaciones:
                        print("No hay habitaciones registradas en esta propiedad.")
                        continue

                    print("Habitaciones existentes:")
                    habitaciones_existentes = {}
                    for habitacion in propiedad.habitaciones:
                        habitaciones_existentes[habitacion.nombre] = habitaciones_existentes.get(habitacion.nombre, 0) + 1

                    for i, habitacion in enumerate(propiedad.habitaciones):
                        if habitaciones_existentes[habitacion.nombre] > 1:
                            print(f"{i + 1}) {habitacion.nombre} (x{habitaciones_existentes[habitacion.nombre]})")
                        else:
                            print(f"{i + 1}) {habitacion.nombre}")

                    opcion_nombre_habitacion = input("Seleccione el número de la habitación que desea editar (o '0' para cancelar): ")
                    if not opcion_nombre_habitacion.isdigit() or int(opcion_nombre_habitacion) < 0 or int(opcion_nombre_habitacion) > len(propiedad.habitaciones):
                        print("\n***** Error: Opción inválida. *****")
                        continue

                    if opcion_nombre_habitacion == '0':
                        print("\n***** Edición de nombre de habitación cancelada. *****")
                        continue

                    habitacion = propiedad.habitaciones[int(opcion_nombre_habitacion) - 1]
                    nuevo_nombre_habitacion = input("Ingrese el nuevo nombre de la habitación: ")

                    if nuevo_nombre_habitacion:
                        habitacion.editar_nombre(nuevo_nombre_habitacion)
                        guardar_propiedades(propiedades)
                        cargar_propiedades(propiedades)  # Cargar las propiedades actualizadas
                        print("\n***** Nombre de habitación editado exitosamente. *****")
                    else:
                        print("\n***** Error: Nombre de habitación inválido. *****")

                elif opcion_habitacion == "3":
                    # Eliminar una habitación

                    print("Habitaciones existentes:")
                    habitaciones_existentes = {}
                    for habitacion in propiedad.habitaciones:
                        habitaciones_existentes[habitacion.nombre] = habitaciones_existentes.get(habitacion.nombre, 0) + 1

                    for i, habitacion in enumerate(propiedad.habitaciones):
                        if habitaciones_existentes[habitacion.nombre] > 1:
                            print(f"{i + 1}) {habitacion.nombre} (x{habitaciones_existentes[habitacion.nombre]})")
                        else:
                            print(f"{i + 1}) {habitacion.nombre}")

                    opcion_eliminar_habitacion = input("Seleccione el número de la habitación que desea eliminar (o '0' para cancelar): ")
                    if not opcion_eliminar_habitacion.isdigit() or int(opcion_eliminar_habitacion) < 0 or int(opcion_eliminar_habitacion) > len(propiedad.habitaciones):
                        print("\n***** Error: Opción inválida. *****")
                        continue

                    if opcion_eliminar_habitacion == '0':
                        print("\n***** Eliminación de habitación cancelada. *****")
                        continue

                    habitacion_eliminar = propiedad.habitaciones[int(opcion_eliminar_habitacion) - 1]
                    propiedad.habitaciones = [habitacion for habitacion in propiedad.habitaciones if habitacion.nombre != habitacion_eliminar.nombre]
                    Dispositivos.eliminar_dispositivos_por_habitacion(habitacion_eliminar.nombre, propiedad.nombre_propiedad)
                    guardar_propiedades(propiedades)
                    cargar_propiedades(propiedades)  # Cargar las propiedades actualizadas
                    print("\n***** Habitación eliminada exitosamente. *****")

                elif opcion_habitacion == "0":
                    # Volver atrás
                    break

                else:
                    print("\n***** Error: Opción inválida. *****")

        elif opcion == "3":
            # Eliminar la propiedad
            confirmacion = input(f"\n¿Está seguro de que desea eliminar la propiedad '{propiedad.nombre_propiedad}'? (S/N): ")
            if confirmacion.lower() == "s":
                os.remove(os.path.join("Propiedades", f"{propiedad.nombre_propiedad}.txt"))
                propiedades.remove(propiedad)
                guardar_propiedades(propiedades)
                print("\n***** Propiedad eliminada exitosamente. *****")
                break
            elif confirmacion.lower() == "n":
                print("\n***** Eliminación de propiedad cancelada. *****")
                break
            else:
                print("\n***** Error: Opción inválida. *****")

        elif opcion == "0":
            # Volver atrás
            break

        else:
            print("\n***** Error: Opción inválida. *****")

def menu_propiedades():
    propiedades = cargar_propiedades()

    while True:
        print("\n***** MENÚ PROPIEDADES *****")
        print("1) Ver propiedades.")
        print("2) Agregar propiedad.")
        print("3) Editar propiedad.")
        print("4) Salir al menú principal.")

        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            ver_propiedades(propiedades)
        elif opcion == "2":
            agregar_propiedad(propiedades)
        elif opcion == "3":
            editar_propiedad_menu(propiedades)
        elif opcion == "4":
            guardar_propiedades(propiedades)
            print("\n***** Volviendo al menú principal. *****\n")
            break
        else:
            print("\n***** Opción no válida, intente nuevamente. *****\n")




menu_propiedades()