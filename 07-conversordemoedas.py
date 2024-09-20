real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.43
euro = real / 6.06
print('Com R${:.2f} voce pode comprar US{:.2f}' .format(real, dolar))
print('Com R${:.2f} voce pode comprar €1000{:.2f}' .format(real, euro))

