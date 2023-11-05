# Evaluación Unidad II Programación Web - Francisco Mendez Y.
# Carrera de Ing. Informática - IPLACEX
def agregar_compra(compras, total_gastado):
    monto = int(input("Ingresa el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print(f"Compra agregada correctamente.")
    return total_gastado

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras realizadas:")
        for idx, monto in enumerate(compras, start=1):
            print(f"Compra {idx}: ${monto}")

def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción ingresada no valida, intenta nuevamente.")
main()# Llamamos a la funcion main() para mostrar el menu.