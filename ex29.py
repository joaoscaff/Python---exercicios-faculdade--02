#Peso Ideal

h = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo(M/F): ").strip().lower()

pesoH = (72.7*h) - 58
pesoF = (62.1*h) - 44.7

if h <= 0:
    print("\nAltura inválida.")

elif sexo in ("m", "masculino"):
    print(f"\nSeu peso ideal é: {pesoH:.2f}")

elif sexo in ("f", "feminino"):
    print(f"\nSeu peso ideal é: {pesoF:.2f}")

else:
    print("\nSexo inválido.")