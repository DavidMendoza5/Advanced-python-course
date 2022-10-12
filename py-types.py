from typing import Dict, List, Tuple

# Con el módulo mypy se puede emular el comportamiento de un lenguaje estático, mostrando errores antes de que el código se ejecute
# mypy archivo.py --check-untyped-defs 

def sum(a: int, b:int) -> int:
  return a + b

print(sum(1,2))

positives: List[int] = [1,2,3,4,5]
print(positives)

users: Dict[str, int] = {
  'argentina': 1,
  'méxico': 34
}
print(users)

countries: List[Dict[str, str]] = [
  {
    'name': 'México',
    'people': '9000000'
  }
]
print(countries)

numbers: Tuple[int, float, int] = (1, 4.5, 3)
print(numbers)

CoordinateType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinateType = [
  {
    'coord1': (1,2),
    'coord2': (3,5)
  }
]

print(coordinates)