class Pet():
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.set_all()
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception
    
    def set_all(self):
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
        return owner_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):
        pet_names = []
        self.pet_list = []
        for object in Pet.all:
            pet_names.append(object.name)
        sorted_pet_names = sorted(pet_names)
        for name in sorted_pet_names:
            for pet in Pet.all:
                if name == pet.name:
                    self.pet_list.append(pet)
        return self.pet_list
        # return sorted_pets

owner = Owner('Ben')
pet1 = Pet('Fido', 'dog', owner)
pet2 = Pet('Clifford', 'dog', owner)

print(owner.get_sorted_pets())
print(owner.pet_list)
print(owner.pet_list[1].name)