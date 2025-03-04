import os 

class Casa:
    def __init__(self, tamaño, internet, habitaciones,capacidad, aire_acondicionado, baños, estacionamiento ,  patio, piscina, tipo_de_piso, pisos, ubicación, valor, mensualidad, televisores):
        self.tamaño = tamaño
        self.internet = internet
        self.habitaciones = habitaciones
        self.capacidad = capacidad
        self.aire_acondicionado = aire_acondicionado
        self.baños = baños
        self.estacionamiento = estacionamiento
        self.patio = patio
        self.piscina = piscina 
        self.tipo_de_piso = tipo_de_piso
        self.pisos = pisos
        self.ubicacion = ubicación
        self.valor = valor
        self.mensualidad = mensualidad
        self.televisores =  televisores

    def atributos (self):
        print ("ATRIBUTOS DE LA CASA")
        print ("1) Tamaño:", self.tamaño, "m²")
        print ("2) Internet:",self.internet)
        print ("3) Habitaciones:", self.habitaciones)
        print ("4) Capacidad:",self.capacidad, "personas")
        print ("5) Aire acondicionado:",self.aire_acondicionado)
        print ("6) Baños:",self.baños)
        print ("7) Estacionamiento:",self.estacionamiento)
        print ("8) Patio:",self.patio)
        print ("9) Piscina:",self.piscina)
        print ("10) Tipo de piso:",self.tipo_de_piso)
        print ("11) Pisos:",self.pisos)
        print ("12) Ubicacion:",self.ubicacion)
        print ("13) Valor:",self.valor)
        print ("14) Mensualidad:",self.mensualidad, "$")
        print ("15) Televisores:",self.televisores)



while True: 
    print ("Elija la casa que desea ver sus atributos")
    print ("1) Casa de la Lagunita")
    print ("2) Casa de Altamira")
    print ("3) Ninguna")
    opcion = input ("Opcion a elegir (1 ó 2): ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            Casa_La_Lagunita = Casa(400, "Netuno 200 mbs", 4 , 8, "Si tiene", 3, "3 puestos", "Si tiene", "Si tiene", "Porcelana", 2, "La Lagunita", 300000, 300, 5)
            Casa_La_Lagunita.atributos()
            break
    
        elif opcion == 2:
            Casa_Altamira = Casa(100, "Inter 50 mbs", 2, 4, "Si tiene", 2, "2 puestos", "No tiene", "No tiene", "Ceramica Blanca", 1, "Altamira", 150000, 150, 3)
            Casa_Altamira.atributos()
            break
        else:
            print ("Ingrese una opcion valida!!!!!!")
            os.system ('cls')
    else:
        print ("Ingrese una opcion valida!!!!!!")
        os.system ('cls')


