from datetime import datetime
import os

class Dispositivo:
    def __init__(self):
        self.nombre = None
        self.horario = False
        self.hora_encendido = None
        self.hora_apagado = None
        self.dias= []
        self.estado = False
   
    def encender(self):
        self.estado = True
        print(f"El dispositivo {self.nombre} ha sido encendido.")

    def apagar(self):
        self.estado = False
        print(f"El dispositivo {self.nombre} ha sido apagado.")

def cargar_dispositivos(ruta_archivo):
    dispositivos = []

    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    dispositivo_actual = None

    for linea in lineas:
        if linea.startswith("Nombre del dispositivo:"):
            if dispositivo_actual is not None:
                dispositivos.append(dispositivo_actual)
            dispositivo_actual = {}
            dispositivo_actual["nombre"] = linea.strip().split(": ")[1]
        elif linea.startswith("Estado:"):
            dispositivo_actual["estado"] = linea.strip().split(": ")[1]
        elif linea.startswith("Hora de encendido:"):
            dispositivo_actual["hora_encendido"] = linea.strip().split(": ")[1]
        elif linea.startswith("Hora de apagado:"):
            dispositivo_actual["hora_apagado"] = linea.strip().split(": ")[1]
        elif linea.startswith("Días en que se repetirá el horario:"):
            dias_repetir = linea.strip().split(": ")[1]
            if dias_repetir == "None":
                dispositivo_actual["dias_repetir"] = []
            else:
                dispositivo_actual["dias_repetir"] = dias_repetir.split(", ")

    # Agregar el último dispositivo a la lista
    if dispositivo_actual is not None:
        dispositivos.append(dispositivo_actual)

    return dispositivos


