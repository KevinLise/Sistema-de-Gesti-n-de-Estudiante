import json
import os
sistema = "estudiante.json"


def cargar_datos():
    if os.path.exists(sistema):
        with open(sistema, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return {int(k): v for k, v in datos.items()}
    return {
        1: {"ID": 100327560, "nombre": "juan",   "edad": "21","course":"soporte tecnico computacion","status": "activo"  },
        2: {"ID": 100326570, "nombre": "carlos", "edad": "36","course": "panaderia","status":"inactivo"},
        3: {"ID": 100326590, "nombre": "jose",  "edad": "45","course": "cocina","status":"activo"},
    }

def guardar_datos():
    with open(sistema, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in estudiante.items()}, f, indent=8, ensure_ascii=False)
    print(f"(Guardado en '{sistema}')")

# Cargar datos al iniciar el programa
estudiante = cargar_datos()

def mostras_estudiante():
    if len(estudiante) == 0:
        print("No hay registro:")
        return
    print("\n Lista de estudiantes ")
    for llave, datos in estudiante.items():
        print(f"\nStudent {llave}:")
        print(f"  ID     : {datos['ID']}")
        print(f"  Nombre : {datos['Nombre']}")
        print(f"  Edad   : {datos['Edad']}")
        print(f"  Course     : {datos['Course']}")
        print(f"  Status     : {datos['Status']}")
    print()
    
       

def agregar_estudiante():
    nueva_llave = max(estudiante.keys(), default=0) + 1
    print(f"\nNuevo Estudiante {nueva_llave}")
    nuevo_id   = input("ID      : ").strip()
    nuevo_nom  = input("Nombre  : ").strip()
    nueva_edad = input("Edad    : ").strip()
    nuevo_cour = input("course  : ").strip()
    nuevo_stat = input("status   :").strip()


    estudiante[nueva_llave] = {
        "ID":     nuevo_id,
        "nombre": nuevo_nom,
        "Edad":   nueva_edad,
        "course": nuevo_cour,
        "status": nuevo_stat
    }
    guardar_datos()
    print(f"Estudiante '{nuevo_nom}' agregado con la  {nueva_llave}.")
    

def eliminar_estudiante():
    mostras_estudiante()

    if len(estudiante) == 0:

        return
    try:
        llave = int(input("\nNumero de ID  eliminar: "))
        if llave in estudiante:
            nombret = estudiante[llave]["nombre"]
            confirmar = input(f"¿Seguro que deseas eliminar '{nombret}'? (s/n): ").strip().lower()
            if confirmar == "s":
                del estudiante[llave]
                guardar_datos()
                print(f"estudiante '{nombret}' eliminado.")
            else:
                print("Eliminacion cancelada.")
        else:
            print("estudiante no encontrado.")
    except ValueError:
        print("Ingresa un numero valido.")
   

def buscar_id():
    try:
        busqueda_id = int(input("Ingrese el ID que va buscar:"))
        encontrado= None
        for llave, datos in estudiante.items():
            if datos["ID"] == busqueda_id:
                encontrado = datos
                break
        if encontrado:
            print(f"Estudiante Encontrado: {encontrado}")
        else:
            print("no se encontrado el estudiante con ID o Nombre")
    except ValueError:
        print("Ingresa un numero valido.")
  

def actulizar_datos():
    mostras_estudiante()
    if len(estudiante) == 0:
        return
    try:
        llave = int(input("Que quiere actulizar: "))
        if llave not in estudiante:
            print("estudiante no encontrado")
            return
    except ValueError:
        print("Ingresa un numero invalido ")
        return
    datos = estudiante[llave]
    print(f"\nActualizando: {datos['Nombre']} (Enter para conservar valor actual)")

dats=False

while not dats:
        
   
    print("\n═════════════════════")
    print("  MENU DE CONSULTAS  ")
    print("═══════════════════════")
    print("1. Mostra todos")
    print("2. Agregar Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Bucar por ID")
    print("5. Actulizar Informacion")
    print("6. Salir")
    opcion = input("\nElige una opcion: ").strip()

    if opcion == "1":
        mostras_estudiante()
    elif opcion == "2":
        agregar_estudiante()
    elif opcion == "3":
        eliminar_estudiante()
    elif opcion == "4":
        buscar_id()
    elif opcion == "5":
        actulizar_datos()
    elif opcion == "6":
        print("salir...")
        dats=True
    else:
        print("Opcion invalidad , intente de nuevo. ")


