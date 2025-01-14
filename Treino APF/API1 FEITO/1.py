#Escreva um enunciado como o seguinte:

#Uma empresa deseja pintar um conjunto de colunas cilíndricas, todas com o mesmo diâmetro e altura. A tinta utilizada cobre uma área de 8 m² por litro.
# A empresa possui dois tipos de latas de tinta: latas grandes, com capacidade de 3 litros, e latas pequenas, com capacidade de 0,75 litro.

#Pergunte ao utilizador as dimensões das colunas (diâmetro e altura, em metros) e o número total de colunas.
#Determine a quantidade total de tinta necessária para pintar todas as colunas, considerando que a área de superfície lateral de cada coluna é um cilindro.
#Calcule o número mínimo de latas grandes e pequenas necessárias, priorizando o uso de latas grandes.
#Se forem necessárias 4 ou mais latas pequenas, substitua por uma lata grande adicional e ajuste o número de latas pequenas.
#Por fim, exiba a quantidade de tinta necessária (em litros) e o número de latas grandes e pequenas a serem compradas.
import math

diametro = float(input("Diametro? "))
altura = float(input("Altura? "))
n = int(input("Colunas? "))


pi = float(math.pi)



area = 2*pi*(diametro/2)*altura

area_total = n*area

litros = area_total/8

latas_grande = math.floor(litros//3)
sobra = litros - (latas_grande*3)
lata_pequena = math.ceil(sobra/0.75)

if lata_pequena>=4:
    latas_grande+=1
    lata_pequena-=4

print("Quantidade necessária (l)", litros)
print("Latas grandes", latas_grande)
print("Latas pequenas", lata_pequena)



