import pet

def main():
  pets = []  #create an array to save the pets
  petData = open("petData.txt", "r")  #open the pet data file

  for item in petData:  #for each line in the file
    data = item.strip().split(" ")  #split the line into an array
    name = data[0]  #save the name
    species = data[1]  #save the species
    family = data[2]  #save the family
    owner = data[3]  #save the owner

    newPet = pet.Pet(name, species, family, owner)  #create a new pet
    pets.append(newPet)  #add the pet to the array

  petData.close()  #close the file

  # Second step - find all owner(s) with snake family type and insect family type pets.
  def get_snake_family_type(pet):
    petFamType = pet.get_family_type()  #get the pet family type

    if (petFamType == "snake" or petFamType == "insect"):
      print(f"This pet's type is {petFamType} and the owner is {pet.get_owner()} \n")


  # First step ----- Output the pets data
  for item in pets:
    get_snake_family_type(item) #Get the family type of the snake and its owner

if __name__ == '__main__':
  main()
