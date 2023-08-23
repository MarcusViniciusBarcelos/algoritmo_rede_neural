def rampa(x):
    return 1 if x > 0 else 0


def ajuste(x1, x2, yd, yo):
    global w1, w2  # Definindo w1 e w2 como globais para poderem ser modificados

    w1 += 1 * (yd - yo) * x1
    w2 += 1 * (yd - yo) * x2


entradas = [[1, 1], [1, 0], [0, 1], [0, 0]]
saidas = [1, 1, 0, 0]

w1 = -1
w2 = -1

c = 1

num_epocas = 10000

# Treinamento da rede neural usando regra delta
rede_treinada = False
while not rede_treinada:
    rede_treinada = True

    for i in range(len(entradas)):
        entrada = entradas[i]
        saida_desejada = saidas[i]

        # Cálculo do potencial de ativação
        potencial_ativacao = entrada[0] * w1 + entrada[1] * w2

        # função de transferência
        saida_atual = rampa(potencial_ativacao)

        # função condicional para ajustar os pesos caso a saida seja errada
        if saida_atual != saida_desejada:
            rede_treinada = False
            ajuste(entrada[0], entrada[1], saida_desejada, saida_atual)


for i in range(len(entradas)):
    entrada = entradas[i]
    potencial_ativacao = entrada[0] * w1 + entrada[1] * w2
    saida_atual = rampa(potencial_ativacao)
    print(f"Entrada: {entrada}, Saída Atual: {saida_atual}")
