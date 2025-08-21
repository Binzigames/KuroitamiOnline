# -------------> imports
import DATA.CORE.storage as s

# -------------> Character class
class Character:
    def __init__(self):

        # Strength:
        # - Carrying weight
        # - Melee combat
        self._strength = 1

        # Agility:
        # - Shooting accuracy
        # - Movement speed
        self._agility = 1

        # Intelligence:
        # - Weapon and equipment repair
        # - Data decryption
        self._intelligence = 1

        # Charisma:
        # - Trading
        # - Interaction with factions
        self._charisma = 1

        # Endurance:
        # - Resistance to radiation/fatigue
        self._endurance = 1

        # Luck:
        # - Chance of finding useful items
        # - Random beneficial events
        self._luck = 1

        # Save initial state to storage
        self.save()

# -------------> Property Getters/Setters with validation for Character attributes
    def _validate_stat(self, value: int) -> int:
        # Ensure that attribute value stays between 0 and 10.
        return max(0, min(10, value))

    @property
    def strength(self): return self._strength

    @strength.setter
    def strength(self, value): self._strength = self._validate_stat(value)

    @property
    def agility(self): return self._agility

    @agility.setter
    def agility(self, value): self._agility = self._validate_stat(value)

    @property
    def intelligence(self): return self._intelligence

    @intelligence.setter
    def intelligence(self, value): self._intelligence = self._validate_stat(value)

    @property
    def charisma(self): return self._charisma

    @charisma.setter
    def charisma(self, value): self._charisma = self._validate_stat(value)

    @property
    def endurance(self): return self._endurance

    @endurance.setter
    def endurance(self, value): self._endurance = self._validate_stat(value)

    @property
    def luck(self): return self._luck

    @luck.setter
    def luck(self, value): self._luck = self._validate_stat(value)

# -------------> Storage interaction
    def to_dict(self):
        # Convert character attributes into a dictionary
        return {
            "strength": self.strength,
            "agility": self.agility,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
            "endurance": self.endurance,
            "luck": self.luck
        }

    def save(self):
        # Save character data into storage.py
        s.P_ATTRIBUTES = self.to_dict()

    def load(self):
        # Load character data from storage.py
        if s.P_ATTRIBUTES:
            data = s.P_ATTRIBUTES
            self.strength = data["strength"]
            self.agility = data["agility"]
            self.intelligence = data["intelligence"]
            self.charisma = data["charisma"]
            self.endurance = data["endurance"]
            self.luck = data["luck"]
