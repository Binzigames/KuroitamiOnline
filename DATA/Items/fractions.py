#script to store/create Fractions
#---------------------------------> importing
from enum import Enum
import random as r


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

#---------------------------------> enum політики
class PolicyType(Enum):
    AGGRESSOR = "aggressor"
    DIPLOMAT = "diplomat"
    OPPORTUNIST = "opportunist"
    NEUTRAL = "neutral"

#---------------------------------> fraction class
class Fraction:
    def __init__(self, name, weaponsList, power , Prep, policy: PolicyType = PolicyType.NEUTRAL):
        self.name = name
        self.weaponsList = weaponsList
        self.power = power
        self.Prep = Prep
        self.policy = policy
        self.relations = {}
        self.army = power  # військовий потенціал (може зростати чи падати)
        self.losses = 0    # накопичені втрати

    def create(self):
        FractionsEnum.register(self.name, self)

    # -------------------- ПОЛІТИКА --------------------
    def set_relation(self, other, status: str):
        self.relations[other.name] = status
        other.relations[self.name] = status

    def relation_with(self, other):
        return self.relations.get(other.name, "neutral")

    def declare_war(self, other):
        print(f"{self.name} оголосили війну {other.name}.")
        self.set_relation(other, "war")

    def make_peace(self, other):
        print(f"{self.name} уклали мир з {other.name}.")
        self.set_relation(other, "peace")

    def form_alliance(self, other):
        print(f"{self.name} утворили альянс із {other.name}.")
        self.set_relation(other, "ally")

    def betray(self, other):
        print(f"{self.name} зрадили {other.name}.")
        self.set_relation(other, "enemy")

    # -------------------- АВТО-ПОВЕДІНКА --------------------
    def political_action(self, frac_list):
        targets = [f for f in frac_list if f.name != self.name]

        if self.policy == PolicyType.AGGRESSOR:
            target = r.choice(targets)
            self.declare_war(target)

        elif self.policy == PolicyType.DIPLOMAT:
            target = r.choice(targets)
            if self.relation_with(target) != "ally":
                self.form_alliance(target)

        elif self.policy == PolicyType.OPPORTUNIST:
            weaker = [f for f in targets if f.power < self.power]
            stronger = [f for f in targets if f.power >= self.power]
            if weaker:
                target = r.choice(weaker)
                self.declare_war(target)
            elif stronger:
                target = r.choice(stronger)
                self.form_alliance(target)

        elif self.policy == PolicyType.NEUTRAL:
            print(f"{self.name} залишаються осторонь (нейтралітет).")

    # -------------------- ВІЙСЬКО --------------------
    def train_army(self):
        growth = r.randint(10, 50)
        self.army += growth
        print(f"{self.name} тренують війська (+{growth} сили). Тепер: {self.army}")

    def suffer_losses(self, amount):
        self.losses += amount
        self.army = max(0, self.army - amount)
        print(f"{self.name} втратили {amount} солдатів. (Залишилось: {self.army})")

    def __repr__(self):
        return f"<Fraction {self.name}, army={self.army}, policy={self.policy.value}, relations={self.relations}>"

# ---------------------------------> fractions
Zones_shadows = Fraction("Zones shadows", ["shit", "shit"], 200, 0, PolicyType.DIPLOMAT)
LRR = Fraction("LRR", ["shit", "shit"], 50, 0, PolicyType.NEUTRAL)
Black_border = Fraction("Black_border", ["shit", "shit"], 400, 0, PolicyType.OPPORTUNIST)
Uranis_235 = Fraction("Uranis-235", ["shit", "shit"], 300, 0, PolicyType.AGGRESSOR)

#--------------------------------->create
def load_fractions():
    global Zones_shadows , LRR , Black_border , Uranis_235
    Zones_shadows.create()
    LRR.create()
    Black_border.create()
    Uranis_235.create()

#---------------------------------> fight
def fraction_power(fraction: Fraction, enemy: Fraction) -> int:
    base = fraction.army
    random_bonus = r.randint(-20, 80)

    relation = fraction.relation_with(enemy)
    if relation == "ally":
        base += 30
    elif relation in ["enemy", "war"]:
        base -= 10
    elif relation == "peace":
        base += 10

    return max(0, base + random_bonus)

def fraction_fight(frac1: Fraction, frac2: Fraction) -> Fraction:
    relation = frac1.relation_with(frac2)

    if relation == "ally":
        print(f"{frac1.name} та {frac2.name} — союзники. Вони не воюють.")
        return None
    if relation == "peace":
        print(f"{frac1.name} та {frac2.name} мають мирний договір. Битви немає.")
        return None

    power1 = fraction_power(frac1, frac2)
    power2 = fraction_power(frac2, frac1)

    print(f"{frac1.name} ({power1}) VS {frac2.name} ({power2})")

    if power1 > power2:
        losses = r.randint(20, 60)
        frac2.suffer_losses(losses)
        return frac1
    elif power2 > power1:
        losses = r.randint(20, 60)
        frac1.suffer_losses(losses)
        return frac2
    else:
        print("Нічия! Обидві сторони зазнали втрат.")
        frac1.suffer_losses(r.randint(10, 30))
        frac2.suffer_losses(r.randint(10, 30))
        return None

#---------------------------------> war handler
def war_frac_handle(frac_list):
    cycles = r.randint(5, 10)
    score = {f: 0 for f in frac_list}

    print(f"\nВійна почалась! {cycles} битв!")

    for i in range(cycles):
        side_1, side_2 = r.sample(frac_list, 2)
        print(f"\nРаунд {i+1}:")
        winner = fraction_fight(side_1, side_2)
        if winner:
            score[winner] += 1
            print(f"Переможець: {winner.name}")
        else:
            print("Нічия/союз/мир")

    print("\n=== Підсумки війни ===")
    for frac, pts in score.items():
        print(f"{frac.name}: {pts} перемог, {frac.losses} втрат, {frac.army} армія залишилась")

    winner = max(score, key=score.get)
    print(f"\n>>> Загальний переможець: {winner.name} <<<")

    losers = [f for f, pts in score.items() if pts < score[winner]]
    for loser in losers:
        if loser.relation_with(winner) in ["enemy", "war"]:
            loser.make_peace(winner)

    return winner


if __name__ == "__main__":
    load_fractions()
    frac_list = [Zones_shadows , LRR , Black_border , Uranis_235]

    print("\n=== Політичні дії перед війною ===")
    for f in frac_list:
        f.political_action(frac_list)
        f.train_army()

    print("\n=== Початок війни ===")
    war_frac_handle(frac_list)
