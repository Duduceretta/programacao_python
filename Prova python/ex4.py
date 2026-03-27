# Coletor de itens e inventario
capacidade_maxima = 15.0
capacidade_atual = 0.0

while capacidade_atual < capacidade_maxima:
    peso_item = float(input(f"Digite o peso do item: "))

    if capacidade_atual + peso_item <= capacidade_maxima:
        print(f"Item adicionado")
        capacidade_atual += peso_item
    else:
        print(f"Mochila cheia, item descartado.")
        print(f"Peso final da mochila: {capacidade_atual} kg")
        break   