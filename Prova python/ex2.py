# Turnos de Rpg
hp_heroi = 100
hp_monstro = 100

while hp_heroi > 0 and hp_monstro > 0:
    dano_heroi = int(input("Digite o dano do heroi: "))
    dano_monstro = int(input("Digite o dano do monstro: "))
    
    hp_monstro = hp_monstro - dano_heroi
    hp_heroi = hp_heroi - dano_monstro
    
    print(f"Final da Rodada")
    print(f"Hp do heroi: {hp_heroi}")
    print(f"Hp do monstro: {hp_monstro}")

if hp_heroi > 0:
    print("O heroi venceu")
elif hp_monstro > 0:
    print("O monstro venceu")
else:
    print("Ninguem venceu, ambos morreram")