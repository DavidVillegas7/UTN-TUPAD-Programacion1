# Definición de credenciales iniciales
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False

# Control de intentos de login
while intentos < 3 and not acceso_concedido:
    intentos += 1
    print(f"Intento {intentos}/3")
    usr = input("Usuario: ")
    clv = input("Clave: ")
    
    if usr == usuario_correcto and clv == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.\n")
    else:
        print("Error: credenciales inválidas.\n")

# Si se superó el límite de intentos sin éxito
if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    # Menú repetitivo del campus
    opcion = ""
    while opcion != "4":
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        
        # Validación de opción ingresada
        if not opcion.isdigit():
            print("Error: ingrese un número válido.\n")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.\n")
        else:
            # Procesamiento de las opciones
            if opcion == "1":
                print("Estado: Inscripto\n")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.\n")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave actualizada correctamente.\n")
                    else:
                        print("Error: las claves no coinciden.\n")
            elif opcion == "3":
                print("Mensaje: El éxito es la suma de pequeños esfuerzos repetidos día tras día.\n")
            elif opcion == "4":
                print("Sesión finalizada.")