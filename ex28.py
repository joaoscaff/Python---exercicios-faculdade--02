#Um pouco de matemática

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite um número real: "))

produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
cubo = n3 ** 3

print(f"\nO produto do dobro do primeiro com metade do segundo é: {produto:.2f}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma:.2f}")
print(f"O terceiro elevado ao cubo é: {cubo:.2f}")