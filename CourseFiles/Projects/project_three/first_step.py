import pet

def main():
  petData = open("petData.txt", "r")  #open the pet data file

  for item in petData:  #for each line in the file
    data = item.strip().split(" ")  #split the line into an array
    name = data[0]  #save the name
    species = data[1]  #save the species
    family = data[2]  #save the family
    owner = data[3]  #save the owner

    newPet = pet.Pet(name, species, family, owner)  #create a new pet
    
    print(f"The pet name is {newPet.get_name()}.")  #output the pet name
    print(f"The pet's species is {newPet.get_species()}.")  #output the pet species
    print(f"The pet's family type is {newPet.get_family_type()}.")  #output the pet family type
    print(f"The pet's owner is {newPet.get_owner()}.\n")  #output the pet owner
    
  petData.close()  #close the file

if __name__ == '__main__':
  main()
