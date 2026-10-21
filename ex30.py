print("João, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.")

peso = float(input("\nDigite, em quilos, o peso total de peixes pescados: "))
excesso = peso - 50
multa = excesso * 4

if peso <=0:
    print("\nPeso inválido.")

elif peso <=50:
    print("\nNão precisará pagar multa.")

else:
    print(f"\nO valor da multa a ser pago é R${multa:.2f}.")