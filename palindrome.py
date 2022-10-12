def is_palindrome(word: str) -> bool:
  new_word = word.replace(" ", "").lower()
  return new_word == new_word[::-1]

def run():
  print(is_palindrome(12))

if __name__ == "__main__":
  run()