salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    print(f"Salário atual: R${salario:.2f}")
    print("Percentual de aumento aplicado: 20%")
    print(f"Valor do aumento: R${salario * 0.20:.2f}")
    print(f"Novo salário: R${salario + salario * 0.20:.2f}")

elif salario > 280 and salario <= 700:
    print(f"Salário atual: R${salario:.2f}")
    print("Percentual de aumento aplicado: 15%")
    print(f"Valor do aumento: R${salario * 0.15:.2f}")
    print(f"Novo salário: R${salario + salario * 0.15:.2f}")

elif salario > 700 and salario <= 1500:
    print(f"Salário atual: R${salario:.2f}")
    print("Percentual de aumento aplicado: 10%")
    print(f"Valor do aumento: R${salario * 0.10:.2f}")
    print(f"Novo salário: R${salario + salario * 0.10:.2f}")

else:
    print(f"Salário atual: R${salario:.2f}")
    print("Percentual de aumento aplicado: 5%")
    print(f"Valor do aumento: R${salario * 0.05:.2f}")
    print(f"Novo salário: R${salario + salario * 0.05:.2f}")