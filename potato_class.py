from crop_class import *

class Potato(Crop):
    """A potato crop"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for potato
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Potato"

    #override the grow method for subclass - polymorphism
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
             #changing the water growth rate based on if there is more water than needed to greater than the original
             #dependant on the status/age of the plant
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            if self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #create a new potato crop
    potato_crop = Potato()
    print(potato_crop.report())
#maunually grow the crop
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()
