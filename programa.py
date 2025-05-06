from funcoes import *
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
rodada = 0
while rodada < 12:
    guardados = []
    rolados = rolar_dados(5)
    rolagem1 = 0
    while True:
        print("Dados rolados:", rolados)
        print("Dados guardados:", guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        escolha = input()
        if escolha == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(rolados):
                resultado = guardar_dado(rolados,guardados,indice)
                rolados = resultado[0]
                guardados = resultado[1]
        elif escolha == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(guardados):
                resultado = remover_dado(rolados, guardados, indice)
                rolados = resultado[0]
                guardados = resultado[1]
        elif escolha == "3":
            if rolagem1 < 2:
                rolagem1 +=1
                rolados = rolar_dados(len(rolados))
            else:
                print("Você já usou todas as rerrolagens.")
        elif escolha == "4":
            imprime_cartela(cartela)
        elif escolha == "0":
            finais = rolados + guardados
            print("Digite a combinação desejada:")
            nivel = input()
            if nivel.isdigit()and int(nivel) in cartela['regra_simples'] and cartela['regra_simples'][int(nivel)] != -1:
                print("Essa combinação já foi utilizada.")
            elif nivel in cartela['regra_avancada'] and cartela['regra_avancada'][nivel] != -1:
                print("Essa combinação já foi utilizada.")
            elif (nivel.isdigit() and int(nivel) in cartela['regra_simples']) or nivel in cartela['regra_avancada']:
                cartela = faz_jogada(finais,nivel,cartela)
                rodada +=1
                break
            else:
                print("Combinação inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

pontos = 0
for numero in cartela['regra_simples'].values():
    if numero != -1:
        pontos += numero
for numero in cartela['regra_avancada'].values():
    if numero != -1:
        pontos += numero
soma = 0
for numero in cartela['regra_simples'].values():
    if numero != -1:
        soma += numero
if soma >= 63:
    pontos += 35 
imprime_cartela(cartela)
print("Pontuação total:", pontos)
