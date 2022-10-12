import time

class FiboIter():

  def __iter__(self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    
    return self


  def __next__(self):
    if self.counter == 0:
      self.counter += 1

      return self.n1
    elif self.counter == 1:
      self.counter += 1

      return self.n2
    else:
      self.aux = self.n1 + self.n2
      
      # Swapping: n1 = n2 y n2 = aux
      self.n1, self.n2 = self.n2, self.aux
      self.counter += 1

      return self.aux

# if __name__ == "__main__":
#   fibonacci = FiboIter()
  
#   for element in fibonacci:
#     print(element)
#     time.sleep(1)


# Generadores: Son funciones que hacen lo mismo que los iteradores, pero en lugar de clases son funciones

# Generator expression: Esta forma de usarlos es similar a las list comprehension, pero a diferencia de estas, es mejor para valores infinitos o valores muy grandes
my_list = [0,1,4,7,9,10]

my_second_gen = (x*2 for x in my_list)
print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))