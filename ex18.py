valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    print(f"Salário bruto({valor_hora} * {horas_trabalhadas}): R${salario_bruto:.2f}")
    print("(-)IR: Isento")
    print(f"(-)INSS(10%): R${salario_bruto * 0.10:.2f}")
    print(f"FGTS(11%): R${salario_bruto * 0.11:.2f}")
    print(f"Total de descontos: R${salario_bruto * 0.10:.2f}")
    print(f"Salário líquido: R${salario_bruto - salario_bruto * 0.10:.2f}")

elif salario_bruto > 900 and salario_bruto <= 1500:
    print(f"Salário bruto({valor_hora} * {horas_trabalhadas}): R${salario_bruto:.2f}")
    print(f"(-)IR(5%): R${salario_bruto * 0.05:.2f}")
    print(f"(-)INSS(10%): R${salario_bruto * 0.10:.2f}")
    print(f"FGTS(11%): R${salario_bruto * 0.11:.2f}")
    print(f"Total de descontos: R${salario_bruto * 0.15:.2f}")
    print(f"Salário líquido: R${salario_bruto - salario_bruto * 0.15:.2f}")

elif salario_bruto > 1500 and salario_bruto <= 2500:
    print(f"Salário bruto({valor_hora} * {horas_trabalhadas}): R${salario_bruto:.2f}")
    print(f"(-)IR(10%): R${salario_bruto * 0.10:.2f}")
    print(f"(-)INSS(10%): R${salario_bruto * 0.10:.2f}")
    print(f"FGTS(11%): R${salario_bruto * 0.11:.2f}")
    print(f"Total de descontos: R${salario_bruto * 0.20:.2f}")
    print(f"Salário líquido: R${salario_bruto - salario_bruto * 0.20:.2f}")

else:
    print(f"Salário bruto({valor_hora} * {horas_trabalhadas}): R${salario_bruto:.2f}")
    print(f"(-)IR(20%): R${salario_bruto * 0.20:.2f}")
    print(f"(-)INSS(10%): R${salario_bruto * 0.10:.2f}")
    print(f"FGTS(11%): R${salario_bruto * 0.11:.2f}")
    print(f"Total de descontos: R${salario_bruto * 0.30:.2f}")
    print(f"Salário líquido: R${salario_bruto - salario_bruto * 0.30:.2f}")