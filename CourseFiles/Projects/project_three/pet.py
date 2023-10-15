class Pet():
  def __init__(self, petName, petSpecies, petFamilyType, petOwnerName):
    self.__petName = petName
    self.__petSpecies = petSpecies
    self.__petFamilyType = petFamilyType
    self.__petOwnerName = petOwnerName

  def set_name(self, petName):
    self.__petName = petName
  
  def set_species(self, petSpecies):
    self.__petSpecies = petSpecies
  
  def set_family_type(self, petFamilyType):
    self.__petFamilyType = petFamilyType

  def set_owner_name(self, petOwnerName):
    self.__petOwnerName = petOwnerName

  # Accessor methods
  def get_name(self):
    return self.__petName

  def get_species(self):
    return self.__petSpecies

  def get_family_type(self):
    return self.__petFamilyType
  
  def get_owner(self):
    return self.__petOwnerName



if __name__ == "__Pet__":
  Pet()



  