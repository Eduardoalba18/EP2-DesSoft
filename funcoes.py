import random
def rolar_dados (numero_inteiro):
    lista_dados =[]
    i = 0
    while i < numero_inteiro:
        numero = random.randint(1,6)
        lista_dados.append(numero)
        i += 1
    return lista_dados

def guardar_dado(lista_dados, dados_guardados, numero_inteiro):
    i = 0
    nova_lista = []
    while i < len(lista_dados):
        if i != numero_inteiro:
            nova_lista.append(lista_dados[i])
        else:
            dados_guardados.append(lista_dados[i]) 
        i +=1             
    return [nova_lista, dados_guardados] 

def remover_dado (dados_rolados,dados_no_estoque,dado_para_remover):
    lista = []
    i = 0
    while i < len(dados_no_estoque):
        if i == dado_para_remover:
            dados_rolados.append(dados_no_estoque[i])
        else:
            lista.append(dados_no_estoque[i])
        i +=1 
    return [dados_rolados, lista]

def calcula_pontos_regra_simples (lista_numeros_int):
    dicio = {}
    for numero in range (1,7):
        soma = 0 
        for dado in lista_numeros_int:
            if dado == numero:
                soma+= soma + numero
        dicio[numero]=soma
    return dicio