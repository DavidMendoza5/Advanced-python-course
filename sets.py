# La declaración de un conjunto (set), es similar a la de un diccionario, pero sólo lleva valores, no es clave-valor
my_set = {3, 4, 5}
print(my_set)


my_set2 = {"Hola", 23.3, False, True}
print(my_set2)


# Si se pone un  valor repetido, python lo elimina, ya que en un set no se pueden repetir los valores
my_set3 = {3, 3, 2}
print(my_set3)


# Si se intenta poner un elemento mutable (en este caso una lista) dentro de un set, este lanzará un error
# my_set4 = {[1,2], 4}


# Si quiero generar un set vacío, se debe hacer de la siguiente manera para evitar que python lo tome como un diccionario vacío
empty_set = set()
print(type(empty_set))


# Casting
my_list = [1, 2, 1, 4, 5, 3]
my_list_set = set(my_list)
print(my_list_set)


# Añadir elementos
my_list_set.add(6)
print(my_list_set)


# Añadir varios elementos
my_list_set.update([1, 2, 7], {8, 9}, (1, 4, 10))
print(my_list_set)


# Borrar elementos de un set
my_list_set.discard(10)
print(my_list_set)

my_list_set.remove(9)
print(my_list_set)

# Si el elemento no existe y se intenta borrar, se debe usar discard, ya que si se usa remove, lanzará un error (KeyError)
my_list_set.discard(20)
print(my_list_set)

# Borrar un elemento aleatorio
my_list_set.pop()
print(my_list_set)

# Eliminar todos los elementos del set
my_list_set.clear()
print(my_list_set)


# Unión de sets, igual se puede hacer de la sigueinte forma: my_set.union(my_set3)
my_union_set = my_set | my_set3
print("Unión Set1 y Set3:", my_union_set)


# Intersección de sets, igual se puede hacer de la sigueinte forma: my_set.intersection(my_set3)
my_intersection_set = my_set & my_set3
print("Intersección Set1 y Set3:", my_intersection_set)


# Diferencia de sets, igual se puede hacer de la sigueinte forma: my_set.difference(my_set3)
my_difference_set = my_set - my_set3
print("Diferencia Set1 y Set3:", my_difference_set)


# Diferencia simétrica (contrario a la intersección) de sets, igual se puede hacer de la sigueinte forma: my_set.symmetric_difference(my_set3)
my_symmetric_difference_set = my_set ^ my_set3
print("Diferencia simétrica Set1 y Set3:", my_symmetric_difference_set)


# Eliminar elementos duplicados de una lista
def remove_duplicates(some_list):
  # without_duplicates = []
  # for element in some_list:
  #   if element not in without_duplicates:
  #     without_duplicates.append(element)
  
  # return without_duplicates

  return list(set(some_list))

def run():
  random_list = [1, 1, 2, 4, 6, 2]
  print(remove_duplicates(random_list))

run()