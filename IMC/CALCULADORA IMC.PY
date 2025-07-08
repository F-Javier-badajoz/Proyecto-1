def nombre():
    #Solicita al usuario que ingrese su Nombre que no este vacio y que contenga letras
    while True:
        input_string = input("Ingresa tu Nombre: \n ")
        if not input_string:
            print("Error: Nombre no puede estar vacía.\n")
        elif input_string.isalpha():
            return input_string
        else:
            print("Error: El Nombre solo debe contener letras.")

def apellidos():

    #Solicita al usuario que ingrese sus Apelldidos que no este vacio y que contenga letras
    while True:
        input_string = input("Ingresa tus Apellidos: \n ")
        if not input_string:
            print("Error: Apellidos no puede estar vacía.\n")
        elif input_string.isalpha():
            return input_string
        else:
            print("Error: Los Apellidos solo debe contener letras.")


def estatura():
    #Solicitar al usaurio que ingrese su Estatura y que contenga numeros
    while True:
        entrada = input("Por favor ingresa tu Estatura en metros: \n")
        if entrada.strip() == "":
            print("Error: Por favor ingresa tu Estatura en metros: \n")
        else:
            try:
                numero = float(entrada)
                return numero
            except ValueError:
                print("Error: Por favor, ingreda una esatura valida: \n")

def edad():
  #Solicita al usuario que ingrese Edad que no este vacio y que contenga numeros
  while True:
    entrada = input("Por favor, ingresa tu Edad: \n ")
    try:
      numero = int(entrada)
      return numero  # Regresa el entero
    except ValueError:
      print("Error. Por favor, ingresa tu Edad: \n")

def estatura():
    #Solicitar al usaurio que ingrese su Estatura y que contenga numeros
    while True:
        entrada = input("Por favor ingresa tu Estatura en metros: \n")
        if entrada.strip() == "":
            print("Error: Por favor ingresa tu Estatura en metros: \n")
        else:
            try:
                numero = float(entrada)
                return numero
            except ValueError:
                print("Error: Por favor, ingreda una esatura valida: \n")

def peso():
    #Solicitar al usaurio que ingrese su Peso y que contenga numeros
    while True:
        entrada = input("Por favor ingresa tu Peso en Kilogramos: \n")
        if entrada.strip() == "":
            print("Error: Por favor ingresa tu Peso en Kilogramos: \n")
        else:
            try:
                numero = float(entrada)
                return numero
            except ValueError:
                print("Error: Por favor, ingreda tu Peso en Kilogramos: \n")

Nombre = nombre()
Apellido = apellidos()
Edad = edad()
Estatura = estatura()
Peso = peso()

IMC = Peso / (Estatura**2)

print(Nombre + " " + Apellido + "\n TU IMC es de: " + str(IMC) )

if IMC <= 18.5 :
    print ("Tienens Bajo Peso")

elif IMC >= 18.5 and IMC <= 24.9 :
    print ("Tienes peso Normal")

elif IMC >= 24.9 and IMC <= 29.9 :
    print ("Tienes SobrePeso")

elif IMC >= 30 :
    print ("Tienes Obesidad")