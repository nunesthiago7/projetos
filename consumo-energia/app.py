aparelho = str(input("Digite o nome do aparelho: ")).strip().title()
potencia = float(input("Digite a potência do aparelho em watts(W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = consumoMensal * 0.75

print("")
print(f'Aparelho: {aparelho}')
print(f'Consumo estimado: {consumoMensal}kWh/mês')
print(f'Custo estimado de: R${custoEstimado:.2f} por kWh')