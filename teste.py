def limite_rapido(x):
    return 1 if x > 0 else -1

def funcao_rampa(x):
    return 1 if x > 0 else 0

def sigmoid(x):
    return 1 * (-1 /(1+x)) if x >= 0 else -1 * (1 /(1-x))

def main():
    num_neurons = int(input("Digite a quantidade de neurônios: "))
    
    LR_atual = 0
    FR_atual = 0
    FS_atual = 0
    entrada1 = float(input(f"Digite a primeira entrada: "))
    peso1 = float(input(f"Digite o peso da primeira entrada: "))
    entrada2 = float(input(f"Digite a segunda entrada: "))
    peso2 = float(input(f"Digite o peso da segunda entrada: "))
    entrada3 = float(input(f"Digite a terceira entrada: "))
    peso3 = float(input(f"Digite o peso da terceira entrada: "))

    soma_ponderada = (entrada1 * peso1) + (entrada2 * peso2) + (entrada3 * peso3)

    LR = limite_rapido(soma_ponderada)
    FR = funcao_rampa(soma_ponderada)
    FS = sigmoid(soma_ponderada)
        
    LR_atual += LR
    FR_atual += FR
    FS_atual += FS
    num_neurons -= 1
    
    for i in range(num_neurons):
        peso = float(input(f"Digite o peso do proximo neuronio: "))
        soma_LR = (LR_atual * peso) 
        soma_FR = (FR_atual * peso) 
        soma_FS = (FS_atual * peso)

        LR = limite_rapido(soma_LR)
        FR = funcao_rampa(soma_FR)
        FS = sigmoid(soma_FS)
        
        LR_atual += LR
        FR_atual += FR
        FS_atual += FS
        
        i +=1
        
    print(f"LR: {LR_atual}\nFR: {FR_atual}\nFS: {FS_atual}")


if __name__ == "__main__":
    main()

