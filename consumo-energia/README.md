# ⚡ Calculadora de Consumo Elétrico Inteligente

## O sistema tem como objetivo calcular, de forma simples, o consumo mensal de energia elétrica de um aparelho e o custo estimado desse consumo, ajudando o usuário a entender melhor seus gastos com energia.

### O sistema foi desenvolvido utilizando *Python*.
<hr>

### Foram efetuados dois cálculos nesse programa:
**consumoMensal** = (potencia * horasDia * 30) / 1000

**custoEstimado** = consumoMensal * 0,75


Onde:

- potencia: potência do aparelho, em watts (W);

-  horasDia: tempo médio de uso diário, em horas;

- 30: número de dias considerados no mês;

- 0.75: tarifa fixa utilizada no cálculo, em R$/kWh;
  
<hr>

### Instruções para executar o programa:
Ter o python 3.10+ instalado na máquina

Informar os dados solicitados no terminal:
  - Nome do aparelho
  - Potência do aparelho em Watts(W)
  - Tempo médio de uso diário em horas
