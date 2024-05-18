import colorama

colorama.init()

def main():

    print(colorama.Back.LIGHTGREEN_EX + "UCAB Elaborado por: Haisa Reyes, Paola Marturet, Gabriel Sousa, Mark D. Vivas")
    print(colorama.Back.RESET)

    print(colorama.Fore.BLUE + "Ingrese las iniciales del primer paciente sin espacios en blanco con 4 letras: ")
    I1 = input()
    print(colorama.Fore.CYAN + "Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 1: ")
    D1 = int(input()) 

    print(colorama.Fore.LIGHTBLUE_EX +  "Ingrese las iniciales del segundo paciente sin espacios en blanco en 4 letras: ")
    I2 = input()
    print(colorama.Fore.LIGHTCYAN_EX + "Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 2: ")
    D2 = int(input()) 
    
    print(colorama.Fore.GREEN + "Ingrese las iniciales del tercer paciente sin espacios en blanco en 4 letras: ")
    I3 = input()
    print(colorama.Fore.LIGHTGREEN_EX + "Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 3: ")
    D3 = int(input()) 

    I1M = I1[0]+I1[2]
    I2M = I2[0]+I2[2]
    I3M = I3[0]+I3[2]

    E1 = D1 // 100
    E1 = E1 / 100
    P1 = D1 % 100

    E2 = D2 // 100
    E2 = E2 / 100
    P2 = D2 % 100

    E3 = D3 // 100
    E3 = E3 / 100
    P3 = D3 % 100

    IMC1 = (P1 // E1**2)
    IMC2 = (P2 // E2**2)
    IMC3 = (P3 // E3**2)
    

    print(colorama.Fore.BLUE + "El paciente 1 es ", I1M, ", pesa ", P1, "kg y mide ", E1, " m")
    print(colorama.Fore.CYAN + "El paciente 2 es ", I2M, ", pesa ", P2, "kg y mide ", E2, " m")
    print(colorama.Fore.GREEN + "El paciente 3 es ", I3M, ", pesa ", P3, "kg y mide ", E3, " m")


    if (IMC1 < 18):
        print(colorama.Fore.CYAN + "El promedio de IMC del paciente",I1M ,"es de bajo peso")
    elif ((IMC1 >= 18) and (IMC1 < 25)):
        print(colorama.Fore.GREEN + "El promedio de IMC del paciente",I1M ,"es de peso normal")
    elif ((IMC1 >= 25) and (IMC1 < 30)):
        print(colorama.Fore.MAGENTA + "El promedio de IMC del paciente",I1M ,"es de sobrepeso")
    elif (IMC1 >= 30):
        print(colorama.Fore.RED + "El promedio de IMC del paciente",I1M ,"es de obesidad")


    if (IMC2 < 18):
        print(colorama.Fore.CYAN + "El promedio de IMC del paciente",I2M ,"es de bajo peso")
    elif ((IMC2 >= 18) and (IMC2 < 25)):
        print(colorama.Fore.GREEN + "El promedio de IMC del paciente",I2M ,"es de peso normal")
    elif ((IMC2 >= 25) and (IMC2 < 30)):
        print(colorama.Fore.MAGENTA + "El promedio de IMC del paciente",I2M ,"es de sobrepeso")
    elif (IMC2 >= 30):
        print(colorama.Fore.RED + "El promedio de IMC del paciente",I2M ,"es de obesidad")

    
    if (IMC3 < 18):
        print(colorama.Fore.CYAN + "El promedio de IMC del paciente",I3M ,"es de bajo peso")
    elif ((IMC3 >= 18) and (IMC3 < 25)):
        print(colorama.Fore.GREEN + "El promedio de IMC del paciente",I3M ,"es de peso normal")
    elif ((IMC3 >= 25) and (IMC3 < 30)):
        print(colorama.Fore.MAGENTA + "El promedio de IMC del paciente",I3M ,"es de sobrepeso")
    elif (IMC3 >= 30):
        print(colorama.Fore.RED + "El promedio de IMC del paciente",I3M ,"es de obesidad")


    if((IMC1 > IMC2) and (IMC1 > IMC3)):
        print(colorama.Fore.MAGENTA + "El IMC mayor es: ", IMC1," del paciente ",I1M)
    elif((IMC2 > IMC1) and (IMC2 > IMC3)):
        print(colorama.Fore.LIGHTMAGENTA_EX + "El IMC mayor es: ", IMC2," del paciente ",I2M)
    elif((IMC3 > IMC1) and (IMC3 > IMC2)):
        print(colorama.Fore.RED + "El IMC mayor es: ", IMC3," del paciente ",I3M)


    if((IMC1 < IMC2) and (IMC1 < IMC3)):
        print(colorama.Fore.YELLOW + "El IMC menor es: ", IMC1," del paciente ",I1M)
    elif((IMC2 < IMC1) and (IMC2 < IMC3)):
        print(colorama.Fore.LIGHTYELLOW_EX + "El IMC menor es: ", IMC2," del paciente ",I2M)
    elif((IMC3 < IMC1) and (IMC3 < IMC2)):
        print(colorama.Fore.CYAN + "El IMC menor es: ", IMC3," del paciente ",I3M)

main()