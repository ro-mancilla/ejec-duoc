CarPorcelana = 250000
ImpDentales = 475000
OrtBrackets = 800000
contCarPorcelana = 0
contImpDentales = 0
contOrtBrackets = 0
porcDesc = 0
subtotal = 0

while True:
    try:
        while True:
            opcion = int(input(f"""
            Bienvenido a clínica dental 'El Diente de Oro'
            ----------------------------------------------
            1) Cotizar (Total: ${subtotal}) (Descuento: {porcDesc}%)
            2) Renunciar
            3) Finalizar

            Ingrese una opción: """))
            while True:
                if opcion == 1:
                    cotizacion = int(input(f"""
                    Tratamientos disponibles:
                    -------------------------
                    1) Carillas Porcelana ($250000)
                    2) Implantes Dentales ($475000)
                    3) Ortodoncia Brackets ($800000)
                    4) Finalizar cotización...

                    Todos nuestros tratamientos incluyen:
                    - Limpieza y destartraje
                    - Aplicación de sellante
                    - Aplicación de fluor

                    Ingrese una opción: """))
                    if cotizacion == 1:
                        subtotal = subtotal + CarPorcelana
                        contCarPorcelana =+ 1
                        print(f"""
                        1 Carilla Porcelana agregado a la cotización (Total: ${subtotal})
                        """)
                    elif cotizacion == 2:
                        subtotal = subtotal + ImpDentales
                        contImpDentales = contImpDentales + 1
                        print(f"""
                        1 Implante Dental agregado a la cotización (Total: ${subtotal})
                        """)
                    elif cotizacion == 3:
                        subtotal = subtotal + OrtBrackets
                        contOrtBrackets = contOrtBrackets + 1
                        print(f"""
                        1 Ortodoncia Brackets agregado a la cotización (Total: ${subtotal})
                        """)
                    elif cotizacion == 4:
                        while True:
                            try:
                                trabajador = int(input("""
                                ¿Es usted trabajador de Duoc?
                                ---------------------
                                1) Auxiliar
                                2) Administrativo
                                3) Docente
                                4) Otro
                                Ingrese una opción: """))
                                if trabajador == 1:
                                    desc = 0.15
                                    porcDesc = int(desc * 100)
                                    print(f"""
                                    Como Trabajador Auxiliar, se le aplicó un {porcDesc}% de descuento.
                                    """)
                                    break
                                if trabajador == 2:
                                    desc = 0.10
                                    porcDesc = int(desc * 100)
                                    print(f"""
                                    Como Trabajador Administrativo, se le aplicó un {porcDesc}% de descuento.
                                    """)
                                    break
                                if trabajador == 3:
                                    desc = 0.05
                                    porcDesc = int(desc * 100)
                                    print(f"""
                                    Como Trabajador Docente, se le aplicó un {porcDesc}% de descuento.
                                    """)
                                    break
                                if trabajador == 4:
                                    desc = 1
                                    porcDesc = int(desc * 100)
                                    print(f"""
                                    No se aplicó ningún descuento.
                                    """)
                                    break
                                else:
                                    print("""
                                    ERROR: Entrada no válida.
                                    """)
                            except ValueError:
                                print("""
                                ERROR: Entrada no válida.
                                """)

                        restDesc = int(subtotal * desc)
                        total = int(subtotal - restDesc)
                        cuotas = int(total / 12)
                        print(f"""
                        -----------------------------------------------------------
                                                Cotización
                        -----------------------------------------------------------
                        """)
                        if contCarPorcelana >= 1:
                            print(f"""
                            {contCarPorcelana} tratamiento(s) Carillas Porcelana     ${CarPorcelana * contCarPorcelana}
                            """)
                        if contImpDentales >= 1:
                            print(f"""
                            {contImpDentales} tratamiento(s) Implantes Dentales     ${ImpDentales * contImpDentales}
                            """)
                        if contOrtBrackets >= 1:
                            print(f"""
                            {contOrtBrackets} tratamiento(s) Ortodoncia Brackets     ${OrtBrackets * contOrtBrackets}
                            """)
                        print(f"""
                        -----------------------------------------------------------
                        Subtotal             ${subtotal}
                        Descuento {porcDesc}%        ${restDesc}
                        -----------------------------------------------------------
                        Total               ${total}
                        -----------------------------------------------------------
                        Son 12 cuotas de: ${cuotas}
                        """)
                        print("                        Sonría Bonito!!!")
                        break
                    else:
                        print("""
                        ERROR: Valor no válido, ingrese un número de la lista...
                        """)
                if opcion == 2:
                    subtotal = 0
                    porcDesc = 0
                    desc = 0
                    print("""
                    Renunció. Vuelva a cotizar nuevamente sus tratamientos.
                    """)
                    break
                if opcion == 3:
                    print("""
                    Hasta luego.
                    """)
                    exit()
    except ValueError:
        print("ERROR: Valor no válido.")
