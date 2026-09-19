lado_a = float(input("Digite o valor do lado A do triângulo: "))
lado_b = float(input("Digite o valor do lado B do triângulo: "))
lado_c = float(input("Digite o valor do lado C do triângulo: "))

if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
    print("Os valores informados não formam um triângulo.")

elif lado_a == lado_b and lado_b == lado_c:
    print("O triângulo é equilátero.")

elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("O triângulo é isósceles.")

elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print("O triângulo é escaleno.")