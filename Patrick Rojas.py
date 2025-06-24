compras = {}

def comprar_entrada():

  nombre = input("Ingrese el nombre del comprador: ")
  if nombre in compras:
    print("Error: este comprador ya existe.")
    return

  tipo = input("Ingrese tipo de entrada (G para General / V para VIP): ").upper()
  if tipo not in ["G", "V"]:
    print("Tipo de entrada no válido.")
    return

  codigo = input("Ingrese el código de confirmación: ")
  if len(codigo) < 6 or not any(c.isdigit() for c in codigo) or not any(c.isalpha() for c in codigo) or " " in codigo:
    print("Código inválido. Debe tener mínimo 6 caracteres, al menos una letra, un número y sin espacios.")
    return



  compras[nombre] = {"tipo": tipo, "codigo": codigo}
  print("¡Entrada registrada exitosamente!")

def consultar_comprador():
  nombre = input("Ingrese el nombre del comprador a consultar: ")
  if nombre in compras:
    print(f"Tipo de entrada: {compras[nombre]['tipo']}")
    print(f"Código de confirmación: {compras[nombre]['codigo']}")
  else:
    print("El comprador no se encuentra.")

def menu():
  while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Comprar entrada")
    print("2. Consultar comprador")
    print("3. Cancelar compra")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")



    if opcion == "1":

      comprar_entrada()
    elif opcion == "2":

      cancelar_compra()
    elif opcion == "4":

      print("Programa terminado.")

      break
    else:

      print("¡Debe ingresar una opción válida!")



menu()