# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:47:21 2024

@author: marcelo
"""
import os
import random
import sqlite3



directorio = "C:\\Users\\marce\\OneDrive\\Escritorio\\asignaturas\\ejercicios intro\\proyecto-gestion de ventas"

nombre="GestionVentas.db"

ruta=os.path.join(directorio, nombre)

con=sqlite3.connect(ruta)
cursor=con.cursor()

# cursor.execute("CREATE TABLE Ventas(DNI INT , Nombre TEXT, Monto INT)")    


información_producto = []

def verificación_importaciones(producto):
    productos_importados = ["laptop", "desktop"]
    if producto.lower() in productos_importados:
        return "Importado"
    else:
        return "No importado"

def información_del_producto():
    producto = input("Ingrese el nombre del producto a buscar: ")
    if producto.lower() == "laptop":
        inf_laptop = {"Nombre": "Laptop HP de 15 pulgadas", "Importación": verificación_importaciones(producto)}
        información_producto.append(inf_laptop)
        print(información_producto)
    elif producto.lower() == "desktop":
        inf_desktop = {"Nombre": "Desktop Dell con procesador i7", "Importación": verificación_importaciones(producto)}
        información_producto.append(inf_desktop)
        print(información_producto)
    elif producto.lower() == "impresora":
        inf_impresora = {"Nombre": "Impresora Epson de inyección de tinta", "Importación": verificación_importaciones(producto)}
        información_producto.append(inf_impresora)
        print(información_producto)
    else:
        print("Producto no disponible")

información_alm_producto = []

def generar_código_inventario():
    n = random.randint(2000, 7000)
    while n % 7 != 0:
        n = random.randint(2000, 7000)
    return n

def generar_costosfunddesktop():
    n = random.randint(150, 250)
    return n

def generar_costoslaptop():
    n = random.randint(80, 150)
    return n

def generar_costosalmacenamientoL_ing():
    n = random.randint(200, 450)
    while n % 2 != 0:
        n = random.randint(200, 450)
    return n

def generar_costosalmacenamientoD_ing():
    n = random.randint(180, 250)
    while n % 3 != 0:
        n = random.randint(180, 250)
    return n

def generar_costosalmacenamientoI_ing():
    n = random.randint(90, 155)
    while n % 2 == 0:
        n = random.randint(90, 155)
    return n

def costo_total_almL():
    a = generar_costoslaptop()
    b = generar_costosalmacenamientoL_ing()
    c = 65
    costo = a + b + c
    return costo

def costo_total_almD():
    a = generar_costosfunddesktop()
    b = generar_costosalmacenamientoD_ing()
    c = 75
    costo = a + b + c
    return costo

def costo_total_almI():
    a = 50
    b = generar_costosalmacenamientoI_ing()
    costo = a + b
    return costo

def registrar_venta():
    producto = input("Ingrese el nombre del producto a buscar: ")
    if producto.lower() == "laptop":
        a = costo_total_almL()
        venta = a + a * 0.25
        print(venta)
    elif producto.lower() == "desktop":
        a = costo_total_almD()
        venta = a + a * 0.25
        print(venta)
    elif producto.lower() == "impresora":
        a = costo_total_almI()
        venta = a + a * 0.25
        print(venta)

def información_de_almacenamiento():
    producto = input("Ingrese el nombre del producto a buscar: ")
    if producto.lower() == "laptop":
        inf_alm_laptop = {
            "Costo de almacenamiento": 65,
            "Código de Inventario": generar_código_inventario(),
            "Costo de funda de protección": generar_costoslaptop(),
            "Costo de ingredientes": generar_costosalmacenamientoL_ing(),
            "Costo total de almacenamiento": costo_total_almL()
        }
        información_alm_producto.append(inf_alm_laptop)
        print(información_alm_producto)
    elif producto.lower() == "desktop":
        inf_alm_desktop = {
            "Costo de almacenamiento": 75,
            "Código de Inventario": generar_código_inventario(),
            "Costo de funda de protección": generar_costosfunddesktop(),
            "Costo de Ingredientes": generar_costosalmacenamientoD_ing(),
            "Costo total de almacenamiento": costo_total_almD()
        }
        información_alm_producto.append(inf_alm_desktop)
        print(información_alm_producto)
    elif producto.lower() == "impresora":
        inf_alm_impresora = {
            "Costo de almacenamiento": 50,
            "Código de Inventario": generar_código_inventario(),
            "Costo de Ingredientes": generar_costosalmacenamientoI_ing(),
            "Costo total de almacenamiento": costo_total_almI()
        }
        información_alm_producto.append(inf_alm_impresora)
        print(información_alm_producto)
    else:
        print("Producto no disponible")

def realizar_compra():
    nombre = input("Ingrese su nombre: ")
    dni= int(input("ingrese su dni: "))
    compra_total = []
    venta_numero = 2000
    compra=0
    while True:
        producto = input("Ingrese el nombre del producto a comprar (0 para no continuar): ")
        if producto == "0":
            venta_numero=+1
            cursor.execute("INSERT INTO Ventas(DNI, Nombre, Monto) VALUES(?, ?,?)",(dni,nombre,compra))
            con.commit()
            break
        elif producto.lower() == "laptop":
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            compra = (costo_total_almL() + costo_total_almL() * 0.25) * cantidad
        elif producto.lower() == "desktop":
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            compra = (costo_total_almD() + costo_total_almD() * 0.25) * cantidad
        elif producto.lower() == "impresora":
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            compra = (costo_total_almI() + costo_total_almI() * 0.25) * cantidad
        else:
            print("Producto inválido. Inténtelo de nuevo")
            continue
        venta = {"Venta": venta_numero, "Producto": producto, "Cantidad": cantidad, "Compra": compra}
        compra_total.append(venta)
        venta_numero += 1
    compra_total.sort(key=lambda x: x["Venta"])
    return compra_total



def buscar_venta_binaria(ventas, target):
    left = 0
    right = len(ventas) - 1

    while left <= right:
        mid = (left + right) // 2
        venta = ventas[mid]

        if venta["Venta"] == target:
            return venta
        elif venta["Venta"] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def buscar_venta_secuencial(ventas, target):
    for venta in ventas:
        if venta["Venta"] == target:
            return venta
    return None

def quicksort(ventas, low, high):
    if low < high:
        pivot_index= partition(ventas, low, high)
        quicksort(ventas, low, pivot_index - 1)
        quicksort(ventas, pivot_index + 1, high)

def partition(ventas, low, high):
    pivot = ventas[high]["Venta"]
    i = low - 1

    for j in range(low, high):
        if ventas[j]["Venta"] < pivot:
            i += 1
            ventas[i], ventas[j] = ventas[j], ventas[i]

    ventas[i + 1], ventas[high] = ventas[high], ventas[i + 1]
    return i + 1

def modificar_cantidad_venta(ventas, numero_venta):
    left = 0
    right = len(ventas) - 1

    while left <= right:
        mid = (left + right) // 2
        venta = ventas[mid]

        if venta["Venta"] == numero_venta:
            cantidad_nueva = int(input("Ingrese la nueva cantidad: "))
            venta["Cantidad"] = cantidad_nueva
            return True
        elif venta["Venta"] < numero_venta:
            left = mid + 1
        else:
            right = mid - 1

    return False

def mostrar_venta_mayor(ventas):
    venta_mayor = None
    max_venta = 0
    
    for venta in ventas:
        if venta["Compra"] > max_venta:
            venta_mayor = venta
            max_venta = venta["Compra"]
    
    if venta_mayor is not None:
        print("Venta con el total más alto:")
        print("Número de venta:", venta_mayor["Venta"])
        print("Producto:", venta_mayor["Producto"])
        print("Cantidad:", venta_mayor["Cantidad"])
        print("Total de venta:", venta_mayor["Compra"])
    else:
        print("No se encontró ninguna venta.")



def doc_impreso(ventas):
    with open("ventas.txt", "w") as f:
        f.write("La información de las ventas es:\n")
        for venta in ventas:
            f.write(f"Número de venta: {venta['Venta']}\n")
            f.write(f"Producto: {venta['Producto']}\n")
            f.write(f"Cantidad: {venta['Cantidad']}\n")
            f.write(f"Total de venta: {venta['Compra']}\n\n")
        
        max_venta = 0
        venta_mayor = None

        for venta in ventas:
            if venta["Compra"] > max_venta:
                max_venta = venta["Compra"]
                venta_mayor = venta
        
        f.write("El total de venta con el total más alto es:\n")
        if venta_mayor is not None:
            f.write(f"Número de venta: {venta_mayor['Venta']}\n")
            f.write(f"Producto: {venta_mayor['Producto']}\n")
            f.write(f"Cantidad: {venta_mayor['Cantidad']}\n")
            f.write(f"Total de venta: {venta_mayor['Compra']}\n")
        else:
            f.write("No se encontró ninguna venta.\n")

    print("Archivo 'ventas.txt' creado exitosamente.")
       
    
def menu():
    ventas = []
    while True:
        print("SISTEMA DE INFORMACIÓN DE PRODUCTOS: LAPTOP, DESKTOP E IMPRESORA")
        print("Seleccione la opción:")
        print("[1] Información general de productos")
        print("[2] Información del almacenamiento de productos")
        print("[3] Costo de venta de productos")
        print("[4] Realizar compra")
        print("[5] Ordenar la lista por total de venta")
        print("[6] Buscar venta (Binaria)")
        print("[7] Buscar venta (Secuencial)")
        print("[8] Modificar cantidad de venta")
        print("[9] Mostrar total de venta con el total mas alto")
        print("[10] Almacenar documento impreso")
        print("[0] Salir")
        opt = int(input("Ingrese opción a realizar: "))

        if opt == 1:
            información_del_producto()
        elif opt == 2:
            información_de_almacenamiento()
        elif opt == 3:
            registrar_venta()
        elif opt == 4:
            resultado = realizar_compra()
            ventas.extend(resultado)
            print(resultado)
        elif opt == 5:
            for i in range(len(ventas)-1):
                for j in range(len(ventas)-1-i):
                    if ventas[j]["Compra"] > ventas[j+1]["Compra"]:
                        ventas[j], ventas[j+1] = ventas[j+1], ventas[j]
            print("Lista de ventas ordenada por el total de venta (método de burbuja):")
            for venta in ventas:
                print("Número de venta:", venta["Venta"])
                print("Producto:", venta["Producto"])
                print("Cantidad:", venta["Cantidad"])
                print("Total de venta:", venta["Compra"])   
        elif opt == 6:
            target = int(input("Ingrese el número de venta a buscar: "))
            quicksort(ventas, 0, len(ventas) - 1)
            result = buscar_venta_binaria(ventas, target)
            if result:
                print("Venta encontrada:", result)
            else:
                print("Venta no encontrada")
        elif opt == 7:
            target = int(input("Ingrese el número de venta a buscar: "))
            result = buscar_venta_secuencial(ventas, target)
            if result:
                print("Venta encontrada:", result)
            else:
                print("Venta no encontrada")
        elif opt == 8:
            target = int(input("Ingrese el número de venta a modificar: "))
            quicksort(ventas, 0, len(ventas) - 1)
            if modificar_cantidad_venta(ventas, target):
                print("Cantidad modificada exitosamente")
            else:
                print("Venta no encontrada")
        elif opt ==9:
            mostrar_venta_mayor(ventas)
            
        elif opt==10:
            doc_impreso(ventas)
        elif opt == 0:
            break
        else:
            print("Opción Incorrecta..")

menu()
con.close()
