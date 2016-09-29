import random

from potato_class import *
from wheat_class import *

class Field:
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self, max_crops):
        self._crops = []
        self._max_crops = max_crops

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
    def harvest_crop(self, position):
        return self._crops.pop(position)

    def report_contents(self):
        crop_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        return {"crops": crop_report}

    def report_needs(self):
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        return {"light": light, "water": water}

    def grow(self,light, water):
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light, water)

def auto_grow(field, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        field.grow(light, water)

def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered is not valid - enter a new one")
        except ValueError:
            print("Value entered is not valid - enter a new one")

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a light value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is not valid - enter a new one")
        except ValueError:
            print("Value entered is not valid - enter a new one")

    field.grow(light,water)

def display_crops(crop_list):
    print()
    print("The following crops are in this field")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos, crop.report()))

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1, length_list + 1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def display_crop_menu():
    print()
    print("Which crop would you like to add?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. I don't want to add a crop - return to main menu")
    print()
    print("Please select an option from the above menu")

def display_main_menu():
    print()
    print("1. Plants a new crop")
    print("2. Harvest a crop")
    print()
    print("3. Grow field manually over 1 day")
    print("4. Grow field automatically over 30 days")
    print()
    print("5. Report field status")
    print()
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - wheat not planted")
            print()

def manage_field(field):
    print("This is the field management program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,5)
        print()
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print("You removed the crop: {0}". format(removed.crop))
        elif option == 3:
            manual_grow(field)
        elif option == 4:
            auto_grow(field,30)
        elif option == 5:
            print(field.report_contents())
            print()
        elif option == 0:
            exit = True
            print()
    print("Thank you for using the field management program")



def main():
    new_field = Field(6)
    manage_field(new_field)
 #   print(new_field._crops)
 #   print(new_field._max_crops)
 #   new_field.plant_crop(Wheat())
 #   new_field.plant_crop(Potato())
 #   report = new_field.report_contents()
 #   print(report["crops"])
 #   report = new_field.report_needs()
 #   manual_grow(new_field)
 #   print(new_field.report_contents())
 #   auto_grow(new_field, 30)
 #   print(new_field.report_contents())

if __name__ == "__main__":
    main()
