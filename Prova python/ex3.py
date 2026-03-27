# Monitor de inundação
nivel_rio = 0.0

while nivel_rio >= 0:
    nivel_rio = float(input("Digite o nivel do rio (em metros): "))

    if nivel_rio <= 3.0:
        print("Estado normal")
    elif nivel_rio <= 5.0:
        print("Estado de Alerta")
    else:
        print("Evacuacao imediata")

print("Nivel do rio abaixo de 0, monitoramento encerrado")