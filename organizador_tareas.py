import json
tareas_json = "tareas.json"
estados_json = "estados.json"


class Tareas:
    def __init__ (self, contenido, estado_a_completar):
        self.contenido = contenido
        self.estado_a_completar = estado_a_completar

    def mostrar_informacion(self):
        if self.estado_a_completar:
            return(f": {self.contenido} -- Completada")
        else:
            return(f": {self.contenido} -- Pendiente")

class Organizador_de_tareas:
    def __init__(self):
       self.almacenamiento_de_tareas = []

    def listar_tareas(self):
        if not self.almacenamiento_de_tareas:
            print("Todavía no se ha creado ninguna tarea.\n")
        else:
            print("----- Lista de tareas -----\n")
            print("----- No completadas -----\n")
            tareas_no_completadas = list(filter(lambda x: x.estado_a_completar == False, self.almacenamiento_de_tareas))
            for tarea_actual in tareas_no_completadas:
                print(f"{self.almacenamiento_de_tareas.index(tarea_actual)+1}{tarea_actual.mostrar_informacion()}")
            tareas_completadas = list(filter(lambda x: x.estado_a_completar == True, self.almacenamiento_de_tareas))
            print("\n------ Completadas -------\n")
            for tarea_actual in tareas_completadas:
                print(f"{self.almacenamiento_de_tareas.index(tarea_actual)+1}{tarea_actual.mostrar_informacion()}")
            print("")


    def añadir_tarea(self):
        estado_a_completar = False
        contenido = input("Ingrese la tarea a añadir: \n")

        nueva_tarea = Tareas(contenido, estado_a_completar)
        self.almacenamiento_de_tareas.append(nueva_tarea)

        print(f"La tarea se ha añadido.\n")
    
    def eliminar_tarea(self):
        while True:
            if not self.almacenamiento_de_tareas: 
                print("No hay tareas guardadas.")
                break
            else:
                try:
                    tarea_a_borrar = int(input("Ingrese el identificador (posición) de la tarea a borrar: "))-1
                except ValueError:
                    print("Ingrese una posición válida (un número).\n")
                if tarea_a_borrar >= len(self.almacenamiento_de_tareas):
                    print("No existe una tarea en esa posición, vuelva a intentarlo.\n")
                else:
                    self.almacenamiento_de_tareas.pop(tarea_a_borrar)
                    print("La tarea ha sido borrada con éxito.\n")
                    break

    def modificar_tarea(self): #Falta editarlo
        while True:
            if not self.almacenamiento_de_tareas: 
                print("No hay tareas guardadas.") 
                break
            else:
                try:
                    tarea_a_modificar = int(input("Ingrese el identificador (posición) de la tarea a modificar: "))-1
                except ValueError:
                    print("Ingrese una posición válida (un número).\n")
                if tarea_a_modificar >= len(self.almacenamiento_de_tareas):
                    print("No existe una tarea en esa posición, vuelva a intentarlo.\n")
                else:
                    nuevo_mensaje = input("Ingrese el nuevo contenido de la tarea:\n")
                    nueva_tarea = Tareas(nuevo_mensaje, False)
                    self.almacenamiento_de_tareas[tarea_a_modificar] = nueva_tarea
                    print("La tarea ha sido modificada.\n")
                    break

    def marcar_como_completada(self):
        while True:
            if not self.almacenamiento_de_tareas:
                print("No hay tareas guardadas.")
                break
            else:
                try:
                    tarea_a_modificar = int(input("Ingrese el identificador (posición) de la tarea que desea marcar como completada, o no completada: \n"))-1
                except ValueError:
                    print("Ingrese una posición válida (un número).\n")
                if tarea_a_modificar >= len(self.almacenamiento_de_tareas):
                    print("No existe una tarea en la posición marcada, por favor inténtelo de nuevo.\n")
                else:
                    if(self.almacenamiento_de_tareas[tarea_a_modificar].estado_a_completar):
                        self.almacenamiento_de_tareas[tarea_a_modificar].estado_a_completar = False
                        print("Tarea marcada como no completada.\n")
                        break
                    else:
                        self.almacenamiento_de_tareas[tarea_a_modificar].estado_a_completar = True
                        print("Tarea marcada como completada.\n")
                        break
    
    def cargar_tareas(self):
        try:
            print("Cargando archivo...\n")
            with open(tareas_json, "r", encoding="utf-8") as f:
                lista_contenidos = json.load(f)
            
            with open(estados_json, encoding="utf-8") as f:
                lista_estados = json.load(f)

            contador = 0
            while contador < len(lista_contenidos):
                tarea_actual = Tareas(lista_contenidos[contador],lista_estados[contador])
                self.almacenamiento_de_tareas.append(tarea_actual)
                contador += 1
            print("Archivo cargado.\n")
        except ValueError:
            print("Empezando nuevo archivo...\n")



    def guardar_tareas(self):
        print("Guardando archivo...\n")
        lista_contenidos = list(map(lambda x: x.contenido, self.almacenamiento_de_tareas))
        lista_estados = list(map(lambda x: x.estado_a_completar, self.almacenamiento_de_tareas))
        with open("tareas.json", "w") as f:
            json.dump(lista_contenidos, f)
        
        with open("estados.json", "w") as f:
            json.dump(lista_estados, f)
        print("Archivo guardado.\n")

def menu():
    organizador = Organizador_de_tareas()
    organizador.cargar_tareas()
    while True:
        print("-------- Organizador de Tareas --------\n")
        print("Opciones: -----------------------------\n")
        print("1. Lista de tareas.--------------------")
        print("2. Añadir una tarea.-------------------")
        print("3. Eliminar una tarea.-----------------")
        print("4. Modificar una tarea.----------------")
        print("5. Marcar tarea como completada.-------")
        print("6. Salir.------------------------------\n")
        try:
            choice = int(input("Ingrese la acción a realizar :\n"))
            print("")
            if choice == 1:
                organizador.listar_tareas()
            elif choice == 2:
                organizador.añadir_tarea()
            elif choice == 3:
                if organizador.almacenamiento_de_tareas:
                    organizador.listar_tareas()
                organizador.eliminar_tarea()
            elif choice == 4:
                if organizador.almacenamiento_de_tareas:
                    organizador.listar_tareas()
                organizador.modificar_tarea()
            elif choice == 5: 
                if organizador.almacenamiento_de_tareas:
                    organizador.listar_tareas()
                organizador.marcar_como_completada()
            elif choice == 6:
                organizador.guardar_tareas()
                print("Saliendo del programa...")
                break
            else:
                print("El valor ingresado no es una opción.\n")
        except ValueError:
            print("Ingrese un valor válido (Del 1 al 6.)\n")

menu()