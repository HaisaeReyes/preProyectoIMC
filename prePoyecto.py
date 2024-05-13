import colorama

colorama.init()

def main():

    print(colorama.Style.BRIGHT + colorama.Fore.WHITE + colorama.Back.LIGHTGREEN_EX)
    print("UCAB Elaborado por: Haisa Reyes, Paola Marturet, Gabriel Sousa, Mark D. Vivas")
    print(colorama.Back.RESET + colorama.Fore.RESET)

    print("Ingrese las iniciales del primer paciente sin espacios en blanco en 4 letras: ")
    I1 = input()
    print("Ingrese los datos de 5 digitos del paciente 1: ")
    D1 = int(input()) 

    print("Ingrese las iniciales del segundo paciente sin espacios en blanco en 4 letras: ")
    I2 = input()
    print("Ingrese los datos de 5 digitos del paciente 2: ")
    D2 = int(input()) 
    
    print("Ingrese las iniciales del tercer paciente sin espacios en blanco en 4 letras: ")
    I3 = input()
    print("Ingrese los datos de 5 digitos del paciente 3: ")
    D3 = int(input()) 


main()
