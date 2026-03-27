# Media de temperatura global

quantidade_dias = int(input("Digite a quantidade de dias a serem medidos: "))
soma_temperaturas = 0.0
i = 0

while i < quantidade_dias:
    temperatura_dia = float(input(f"Digite a temperatura do dia {i + 1}: "))
    soma_temperaturas = soma_temperaturas + temperatura_dia
    i = i + 1

media_temperaturas = soma_temperaturas / quantidade_dias
print(f"A media de temperatura global e: {media_temperaturas:.2f}°C")
      
if media_temperaturas > 25.0:
    print("Media acima do esperado")
else:
    print("Media dentro da normalidade")