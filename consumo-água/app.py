print("=" * 60)
print(" CAMPANHA DE CONSCIENTIZAÇÃO AMBIENTAL - ÁGUA & CIDADANIA")
print("=" * 60)
print()

# Entrada do tipo de imóvel
tipo_imovel = input("Informe o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Entrada do consumo mensal (aceita vírgula ou ponto como decimal)
consumo_texto = input("Informe o consumo mensal de água em m³ (ex: 12.5): ").strip().replace(",", ".")
consumo_m3 = float(consumo_texto)

# Classificação de acordo com as regras de negócio
if tipo_imovel == "comercial":
    mensagem = "Tarifa comercial aplicada – consulte o plano corporativo."
elif tipo_imovel == "apartamento" and consumo_m3 < 10:
    mensagem = "Consumo econômico – excelente controle de água!"
elif tipo_imovel in ("apartamento", "casa") and consumo_m3 <= 25:
    mensagem = "Consumo moderado – dentro do padrão residencial."
else:
    mensagem = "Consumo excessivo – adote medidas de economia e verifique vazamentos."

# Exibição do resultado
print("\n" + "-" * 60)
print(f"Tipo de imóvel : {tipo_imovel.capitalize()}")
print(f"Consumo mensal : {consumo_m3:.2f} m³")
print("-" * 60)
print(f"➡ {mensagem}")
print("-" * 60)