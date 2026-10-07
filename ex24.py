#Produção de sanduíche

print("Em um sanduíche vão duas fatias de queijo(50g), uma fatia de presunto(50g) e uma rodela de hambúrguer(100g).")

sanduiche = int(input("\nDigite a quantidade de sanduíches a ser produzida: "))

mussarela = sanduiche * 0.1
presunto = sanduiche * 0.05
hamburguer = sanduiche * 0.1

if sanduiche <= 0:
    print("\nVocê não precisa de nenhum ingrediente.")

else:
    print(f"\nVocê precisará de {mussarela:.2f}kg de mussarela, {presunto:.2f}kg de presunto e {hamburguer:.2f}kg de hambúrguer.")