def limite_rapido(x):
    return 1 if x > 0 else -1

def funcao_rampa(x):
    return 1 if x > 0 else 0

def sigmoid(x):
    return 1 * (-1 /(1+x)) if x >= 0 else -1 * (1 /(1-x))

def main():
    num_neurons = int(input("Digite a quantidade de neurônios: "))
    
    entradas = []
    pesos = []
    saida_atual = 0
    
    for i in range(num_neurons):
        entrada = float(input(f"Digite a entrada para o neurônio {i + 1}: "))
        entradas.append(entrada)
        
        if i > 0:
            peso = float(input(f"Digite o peso para o neurônio {i + 1}: "))
            pesos.append(peso)
            
            soma_ponderada = saida_atual * peso
            
            funcao = int(input(f"Escolha a função de ativação para o neurônio {i + 1} (1 - Limite Rapido, 2 - Funcao Rampa, 3 - Funcao Sigmoid): "))
            
            if funcao == 1:
                saida_atual = limite_rapido(soma_ponderada)
            elif funcao == 2:
                saida_atual = funcao_rampa(soma_ponderada)
            elif funcao == 3:
                saida_atual = sigmoid(soma_ponderada)
            else:
                print("Opção inválida! Usando função de ativação padrão.")
                saida_atual = limite_rapido(soma_ponderada)
        else:
            saida_atual = entrada  # Primeiro neurônio não tem peso nem função de ativação
        
    print(f"Saida do último neurônio: {saida_atual}")

if __name__ == "__main__":
    main()
