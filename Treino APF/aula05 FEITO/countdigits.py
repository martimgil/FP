"""
Crie uma função que conte quantos dígitos há numa dada string.
Por exemplo:  countDigits("23 mil 456") deve devolver 5.
Sugestão: o método isdigit verifica se uma string só tem dígitos,
e.g., "2".isdigit() -> True.
"""

# Defina a função aqui.
def countDigits(str):
   count=0
   for element in str:
      if element.isdigit():
         count+=1
   return count


def main():
   str = input()
   # Não deve precisar de mudar nada aqui...
   
   print("str:", repr(str))
   print("result:", countDigits(str) )

if __name__ == "__main__":
   main()


