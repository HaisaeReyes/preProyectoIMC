import colorama

colorama.init()

def main():

    print(colorama.Style.BRIGHT + colorama.Fore.WHITE + colorama.Back.LIGHTGREEN_EX)
    print("UCAB Elaborado por: Haisa Reyes, Paola Marturet, Gabriel Sousa, Mark D. Vivas")
    print(colorama.Back.RESET + colorama.Fore.RESET)

    print("Ingrese las iniciales del primer paciente sin espacios en blanco en 4 letras: ")
    I1 = input()
    print("Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 1: ")
    D1 = int(input()) 

    print("Ingrese las iniciales del segundo paciente sin espacios en blanco en 4 letras: ")
    I2 = input()
    print("Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 2: ")
    D2 = int(input()) 
    
    print("Ingrese las iniciales del tercer paciente sin espacios en blanco en 4 letras: ")
    I3 = input()
    print("Ingrese 5 digitos, siendo los primeros 3 la estatura en cm y los 2 ultimos el peso del paciente 3: ")
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

    if (IMC1 < 18):
        PIMC1 = "Bajo peso"
    elif (IMC1 >= 18 and IMC1 < 25):
        PIMC1 = "Peso Normal"
    elif (IMC1 >= 25 and IMC1 < 30):
        PIMC1 = "Sobrepeso"
    elif (IMC1 >= 30):
        PIMC1 = "Obesidad"


    if (IMC2 < 18):
        PIMC2 = "Bajo peso"
    elif (IMC2 >= 18 and IMC2 < 25):
        PIMC2 = "Peso Normal"
    elif (IMC2 >= 25 and IMC2 < 30):
        PIMC2 = "Sobrepeso"
    elif (IMC2 >= 30):
        PIMC2 = "Obesidad"

    
    if (IMC3 < 18):
        PIMC3 = "Bajo peso"
    elif (IMC3 >= 18 and IMC3 < 25):
        PIMC3 = "Peso Normal"
    elif (IMC3 >= 25 and IMC3 < 30):
        PIMC3 = "Sobrepeso"
    elif (IMC3 >= 30):
        PIMC3 = "Obesidad"

    
    



    




    


main()