def agregar_dispositivo(nombre_habitacion, nombre_dispositivo, nombre_propiedad):
    dispositivo = Dispositivo()
    while True:
        agregar_horario = input("¿Desea agregar un horario de encendido para el dispositivo? (s/n): ")

        # Verificar estado válido
        while True:
            estado_dispositivo = input("¿Cuál es el actual estado del dispositivo? (encendido/apagado): ")
            if estado_dispositivo.lower() == "encendido":
                dispositivo.estado = True
                break
            elif estado_dispositivo.lower() == "apagado":
                dispositivo.estado = False
                break
            else:
                print("\n***** Seleccione un estado válido. *****\n")

        if agregar_horario.lower() == "s":
            dispositivo.nombre = nombre_dispositivo
            # Verificar hora de encendido válida
            while True:
                hora_encendido = input("Ingrese la hora de encendido (formato 24 horas - HH:MM): ")
                try:
                    horario_encendido = datetime.strptime(hora_encendido, "%H:%M")
                    dispositivo.hora_encendido = horario_encendido.time()
                    break
                except ValueError:
                    print("Error: Formato de hora incorrecto. Utilice el formato HH:MM.")

            # Verificar hora de apagado válida
            while True:
                hora_apagado = input("Ingrese la hora de apagado (formato 24 horas - HH:MM): ")
                try:
                    horario_apagado = datetime.strptime(hora_apagado, "%H:%M")
                    dispositivo.hora_apagado = horario_apagado.time()
                    break
                except ValueError:
                    print("Error: Formato de hora incorrecto. Utilice el formato HH:MM.")

            # Verificar días de repetición válidos
            while True:
                dias_repetir = input("Ingrese los días en que se repetirá el horario (lunes a domingo, separados por comas): ")
                dias_repetir = [dia.strip() for dia in dias_repetir.split(",")]
                if all(dia.lower() in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"] for dia in dias_repetir):
                    dias_repetir = sorted(dias_repetir, key=lambda dia: ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"].index(dia.lower()))
                    dispositivo.dias = dias_repetir
                    break
                else:
                    print("Error: Ingrese días válidos (lunes a domingo).")

        elif agregar_horario.lower() == "n":
            dispositivo.nombre = nombre_dispositivo
        
        # Guardar datos en el archivo "dispositivos.txt"
        ruta_archivo = os.path.join("Propiedades", f"{nombre_propiedad}.txt")
        with open(ruta_archivo, "a") as archivo:
            archivo.write(f"\nNombre de la habitacion: {nombre_habitacion}\n")
            archivo.write(f"Nombre del dispositivo: {dispositivo.nombre}\n")
            archivo.write(f"Estado: {'Encendido' if dispositivo.estado else 'Apagado'}\n")
            
            if agregar_horario.lower() == "s":
                archivo.write(f"Hora de encendido: {dispositivo.hora_encendido}\n")
                archivo.write(f"Hora de apagado: {dispositivo.hora_apagado}\n")
                archivo.write("Días en que se repetirá el horario: ")
                archivo.write(", ".join(dispositivo.dias))
                archivo.write("\n\n")
            else:
                archivo.write("Horario de encendido: No especificado\n")
                archivo.write("Horario de apagado: No especificado\n")
                archivo.write("Días en que se repetirá el horario: No especificado\n")
                archivo.write("\n\n")
        break

def mostrar_dispositivos(nombre_propiedad, nombre_habitacion):
    dispositivos_encontrados = []
    ruta_archivo = os.path.join("Dispositivos", "dispositivos.txt")

    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    for i in range(len(lineas)):
        if nombre_propiedad in lineas[i] and nombre_habitacion in lineas[i]:
            dispositivo = {}
            dispositivo["nombre"] = lineas[i + 1].strip().split(": ")[1]
            dispositivo["encendido"] = lineas[i + 2].strip().split(": ")[1]
            dispositivo["hora_encendido"] = lineas[i + 3].strip().split(": ")[1]
            dispositivo["hora_apagado"] = lineas[i + 4].strip().split(": ")[1]

            # Verificar si el índice i + 5 está dentro de los límites de la lista lineas
            if i + 5 < len(lineas):
                dias_repetir_linea = lineas[i + 5].strip().split(": ")[1]
                if dias_repetir_linea:
                    dispositivo["dias_repetir"] = dias_repetir_linea.split(", ")
                else:
                    dispositivo["dias_repetir"] = []
            else:
                dispositivo["dias_repetir"] = []

            dispositivos_encontrados.append(dispositivo)

    # Mostrar dispositivos encontrados
    if dispositivos_encontrados:
        print(f"\nDispositivos encontrados en {nombre_propiedad} - {nombre_habitacion}: " + str(len(dispositivos_encontrados))+"\n")
        for i, dispositivo in enumerate(dispositivos_encontrados, start=1):
            print("\n***** Dispositivo", i, "*****\n")
            print("Nombre del dispositivo:", dispositivo["nombre"])
            print("Encendido:", dispositivo["encendido"])
            print("Horario de encendido:", dispositivo["hora_encendido"])
            print("Horario de apagado:", dispositivo["hora_apagado"])
            print("Días en que se repetirá el horario:", ", ".join(dispositivo["dias_repetir"]))
            print()
    else:
        print(f"No se encontraron dispositivos en {nombre_propiedad} - {nombre_habitacion}.")

def editar_dispositivo(propiedad, habitacion):
    dispositivos = cargar_dispositivos()  # Llamamos a la función cargar_dispositivos para obtener la lista de dispositivos existentes

    # Filtrar dispositivos por propiedad y habitación
    dispositivos_filtrados = [dispositivo for dispositivo in dispositivos if dispositivo["propiedad"] == propiedad and dispositivo["habitacion"] == habitacion]

    if not dispositivos_filtrados:
        print(f"No se encontraron dispositivos en la propiedad '{propiedad}' y la habitación '{habitacion}'.")
        return

    # Mostrar la lista de dispositivos encontrados
    print(f"Dispositivos encontrados en la propiedad '{propiedad}' y la habitación '{habitacion}':")
    for i, dispositivo in enumerate(dispositivos_filtrados):
        print(f"{i+1}. {dispositivo['nombre']}")

    # Pedir al usuario que seleccione el dispositivo a editar
    while True:
        try:
            indice_dispositivo = int(input("Seleccione el número de dispositivo que desea editar: "))
            if indice_dispositivo >= 1 and indice_dispositivo <= len(dispositivos_filtrados):
                break
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Selección inválida. Intente nuevamente.")

    dispositivo_seleccionado = dispositivos_filtrados[indice_dispositivo - 1]

    print("\nDispositivo seleccionado:")
    print("Nombre:", dispositivo_seleccionado.get("nombre", ""))
    print("Estado:", dispositivo_seleccionado.get("estado", ""))
    print("Horario de encendido:", dispositivo_seleccionado.get("hora_encendido", "No especificado"))
    print("Horario de apagado:", dispositivo_seleccionado.get("hora_apagado", "No especificado"))
    print("Días en que se repite el horario:", ", ".join(dispositivo_seleccionado.get("dias_repetir", [])))

    # Pedir al usuario que seleccione qué desea editar
    while True:
        opcion = input("\nSeleccione qué desea editar (nombre/estado/horario/días): ")
        if opcion.lower() in ["nombre", "estado", "horario", "días"]:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    if opcion.lower() == "nombre":
        nuevo_nombre = input("Ingrese el nuevo nombre del dispositivo (deje en blanco para mantener el mismo nombre): ")
        if nuevo_nombre:
            dispositivo_seleccionado["nombre"] = nuevo_nombre
    elif opcion.lower() == "estado":
        nuevo_estado = input("Ingrese el nuevo estado del dispositivo (encendido/apagado) (deje en blanco para mantener el mismo estado): ")
        if nuevo_estado:
            dispositivo_seleccionado["estado"] = nuevo_estado.lower()
    elif opcion.lower() == "horario":
        # Verificar el formato de horario de encendido
        while True:
            nuevo_horario_encendido = input("Ingrese el nuevo horario de encendido (formato 24 horas - HH:MM) (deje en blanco para mantener el mismo horario): ")
            if nuevo_horario_encendido:
                try:
                    horario_encendido = datetime.strptime(nuevo_horario_encendido, "%H:%M")
                    dispositivo_seleccionado["hora_encendido"] = horario_encendido.strftime("%H:%M")
                    break
                except ValueError:
                    print("Error: Formato de hora incorrecto. Utilice el formato HH:MM.")
            else:
                break

        # Verificar el formato de horario de apagado
        while True:
            nuevo_horario_apagado = input("Ingrese el nuevo horario de apagado (formato 24 horas - HH:MM) (deje en blanco para mantener el mismo horario): ")
            if nuevo_horario_apagado:
                try:
                    horario_apagado = datetime.strptime(nuevo_horario_apagado, "%H:%M")
                    dispositivo_seleccionado["hora_apagado"] = horario_apagado.strftime("%H:%M")
                    break
                except ValueError:
                    print("Error: Formato de hora incorrecto. Utilice el formato HH:MM.")
            else:
                break

        # Verificar los días válidos
        dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]
        while True:
            nuevos_dias = input("Ingrese los nuevos días en que se repetirá el horario (lunes a domingo, separados por comas) (deje en blanco para mantener los mismos días): ")
            if nuevos_dias:
                nuevos_dias = [dia.strip() for dia in nuevos_dias.split(",")]
                if all(dia.lower() in dias_validos for dia in nuevos_dias):
                    nuevos_dias = sorted(nuevos_dias, key=lambda dia: dias_validos.index(dia.lower()))
                    dispositivo_seleccionado["dias_repetir"] = nuevos_dias
                    break
                else:
                    print("Error: Ingrese días válidos (lunes a domingo).")
            else:
                break

    # Guardar los nuevos valores en el archivo "dispositivos.txt"
    ruta_archivo = os.path.join("Dispositivos", "dispositivos.txt")
    with open(ruta_archivo, "w") as archivo:
        for dispositivo in dispositivos:
            archivo.write(f"\n{propiedad} - {habitacion}\n")
            archivo.write(f"Nombre del dispositivo: {dispositivo.get('nombre', '')}\n")
            archivo.write(f"Estado: {dispositivo.get('estado', '')}\n")
            archivo.write(f"Hora de encendido: {dispositivo.get('hora_encendido', '')}\n")
            archivo.write(f"Hora de apagado: {dispositivo.get('hora_apagado', '')}\n")
            dias_repetir = dispositivo.get('dias_repetir')
            if dias_repetir:
                archivo.write(f"Días en que se repetirá el horario: {', '.join(dias_repetir)}\n")
            else:
                archivo.write("Días en que se repetirá el horario: None\n")
            archivo.write("\n")

    print("\nLos cambios han sido guardados exitosamente.")

def eliminar_dispositivo(nombre_propiedad, nombre_habitacion):
    ruta_archivo = os.path.join("Dispositivos", "dispositivos.txt")
    dispositivos_encontrados = []
    dispositivos_actualizados = []

    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()
        for i in range(len(lineas)):
            linea = lineas[i]
            if f"{nombre_propiedad} - {nombre_habitacion}" in linea:
                dispositivos_encontrados.append(i)

    if dispositivos_encontrados:
        print("Dispositivos disponibles en la propiedad y habitación:")
        for i in range(len(dispositivos_encontrados)):
            num_dispositivo = dispositivos_encontrados[i]
            nombre_dispositivo = lineas[num_dispositivo + 1].replace("Nombre del dispositivo: ", "").strip()
            print(f"{i + 1}. {nombre_dispositivo}")
        print()

        while True:
            opcion_dispositivo = input("Ingrese el número del dispositivo que desea eliminar: ")
            if opcion_dispositivo.isdigit() and 1 <= int(opcion_dispositivo) <= len(dispositivos_encontrados):
                num_dispositivo_eliminar = dispositivos_encontrados[int(opcion_dispositivo) - 1]
                dispositivos_actualizados = lineas[:num_dispositivo_eliminar] + lineas[num_dispositivo_eliminar + 7:]
                break
            else:
                print("\n***** Seleccione una opción válida. *****\n")

        with open(ruta_archivo, "w") as archivo:
            for linea in dispositivos_actualizados:
                archivo.write(linea)

        print("El dispositivo ha sido eliminado correctamente.")

    else:
        print(f"No se encontraron dispositivos en la propiedad {nombre_propiedad} y habitación {nombre_habitacion}.")

def eliminar_dispositivos(nombre_propiedad, nombre_habitacion):    
    ruta_folder = "Propiedades"

    for archivo in os.listdir(ruta_folder):
        if archivo != "propiedades.txt" and archivo == f"{nombre_propiedad}.txt":
            ruta_archivo = os.path.join(ruta_folder, archivo)
            dispositivos_actualizados = []
            dispositivo_actual = []
            eliminar_dispositivo = False

            with open(ruta_archivo, "r") as archivo_propiedad:
                lineas = archivo_propiedad.readlines()
                for linea in lineas:
                    if "Nombre de la habitacion: " in linea:
                        if dispositivo_actual and not eliminar_dispositivo:
                            dispositivos_actualizados.extend(dispositivo_actual)
                        dispositivo_actual = []
                        if nombre_habitacion in linea:
                            eliminar_dispositivo = True
                        else:
                            eliminar_dispositivo = False
                    if not eliminar_dispositivo:
                        dispositivo_actual.append(linea)

                if dispositivo_actual and not eliminar_dispositivo:
                    dispositivos_actualizados.extend(dispositivo_actual)

            with open(ruta_archivo, "w") as archivo_propiedad:
                for linea in dispositivos_actualizados:
                    archivo_propiedad.write(linea)

            if eliminar_dispositivo:
                print(f"Se han eliminado los dispositivos de la habitación {nombre_habitacion} en la propiedad {nombre_propiedad}.")
            else:
                print(f"No se encontró la habitación {nombre_habitacion} en la propiedad {nombre_propiedad}.")
            return

    print(f"No se encontró la propiedad {nombre_propiedad}.")




