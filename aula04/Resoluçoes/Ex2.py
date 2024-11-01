# This program shows a table of the squares of four numbers.
# Modify the program to show the squares of 1..20.  Use the range function.
# Also, add a column to show 2**n.  Adjust the formatting.

#:2s: Especifica que o valor a ser formatado é uma string (s) e deve ter um mínimo de 2 caracteres de largura. Se a string for menor que 2 caracteres, ela será preenchida com espaços à esquerda.
#:2d: Especifica que o valor a ser formatado é um número inteiro (d) e deve ter um mínimo de 2 dígitos de largura. Se o número tiver menos de 2 dígitos, ele será preenchido com espaços à esquerda.
#:2f é usado para floats e define o minimo de caracteres que deve ter, caso nao tiver é preenchido os espaços na mesma
#:.2f é usado para definir apenas duas casas decimais
#:>2f para encostar a direia e :<2f para encostar os numeros a esquerda


print("{:>2s} {:>3s} {:>8s}".format("n", "n²","2**n"))
for n in list(range(1,21)):
    print("{:>2d} {:>3d} {:>8d}".format(n, n**2, 2**n))
