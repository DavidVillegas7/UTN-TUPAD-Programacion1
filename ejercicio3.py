# Pedir y validar nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: ingrese solo letras.")
    operador = input("Nombre del operador: ")

# Variables simples para turnos de Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables simples para turnos de Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

# Menú principal del sistema
while opcion != "5":
    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Opción: ")
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida.")
    else:
        # Opción 1: Reservar turno
        if opcion == "1":
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: día no válido.")
                dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                print("Error: solo se permiten letras.")
                paciente = input("Nombre del paciente: ")
            
            # Reservar en Lunes
            if dia == "1":
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: el paciente ya tiene un turno asignado este día.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes (Turno 4).")
                else:
                    print("No hay cupos disponibles para el Lunes.")
            
            # Reservar en Martes
            elif dia == "2":
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: el paciente ya tiene un turno asignado este día.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes (Turno 3).")
                else:
                    print("No hay cupos disponibles para el Martes.")

        # Opción 2: Cancelar turno
        elif opcion == "2":
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: día no válido.")
                dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
            paciente = input("Nombre del paciente a cancelar: ")
            while not paciente.isalpha():
                print("Error: solo se permiten letras.")
                paciente = input("Nombre del paciente a cancelar: ")
            
            encontrado = False
            if dia == "1":
                if lunes1 == paciente:
                    lunes1 = ""
                    encontrado = True
                elif lunes2 == paciente:
                    lunes2 = ""
                    encontrado = True
                elif lunes3 == paciente:
                    lunes3 = ""
                    encontrado = True
                elif lunes4 == paciente:
                    lunes4 = ""
                    encontrado = True
            elif dia == "2":
                if martes1 == paciente:
                    martes1 = ""
                    encontrado = True
                elif martes2 == paciente:
                    martes2 = ""
                    encontrado = True
                elif martes3 == paciente:
                    martes3 = ""
                    encontrado = True
            
            if encontrado:
                print("Turno cancelado exitosamente.")
            else:
                print("No se encontró al paciente en el día seleccionado.")

        # Opción 3: Ver agenda del día
        elif opcion == "3":
            dia = input("Elegir día a ver (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: día no válido.")
                dia = input("Elegir día a ver (1=Lunes, 2=Martes): ")
            
            if dia == "1":
                print("--- Agenda Lunes ---")
                print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
                print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
                print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
                print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
            elif dia == "2":
                print("--- Agenda Martes ---")
                print("Turno 1:", martes1 if martes1 != "" else "(libre)")
                print("Turno 2:", martes2 if martes2 != "" else "(libre)")
                print("Turno 3:", martes3 if martes3 != "" else "(libre)")

        # Opción 4: Ver resumen general
        elif opcion == "4":
            ocu_lun = (1 if lunes1 != "" else 0) + (1 if lunes2 != "" else 0) + (1 if lunes3 != "" else 0) + (1 if lunes4 != "" else 0)
            disp_lun = 4 - ocu_lun
            
            ocu_mar = (1 if martes1 != "" else 0) + (1 if martes2 != "" else 0) + (1 if martes3 != "" else 0)
            disp_mar = 3 - ocu_mar
            
            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes: {ocu_lun} ocupados, {disp_lun} disponibles.")
            print(f"Martes: {ocu_mar} ocupados, {disp_mar} disponibles.")
            
            if ocu_lun > ocu_mar:
                print("Día con más turnos ocupados: Lunes")
            elif ocu_mar > ocu_lun:
                print("Día con más turnos ocupados: Martes")
            else:
                print("Ambos días tienen la misma cantidad de turnos ocupados (Empate).")

# Fin del sistema
print("Sistema cerrado.")