def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100 if total_votos > 0 else 0

# Inicializando array para contar os votos de cada jogador
num_jogadores = 23
votos = [0] * num_jogadores

# Loop para receber votos
while True:
    try:
        voto = int(input("Digite o número do jogador (1 a 23, 0 para encerrar): "))
        
        if voto == 0:
            break

        if 1 <= voto <= 23:
            votos[voto - 1] += 1
        else:
            print("Número inválido. Por favor, digite um número entre 1 e 23.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Calculando o total de votos
total_votos = sum(votos)

# Imprimindo resultados
print("\nResultado da votação:")
print(f"Total de votos computados: {total_votos}")

for i in range(num_jogadores):
    if votos[i] > 0:
        percentual = calcular_percentual(votos[i], total_votos)
        print(f"Jogador {i + 1}: {votos[i]} votos ({percentual:.2f}%)")

# Encontrando o jogador mais votado
melhor_jogador = votos.index(max(votos)) + 1
percentual_melhor_jogador = calcular_percentual(votos[melhor_jogador - 1], total_votos)
print(f"\nMelhor jogador da partida: Jogador {melhor_jogador} com {votos[melhor_jogador - 1]} votos ({percentual_melhor_jogador:.2f}%)")

# Gravando os resultados em um arquivo texto
with open("resultado_votacao.txt", "w") as arquivo:
    arquivo.write(f"Total de votos computados: {total_votos}\n\n")
    
    for i in range(num_jogadores):
        if votos[i] > 0:
            percentual = calcular_percentual(votos[i], total_votos)
            arquivo.write(f"Jogador {i + 1}: {votos[i]} votos ({percentual:.2f}%)\n")
    
    arquivo.write(f"\nMelhor jogador da partida: Jogador {melhor_jogador} com {votos[melhor_jogador - 1]} votos ({percentual_melhor_jogador:.2f}%)")

print("Resultados gravados no arquivo resultado_votacao.txt.")
