'''
    The bases class Pet has attributes name and age. The derived class Dog inherits attributes from the
    base class Pet class and includes a breed attribute. Complete the program to:
        Create a generic pet and print the pet's informatio using print_info()
        Create a Dog pet, use print_info() to print the dog's information, and add a statement to
            print the dog's breed attribute
    ex input:
        Dobby
        2
        Kreacher
        3
        German Schnauzer
    ex output:
        Pet Information:
            Name: Dobby
            Age: 2
        Pet Information:
            Name: Kreacher
            Age: 3
            Breed: German Schnauzer
'''
class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print('Pet Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.breed = ''

    def print_info(self):
        Pet.print_info(self)
        print(f'Breed: {self.breed}')

my_pet = Pet()
my_dog = Dog()

pet_name = input()
pet_age = int(input())
dog_name = input()
dog_age = int(input())
dog_breed = input()

# Create generic pet (using pet_name, pet_age) and then call print_info()
my_pet.name = pet_name
my_pet.age = pet_age
my_pet.print_info()

# Create dog pet (using dog_name, dog_age, dog_breed) and then call print_info()
my_dog.name = dog_name
my_dog.age = dog_age
my_dog.breed = dog_breed
my_dog.print_info()

