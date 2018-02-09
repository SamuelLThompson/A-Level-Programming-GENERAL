class character:
    """This is the parent class character"""

    def __init__(self, name, hp, stre, deff):
        self. name = str(name)
        try:
            self.hp = int(hp)
            self.stre = int(stre)
            self.deff = int(deff)
        except:
            print("invalid attributes")

    def attack(self, char):

        dmg = ((self.stre) - (char.deff/2))

        char.hp -= dmg

        print(self.name, "damaged", char.name, "for", dmg, "points.")


# DEFINING MAGE SUBCLASS -----------------------------------------------------------------------------------------------

class mage(character):
    """subclass of character"""

    def __init__(self, name, hp, stre, deff, m_atk, m_def):
        character.__init__(self, name, hp, stre, deff)
        self.m_atk = int(m_atk)
        self.m_def = int(m_def)


    def attack(self, char):
        try:
            dmg = (self.m_atk - (char.m_def/2))

        except:
            dmg = (self.m_atk)*2

        char.hp = char.hp - dmg

        print(self.name, "cast a fireball and damaged", char.name, "for", dmg, "points.")



# EXAMPLES OF RUNNING THE CODE -----------------------------------------------------------------------------------------

player = character("Julian", 100, 40, 60)
alex = character("Alex", 100, 70, 30)

player.attack(alex)
alex.attack(player)

barry = mage("Barry", 100, 50, 50, 60, 40)

barry.attack(alex)
barry.attack(player)

khadgar = mage("Khadgar", 200, 60, 40, 30, 70)

khadgar.attack(alex)
khadgar.attack(barry)
