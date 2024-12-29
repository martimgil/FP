"""
Complete a função para devolver a mediana da lista de valores lst.
A função não deve modificar a lista.
Se a lista tiver um número ímpar de valores,
a mediana é o valor no meio da lista ordenada.
Se a lista tiver um número par de valores,
a mediana é a média dos dois valores no meio da lista ordenada.
"""

def median(lst):
   assert len(lst) > 0
   count = len(lst)
   lst.sort()
   sorted_lst = sorted(lst)
   if count%2!=0:
      return lst[count//2]
   else:
      mid1 = count // 2 - 1
      mid2 = count // 2
      return (sorted_lst[mid1] + sorted_lst[mid2]) / 2
      

def check(lst):
   backup = lst.copy()
   m = median(lst)
   return m, lst

