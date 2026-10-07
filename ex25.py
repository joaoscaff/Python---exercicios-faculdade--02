#Venda de roupa

print("Preços: \nCamiseta P: R$10,00 \nCamiseta M: R$12,00 \nCamiseta G: R$15,00")

p = int(input("\nQuantas camisetas P você deseja? "))
m = int(input("Quantas camisetas M você deseja? "))
g = int(input("Quantas camisetas G você deseja? "))

p = p * 10
m = m * 12
g = g * 15

total = p + m + g

if total <= 0:
    print("\nCarrinho vazio.")

elif p <= 0:
    print(f"\nRevisão do pedido: \nCamisetas M: R${m:.2f} \nCamisetas G: R${g:.2f} \nTotal: R${total:.2f}")

elif m <= 0:
    print(f"\nRevisão do pedido: \nCamisetas P: R${p:.2f} \nCamisetas G: R${g:.2f} \nTotal: R${total:.2f}")

elif g <= 0:
    print(f"\nRevisão do pedido: \nCamisetas P: R${p:.2f} \nCamisetas M: R${m:.2f} \nTotal: R${total:.2f}")

else:
    print(f"\nRevisão do pedido: \nCamisetas P: R${p:.2f} \nCamisetas M: R${m:.2f} \nCamisetas G: R${g:.2f} \nTotal: R${total:.2f}")