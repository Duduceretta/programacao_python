def ler_arquivo_gerar_dicionario(caminho_arquivo):
    lista_jogadores = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            jogador = {
                "nome": dados[0],
                "classe": dados[1],
                "kills": int(dados[2]),
                "deaths": int(dados[3]),
                "dano": int(dados[4])
            }

            lista_jogadores.append(jogador)

    return lista_jogadores


def filtrar_jogadores_por_classe(lista_jogadores, classe):
    lista_jogadores_filtrados = []
    
    for jogador in lista_jogadores:
        if jogador["classe"] == classe:
            lista_jogadores_filtrados.append(jogador)

    return lista_jogadores_filtrados


def calcular_kda(kills, deaths):
    if deaths == 0:
        return float(kills)
    return kills / deaths


# Fluxo principal do programa
lista = ler_arquivo_gerar_dicionario("partida.txt")

maior_dano = 0
jogador_maior_dano = ""

total_kills = 0
jogadores_kda_maior_que_2 = []

for jogador in lista:
    if jogador["dano"] > maior_dano:
        maior_dano = jogador["dano"]
        jogador_maior_dano = jogador["nome"]
        
    total_kills += jogador["kills"]
    
    kda = calcular_kda(jogador["kills"], jogador["deaths"])
    if kda > 2.0:
        jogadores_kda_maior_que_2.append((jogador["nome"].upper(), kda))

if len(lista) > 0:
    media_kills = total_kills / len(lista)
else:
    media_kills = 0


print("-" * 40)
print("RELATÓRIO DE PERFORMANCE DA PARTIDA")
print("-" * 40)

print(f"Jogador com maior dano: {jogador_maior_dano} ({maior_dano} de dano)")
print(f"Média de kills da partida: {media_kills:.2f} kills por jogador")

print("\nJogadores com KDA superior a 2.0:")
for nome, kda in jogadores_kda_maior_que_2:
    print(f" - {nome} (KDA: {kda:.2f})")

print("-" * 40)

classe = input("Digite a classe que deseja filtrar (ex: Guerreiro, Mago, Arqueiro, Ladrão): ")
lista_classes = ["Guerreiro", "Mago", "Arqueiro", "Ladrão"]

while classe not in lista_classes:
    print("Classe inválida. Por favor, escolha entre: Guerreiro, Mago, Arqueiro, Ladrão.")
    classe = input("Digite a classe que deseja filtrar (ex: Guerreiro, Mago, Arqueiro, Ladrão): ")

print("\n Jogadores da classe filtrada:")
jogadores_filtrados = filtrar_jogadores_por_classe(lista, classe)

for jogador in jogadores_filtrados:
    print(f" - {jogador['nome']} (Classe: {jogador['classe']}, Kills: {jogador['kills']}, Deaths: {jogador['deaths']}, Dano: {jogador['dano']})")
