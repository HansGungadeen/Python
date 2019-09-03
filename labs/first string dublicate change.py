str = input("Enter String: ")

def change_char(str):
  char = str[0]
  str = str.replace(char, '$')
  str = char + str[1:]

  return str

print(change_char(str))