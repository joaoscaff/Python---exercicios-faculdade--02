produto = float(input("Digite o valor do produto: "))
desconto = produto * 0.1

print(f"\nPreço do produto: R${produto}")
print(f"Valor a ser descontado(10%): R${desconto:.2f}")
print(f"Preço final do produto: R${produto - desconto:.2f}")