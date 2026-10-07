#Revenda

print("Se o preço de aquisição de um produto é menor que R$ 50,00, ele será vendido por um preço 45% maior, caso contrário o lucro será de 30%.")

produto = float(input("\nQual o valor do produto? "))

if produto <= 0:
    print("\nValor inválido.")

elif produto < 50:
    print(f"\nPreço final: R${produto + produto * 0.45:.2f}")

else:
    print(f"\nPreço final: R${produto + produto * 0.3:.2f}")