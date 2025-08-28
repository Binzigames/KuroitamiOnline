from enum import Enum
import random as r


# ---------------------------------> enum
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

# ---------------------------------> policy enum
class PolicyType(Enum):
    AGGRESSOR = "aggressor"
    DIPLOMAT = "diplomat"
    OPPORTUNIST = "opportunist"
    NEUTRAL = "neutral"

# ---------------------------------> fraction class
class Fraction:
    def __init__(self, name, weapons_list, power, prep, policy: PolicyType = PolicyType.NEUTRAL):
        self.name = name
        self.weapons_list = weapons_list
        self.power = power
        self.prep = prep
        self.policy = policy
        self.army = power
        self.losses = 0

    def create(self):
        FractionsEnum.register(self.name, self)

    # -------------------- ARMY --------------------
    def train_army(self, events):
        growth = r.randint(10, 50)
        self.army += growth
        events.append(f"{self.name} trained their army (+{growth}). Army: {self.army}")

    def suffer_losses(self, amount, events):
        self.losses += amount
        self.army = max(0, self.army - amount)
        events.append(f"{self.name} suffered {amount} losses. Remaining army: {self.army}")

    def __repr__(self):
        return f"<Fraction {self.name}, army={self.army}, policy={self.policy.value}>"

# ---------------------------------> fractions
Zones_shadows = Fraction("Zones shadows", ["basic", "basic"], 200, 0, PolicyType.DIPLOMAT)
LRR = Fraction("LRR", ["basic", "basic"], 50, 0, PolicyType.NEUTRAL)
Black_border = Fraction("Black border", ["basic", "basic"], 400, 0, PolicyType.NEUTRAL)
Uranis_235 = Fraction("Uranis-235", ["basic", "basic"], 300, 0, PolicyType.AGGRESSOR)
Dogs_ruins = Fraction("Dogs of ruins", ["basic", "basic"], 350, 0, PolicyType.OPPORTUNIST)

# ---------------------------------> create
def load_fractions():
    global Zones_shadows, LRR, Black_border, Uranis_235, Dogs_ruins
    Zones_shadows.create()
    LRR.create()
    Black_border.create()
    Uranis_235.create()
    Dogs_ruins.create()

# ---------------------------------> fight
def fraction_power(fraction: Fraction) -> int:
    base = fraction.army
    random_bonus = r.randint(-20, 80)
    return max(0, base + random_bonus)

def fraction_fight(frac1: Fraction, frac2: Fraction, events) -> Fraction:
    power1 = fraction_power(frac1)
    power2 = fraction_power(frac2)

    events.append(f"{frac1.name} ({power1}) vs {frac2.name} ({power2})")

    if power1 > power2:
        losses = r.randint(20, 60)
        frac2.suffer_losses(losses, events)
        events.append(f"Winner: {frac1.name}")
        return frac1
    elif power2 > power1:
        losses = r.randint(20, 60)
        frac1.suffer_losses(losses, events)
        events.append(f"Winner: {frac2.name}")
        return frac2
    else:
        events.append("Draw! Both sides suffered losses.")
        frac1.suffer_losses(r.randint(10, 30), events)
        frac2.suffer_losses(r.randint(10, 30), events)
        return None

# ---------------------------------> game loop
def fraction_tick(frac_list, tick_num):
    events = []
    events.append(f"=== Tick {tick_num} ===")

    # army growth
    for f in frac_list:
        f.train_army(events)

    # random battle
    if r.random() < 0.5:
        side_1, side_2 = r.sample(frac_list, 2)
        events.append(f"Random battle between {side_1.name} and {side_2.name}:")
        fraction_fight(side_1, side_2, events)

    # economy
    for f in frac_list:
        income = r.randint(50, 150)
        f.prep += income
        events.append(f"{f.name} received {income} resources. Total: {f.prep}")

    # world status
    events.append("=== World status ===")
    for f in frac_list:
        events.append(f"- {f.name}: army={f.army}, resources={f.prep}, policy={f.policy.value}")

    return events


if __name__ == "__main__":
    load_fractions()
    frac_list = [Zones_shadows, LRR, Black_border, Uranis_235, Dogs_ruins]

    tick = 1
    while True:
        events = fraction_tick(frac_list, tick)
        for e in events:
            print(e)
        tick += 1
        cmd = input("\nPress Enter for next tick, or 'exit' to quit: ")
        if cmd.lower() == "exit":
            break
