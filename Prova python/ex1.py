# O Reflorestador
meta_biomassa = float(input("Digite a meta de biomassa: "))

biomassa = 0.0
arvores = 0

while biomassa < meta_biomassa:
    biomassa_arvore = float(input(f"Digite a biomassa da arvore {arvores + 1}: "))
    
    biomassa = biomassa + biomassa_arvore
    arvores = arvores + 1

print(f"Meta de biomassa atingida com {arvores} arvores plantadas")