print("Registro de jugadores para el campeonato de Padel.")
regacum = []
regnombre = []
regrut = []
reganio = []
regcat = []
regfono = []
regidparejas = []
regcorreo = []

def opcion1():
    print("Grabar...")
    try:
        while True:
            nombrejug = input("Ingrese el nombre del jugador: ")
            if len(nombrejug) >= 2:
                regnombre.append(nombrejug)
                print("¡Nombre registrado!")
                break
            else:
                print("Nombre no cumple con los requisitos...")
        while True:
            rutjug = input("Ingrese el rut del jugador (Sin guión ni puntos): ")
            if len(rutjug) < 9:
                print("RUT no cumple con los requisitos...")
            else:
                regrut.append(rutjug)
                print("¡RUT registrado!")
                break
        while True:
            aniofechajug = int(input("Ingrese el año de la fecha de nacimiento del jugador: "))
            if 2023 - aniofechajug <= 81:
                reganio.append(aniofechajug)
                print("¡Año de nacimiento registrado!")
                break
            else:
                print("Usted no puede tener más de 80 años...")
        while True:
            catjug = input("Ingrese la categoría del jugador (Oro - Plata - Bronce): ").upper()
            if catjug == "ORO" or catjug == "PLATA" or catjug == "BRONCE":
                regcat.append(catjug)
                print("¡Categoría registrada!")
                break
            else:
                print("Ingrese una categoría válida...")
        while True:
            fonojug = input("Ingrese su número de teléfono: ")
            if len(fonojug) == 9:
                regfono.append(fonojug)
                print("¡Teléfono registrado!")
                break
            else:
                print("Teléfono no válido...")
        while True:
            idparejas = input("Ingrese el nombre de pareja: ")
            if len(idparejas) > 0:
                regidparejas.append(idparejas)
                print("¡Nombre de pareja registrado!")
                break
            else:
                print("No ingrese un nombre del equipo vacío...")
        while True:
            correojug = input("Ingrese su correo electrónico: ")
            if len(correojug) >= 6:
                regcorreo.append(correojug)
                print("¡Correo registrado!")
                break
            else:
                print("Correo no cumple con los requisitos...")
        print("¡Registro completado!")
    except ValueError:
        print("Ingreso no válido...")
def opcion2():
    try:
        print("Buscar...")
        busqrut = input("Ingrese el RUT del participante a buscar: ")
        if busqrut == regrut[0]:
            print(f"Nombre: {regnombre[0]}")
            print(f"Categoría: {regcat[0]}")
            print(f"Teléfono: {regfono[0]}")
            print(f"Correo: {regcorreo[0]}")
        else:
            print("RUT no coincide en ninguna pareja...")
    except ValueError or IndexError:
        print("RUT no coincide en ninguna pareja...")
def opcion3():
    print("Imprimir parejas...")
    try:
        busqparejas = input("Ingrese el nombre de pareja: ").lower
        if busqparejas == regidparejas[0]:
            print(f"Participantes del equipo: {regnombre[0]}")
    except ValueError or IndexError:
        print("Nombre de pareja no existe...")
def opcion4():
    print("Adiós, ¡buen juego!\nRodrigo Mancilla")
    exit()

while True:
    try:
        print("""
1- Grabar
2- Buscar
3- Imprimir parejas
4- Salir
       """)
        opcion = int(input("Seleccione opción: "))
        if opcion == 1:
            opcion1()
        if opcion == 2:
            opcion2()
        if opcion == 3:
            opcion3()
        if opcion == 4:
            opcion4() 
        elif opcion > 4 or opcion < 1:
            print("Opción no válida...")
    except ValueError:
        print("Opción no válida...")
