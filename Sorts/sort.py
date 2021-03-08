list = [37, 48, 59, 12, 24, 3, 5, 9, 10]
i = 0 
listaOrganizada = []
tamanho_lista = len(list)

while i != tamanho_lista:
  menor_numero = min(list)
  listaOrganizada.append(menor_numero)
  list.remove(menor_numero)
  i += 1

print(listaOrganizada)