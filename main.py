from random import randint

def generatePassword():
  alredyIn = {}
  password = ''

  for i in range (15):
    character = chr(randint(33,125));
    while(alredyIn.get(character) != None):
     character = chr(randint(33,125));
    password += character
    alredyIn[character] = character
  return password

print(generatePassword())