def categoria (cat,cartela):
    num = ['1','2','3','4','5','6']
    if cat in num:
        cat = int(cat)
    if cat in cartela['regra_simples'] and cartela['regra_simples'][cat] != -1:
        return 1
    elif cat in cartela['regra_avancada'] and cartela['regra_avancada'][cat] != -1:
        return 1
    elif cat not in cartela['regra_simples'] and cat not in cartela['regra_avancada']:
        return 0

from funcoes import *

rolados = rolar_dados(5)
guardados = []

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

def turno(cartela, rolados, guardados):
    tentativas = 0
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = input()
    while acao != "0":
        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            numero = int(input())

            x = guardar_dado(rolados, guardados, numero)
            rolados = x[0]
            guardados=x[1]

            print(f"Dados rolados:{rolados}")
            print(f'Dados guardados:{guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            acao = input()

        elif acao =='2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            numero =int(input())

            x = remover_dado(rolados,guardados,numero)
            rolados = x[0]
            guardados=x[1]

            print(f"Dados rolados:{rolados}")
            print(f'Dados guardados:{guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            acao = input()

        elif acao =='3':
            if tentativas >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rolados = rolar_dados(len(rolados))
                tentativas+=1

            print(f"Dados rolados:{rolados}")
            print(f'Dados guardados:{guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            acao = input()
        
        elif acao =='4':
            imprime_cartela(cartela)

            print(f"Dados rolados:{rolados}")
            print(f'Dados guardados:{guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            acao = input()

        else:
            print("Opção inválida. Tente novamente.")
            acao = input()
    dado = rolados + guardados
    print("Digite a combinação desejada:") 
    categoria1 = input()
    y = categoria(categoria1,cartela)
    while y == 1 or y == 0:
        if y == 1:
            print("Essa combinação já foi utilizada.")
            categoria1=input()
        elif y ==0:
            print("Combinação inválida. Tente novamente.")
            categoria1=input()
        y = categoria(categoria1,cartela)
    faz_jogada(dado,categoria1,cartela)

    return cartela

rodados = 0

imprime_cartela(cartela)
print (f"Dados rolados:{rolados}")
print(f'Dados guardados:{guardados}')

while rodados < 12:
    cartela = turno (cartela,rolados,guardados)
    rolados= rolar_dados(5)
    guardados=[]

    if rodados != 11:
        print (f"Dados rolados:{rolados}")
        print(f'Dados guardados:{guardados}')
    
    rodados +=1

pontos = 0
pontos_simples=0

for chave,valor in cartela.items():
    for pont in valor.values():
        pontos+= pont
        if chave == "regra_simples":
            pontos_simples += pont
if pontos_simples >=63:
    pontos+=35

imprime_cartela(cartela)
print(f"Pontuação total: {pontos}")
