# Pedir y validar nombre del cliente
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: ingrese un nombre válido (solo letras).")
    nombre = input("Cliente: ")

# Pedir y validar cantidad de productos
cant_prod_input = input("Cantidad de productos: ")
while not cant_prod_input.isdigit() or int(cant_prod_input) <= 0:
    print("Error: ingrese un número entero positivo mayor a 0.")
    cant_prod_input = input("Cantidad de productos: ")

cant_productos = int(cant_prod_input)

total_sin_desc = 0.0
total_con_desc = 0.0

# Procesar cada producto ingresado
for i in range(1, cant_productos + 1):
    print(f"\nProducto {i}")
    
    # Validar precio del producto
    precio_input = input("Precio: ")
    while not precio_input.isdigit() or int(precio_input) <= 0:
        print("Error: ingrese un precio válido.")
        precio_input = input("Precio: ")
    
    precio = int(precio_input)
    total_sin_desc += precio
    
    # Validar si tiene descuento
    tiene_desc = input("Descuento (S/N): ").lower()
    while tiene_desc != "s" and tiene_desc != "n":
        print("Error: ingrese 's' o 'n'.")
        tiene_desc = input("Descuento (S/N): ").lower()
    
    # Calcular precio final con o sin descuento
    if tiene_desc == "s":
        precio_final = precio * 0.90
    else:
        precio_final = float(precio)
        
    total_con_desc += precio_final

# Calcular variables globales finales
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cant_productos

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Total sin descuentos: ${total_sin_desc:.2f}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")