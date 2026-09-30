print("Anel de identificação: R$4,00")
print("Anel de alimento: R$3,50")
print("Cada frango precisa de um anel de id. no pé direito e dois anéis de alimento no pé esquerdo.")

frango = int(input("\nDigite a quantidade de frangos desejada: "))
gasto = frango * 4 + frango * 7

print(f"\nQuantidade de frangos: {frango}")
print(f"Valor a ser gasto com os anéis: R${gasto:.2f}")