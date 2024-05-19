'''
    Given a base Plant class and a derived Flower class, write a program to create a list called my_garden
    Store obects that belong to the Plant or Flower class in the list
    Create a function called print_list(), that uses print_info() instance methods defined in the respective
    classes and prints each elemtn in my_garden.
    The program shoudl read plants of flowers from input (ending with -1), add each Plant of Flower to the my_garden
    list, and output each element in my_garden using the print_info() function

'''
class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)
        print('   Annual:', self.is_annual)
        print('   Color of flowers:', self.color_of_flowers)


# TD: Define the print_list() function that prints a list of plant (or flower) objects
def print_list(garden):
    for item in garden:
        item.print_info()
        print()

if __name__ == "__main__":

    # TD: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()

    while user_string != '-1':
        # TD: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        values = user_string.split(' ')
        if values[0] == 'plant':
            plant_name = values[1]
            plant_cost = values[2]
            my_garden.append(Plant(plant_name, plant_cost))
        elif values[0] == 'flower':
            plant_name = values[1]
            plant_cost = values[2]
            is_annual = values[3]
            color_of_flowers = values[4]
            my_garden.append(Flower(plant_name, plant_cost, is_annual, color_of_flowers))

        user_string = input()

    print_list(my_garden)