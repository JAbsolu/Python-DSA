class Person:
  def __init__(self, name, occupation, school):
    self.name = name
    self.occupation = occupation
    self.school = school


newPerson = Person('Johnson', 'SWE', 'SCSU')

print(newPerson.name)
print(newPerson.occupation)
print(newPerson.school)

introduce = f'Hello! my name is {newPerson.name}, my occupation is {newPerson.occupation}, and I went to {newPerson.school}'

print(introduce)