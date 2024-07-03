import colorama
import numpy as np

colorama.init()

def main():

    print(colorama.Back.LIGHTGREEN_EX + "UCAB Elaborado por: Haisa Reyes, Paola Marturet, Gabriel Sousa, Mark D. Vivas")
    print(colorama.Back.RESET)

    def LeerArchivo():
        arch= open("colocar direccion", "rt")
        lineas = arch.readlines()
        arch.close
        return lineas
    
    def Iniciales(p):
        aux= []
        IM= []
        for i in range(0, len(p), 1):
            aux= p[i]
            IM= IM + [aux[0] + aux[2]]
        return IM
    
    def Peso(pes):
        P = []
        aux= 0
        for i in range(0, len(pes), 1):
            aux = int(pes[i])
            P = P + [aux // 1000]
        return P
    

    def Estatura(es):
        Est = []
        aux = 0
        for i in range(0, len(es), 1):
            aux= int(es[i])
            res= (aux % 1000)
            Est = Est + [res / 100]
        return Est

    
    def IMCP(es, pes):
        IMC = []
        for i in range(0, len(es), 1):
            IMC = IMC + [pes[i] // (es[i]**2)]
        return IMC
    
    def IMCmay(imc):
        may = 0
        for i in range(0, len(imc), 1):
            if (imc[i] > may):
                may = imc[i]
        print(colorama.Fore.BLUE + "El IMC mayor es:", may)

    def IMCmen(imc):
        men = imc[0]
        for i in range(0, len(imc), 1):
            if (imc[i] < men):
                men = imc[i]
        print(colorama.Fore.YELLOW + "El IMC menor es:", men)

    def IMCprom(imc):
        sum = 0
        for i in range(0, len(imc), 1):
            num = imc[i]
            sum = sum + num
        prom = (sum / len(imc))
        print(colorama.Fore.GREEN + "El Promedio de IMC es de:", prom)


    def IMCPaciente(nom, imc):
        for i in range(0, len(imc), 1):
            print(colorama.Fore.MAGENTA + "Paciente:", nom[i], "su IMC es:", imc[i])


    def IMCfinal(nom, imc):
        n = len(imc)
        for i in range(n-1, 0, -1):
            for j in range(i):
                if imc[j] > imc[j + 1]:
                    temp_imc = imc[j]
                    imc[j] = imc[j + 1]
                    imc[j + 1] = temp_imc
                    temp_nom = nom[j]
                    nom[j] = nom[j + 1]
                    nom[j + 1] = temp_nom
        
        arch = open("escribir direccion", "w")

        for i in range(n):
            arch.write(nom[i] + ": " + str(imc[i]) + "\n")
        arch.close()
        print(colorama.Fore.GREEN + "IMC ordenados guardados en Pacisal.txt")


    lineas = LeerArchivo()
    iniciales = []
    datos = []
    info = np.array([])

    info = lineas

    for i in range(0, len(info), 1):
        if ((i % 2) == 0):
            iniciales += [info[i].strip()]
        else:
            datos += [info[i].strip()]

    IM = Iniciales(iniciales)
    E = Estatura(datos)
    P = Peso(datos)
    IMC = IMCP(E, P)

    IMCPaciente(IM, IMC)
    IMCmay(IMC)
    IMCmen(IMC)
    IMCprom(IMC)
    IMCfinal(IM, IMC)

main()