salario = float(input("Digite seu salário: "))
vendas = float(input("Digite, em reais, quanto faturou em vendas esse mês: "))
comissao = vendas * 0.04

print(f"\nSalário: R${salario}")
print(f"Valor da comissão: R${comissao:.2f}")
print(f"Salário final: R${salario + comissao:.2f}")