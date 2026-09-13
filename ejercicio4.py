# Inicialización de variables requeridas
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

# Pedir y validar el nombre del agente
agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: ingrese solo letras.")
    agente = input("Nombre del agente: ")

# Bucle principal de juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- ESTADO AGENTE {agente.upper()} ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura (-20 Energía, -2 Tiempo)")
    print("2. Hackear panel (-10 Energía, -3 Tiempo)")
    print("3. Descansar (+15 Energía, -1 Tiempo)")
    
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese una opción válida (1-3).")
        opcion = input("Opción: ")
    
    # Procesamiento de Opción 1: Forzar cerradura
    if opcion == "1":
        forzar_seguidos += 1
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidos == 3:
            alarma = True
            print("¡La cerradura se trabó! Se activó la alarma.")
        else:
            if energia < 40:
                print("Riesgo de alarma. Ingrese un número (1-3):")
                num_riesgo = input("Número: ")
                while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                    print("Error: ingrese un número de 1 a 3.")
                    num_riesgo = input("Número: ")
                
                if int(num_riesgo) == 3:
                    alarma = True
                    print("¡Alarma activada por fallo!")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Forzaste y abriste 1 cerradura!")

    # Procesamiento de Opción 2: Hackear panel
    elif opcion == "2":
        forzar_seguidos = 0
        energia -= 10
        tiempo -= 3
        
        print("Hackeando panel...")
        for _ in range(4):
            codigo_parcial += "A"
            print(f"Progreso código: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! Se abrió 1 cerradura automáticamente.")

    # Procesamiento de Opción 3: Descansar
    elif opcion == "3":
        forzar_seguidos = 0
        tiempo -= 1
        
        if alarma:
            energia += 5
        else:
            energia += 15
            
        if energia > 100:
            energia = 100
        print("Descansaste y recuperaste energía.")

# Verificación de resultados
print("\n--- RESULTADO FINAL ---")
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste todas las cerraduras y lograste escapar.")
elif alarma and tiempo <= 3:
    print("DERROTA. El sistema se bloqueó debido a la alarma.")
else:
    print("DERROTA. Te quedaste sin recursos para continuar.")