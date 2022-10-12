from datetime import datetime

# El * es para destructurar en Python

def to_upper(func):
  
  def wrapper(text):
    return func(text).upper()
  
  return wrapper


@to_upper
def print_message(name):
  return f'{name}, recibiste un mensaje'

print(print_message("David"))


def execution_time(func):
  
  def wrapper(*args, **kwargs):
    initial_time = datetime.now()
    func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed = final_time - initial_time
    print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
  
  return wrapper


@execution_time
def random_func():
  for _ in range(1, 1000000):
    pass


@execution_time
def sum(a: int, b: int) -> int:
  return a + b


random_func()
sum(1,2)