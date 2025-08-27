#script to store/create Fractions
#---------------------------------> importing
from enum import Enum

#---------------------------------> enum
class FractionsEnum(Enum):
    PLACEHOLDER = "placeholder"

    @classmethod
    def register(cls, name: str, fraction_obj):
        FRACTION_REGISTRY[name] = fraction_obj

    @classmethod
    def get(cls, name: str):
        return FRACTION_REGISTRY.get(name)

    @classmethod
    def all(cls):
        return FRACTION_REGISTRY


FRACTION_REGISTRY = {}


#---------------------------------> fraction class
class Fraction:
    def __init__(self, name, weaponsList, power , Prep):
        self.name = name
        self.weaponsList = weaponsList
        self.power = power
        self.Prep = Prep

    def create(self):
        FractionsEnum.register(self.name, self)


    def __repr__(self):
        return f"<Fraction {self.name}, power={self.power}, weapons={self.weaponsList}>"

#---------------------------------> bools
#> player rep
PrepZS = 0
PrepLRR = 0
PrepBB = 0
PrepU235 = 0

#>fractions bools
Zones_shadows =  Fraction("Zones shadows" , ["shit" , "shit"] , 200 , PrepZS)
LRR = Fraction("LRR" , ["shit" , "shit"] , 50 , PrepLRR)
Black_border = Fraction("Black_border" , ["shit" , "shit"] , 400 , PrepBB)
Uranis_235 = Fraction("Uranis-235", ["shit" , "shit"], 300, PrepU235)
#---------------------------------> Handler

#> create
def load_fractions():
    global Zones_shadows , LRR , Black_border , Uranis_235
    Zones_shadows.create()
    LRR.create()
    Black_border.create()
    Uranis_235.create()
