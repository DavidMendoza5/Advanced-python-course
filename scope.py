# Local scope
def my_func():
  y = 3
  print("Local scope",y)

my_func()


# Global scope
y = 5

def my_other_func():
  print("Global scope",y)

my_other_func()


# Nested functions
def main_func():
  a = 1
  
  def nested():
    print("Nested",a)
  
  nested()

main_func()


# Closures
def second_main_func():
  a = 1
  
  def nested():
    print("Nested returned",a)
  
  return nested

func_variable = second_main_func()
func_variable()

def make_multiplier(x):

  def multiplier(n):
    return x * n
  
  return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))