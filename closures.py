# Hola -> 3 HolaHolaHola

def make_repeater_of(times):

  def repeater(word):
    assert type(word) == str, "Sólo puedes utilizar cadenas de texto"
    return word * times
  
  return repeater


def run():
  repeat_5 = make_repeater_of(5)
  print(repeat_5(input("Escribe la palabra a repetir 5 veces: ")))

  
if __name__ == "__main__":
  run()