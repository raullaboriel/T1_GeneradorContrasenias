from random import randint

def passwordGenerator():
  Password = ''
  AlredyIn = [];

  for i in range (15):
    Character = chr(randint(33, 125))
    while(Character in AlredyIn):
      Character = chr(randint(33, 125))
    Password = Password + Character
    AlredyIn.append(Character);
  return Password
  
print(passwordGenerator())