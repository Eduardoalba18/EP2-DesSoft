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
                soma+= numero
        dicio[numero]=soma
    return dicio

def calcula_pontos_soma (lista_numeros):
    i = 0
    soma = 0
    while i < len(lista_numeros):
        soma += lista_numeros[i]
        i += 1
    return soma

def calcula_pontos_sequencia_baixa (lista_numeros):
    if 1 in lista_numeros and 2 in lista_numeros and 3 in lista_numeros and 4 in lista_numeros:
        return 15
    if 2 in lista_numeros and 3 in lista_numeros and 4 in lista_numeros and 5 in lista_numeros:
        return 15
    if  3 in lista_numeros and 4 in lista_numeros and 5 in lista_numeros and 6 in lista_numeros:
        return 15
    else: 
        return 0 

def calcula_pontos_sequencia_alta (lista_numeros):
    if  1 in lista_numeros and 2 in lista_numeros and 3 in lista_numeros and 4 in lista_numeros and 5 in lista_numeros:
        return 30
    if 2 in lista_numeros and 3 in lista_numeros and 4 in lista_numeros and 5 in lista_numeros and 6 in lista_numeros:
        return 30 
    else: 
        return 0 

def calcula_pontos_full_house (lista_numeros):
    dicio = {}
    for numero in lista_numeros:
        if numero in dicio:
            dicio[numero]+= 1
        else:
            dicio[numero]=1
    valor1 = 3
    valor2 = 2
    if valor1 in dicio.values() and valor2 in dicio.values():
        soma = 0
        for numero,quantidade in dicio.items():
            soma += dicio[numero]
    return soma            
