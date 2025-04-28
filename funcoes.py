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

def remover_dado (dados_rolados,dados_guardados,numero_inteiro):
    nova_lista = []
    i = 0 
    while i < len(dados_guardados):
        if dados_guardados[i]==numero_inteiro:
            dados_rolados.append(dados_guardados[i])
        else:
            nova_lista.append(dados_guardados[i])
    return [dados_rolados,nova_lista]