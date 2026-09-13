# Paso 1: Configuración del personaje (validar nombre con isalpha)
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Paso 2: Inicialización de estadísticas (tipos de datos int, float, bool)
hp_jugador = 100
hp_enemigo = 100
pociones = 3
ataque_pesado_base = 15
dano_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: Ciclo de combate
while hp_jugador > 0 and hp_enemigo > 0:
    print(f"\n{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    # Validar opción del menú (debe ser dígito entre 1 y 3)
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
        
    opcion_num = int(opcion)
    
    # Acción 1: Ataque Pesado
    if opcion_num == 1:
        if hp_enemigo < 20:
            dano_final = float(ataque_pesado_base * 1.5)  # Golpe crítico (float)
            print(f"¡Golpe Crítico! Atacaste al enemigo por {dano_final} puntos de daño.")
        else:
            dano_final = float(ataque_pesado_base)
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
            
        hp_enemigo -= int(dano_final)

    # Acción 2: Ráfaga Veloz (uso obligatorio de for)
    elif opcion_num == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            hp_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Acción 3: Curar
    elif opcion_num == 3:
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print(f"Te has curado. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    # Turno del Enemigo (ataca si sigue con vida)
    if hp_enemigo > 0:
        hp_jugador -= dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")

# Paso 4: Fin del Juego
print("\n=== FIN DEL COMBATE ===")
if hp_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")