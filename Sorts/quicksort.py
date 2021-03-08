import random

def quicksort(lista):
  tamanho_lista = len(lista)
  if tamanho_lista > 0:
    # pivo = lista[tamanho_lista - 1] #Pivo fixo no final à direita
    pivo = lista[random.randint(0, len(lista) - 1)] # Critério pivô aleatório
  elif tamanho_lista == 0:
    return lista
  sublista_menor = []
  sublista_maior = []
  sublista_pivo = []
  for elemento in lista:
    if elemento < pivo:
      sublista_menor.append(elemento)
    elif elemento > pivo:
      sublista_maior.append(elemento)
    elif elemento == pivo:
      sublista_pivo.append(elemento)
  if tamanho_lista == 1:
    return lista[0:]
  if lista == sublista_pivo:
    return lista[0:]
  else:
    return quicksort(sublista_menor) + quicksort(sublista_pivo) + quicksort(sublista_maior)

lista = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]

print(quicksort(lista))
    

