# tarefa avaliativa
# lista e decomposição funcional
# Criar um programa com método que popule n numeros aleatórios (100 a 400) em uma lista. Também crie método que exiba a lista.
# O método a ser criado para avaliação, não pode ter pacotes, bibliotecas ou funções prontas do Python.
# O método deve receber uma lista com números e retirar (da própria lista) todos os números replicados.
# Por exemplo, lista inicial = [6,4,2,6,9,2,6]
# lista transformada = [6,4,2,9]

import random

def popula_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(random.randint(100, 400))
    return lista

def exibe_lista(lista):
    print("Lista de números:")
    for num in lista:
        print(num, end=" ")
    print()

def remove_duplicados(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                del lista[j]
            else:
                j += 1
        i += 1


tamanho_lista = int(input("Digite o tamanho da lista: "))
numeros = popula_lista(tamanho_lista)

exibe_lista(numeros)

remove_duplicados(numeros)
exibe_lista(numeros)
