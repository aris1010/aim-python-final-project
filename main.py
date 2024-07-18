import random
class Character:
    def __init__(self, name, health=100, energy=100, experience=0, level=1):
        self.name = name
        self.health = health
        self.energy = energy
        self.experience = experience
        self.level = level
    def hero_attack (sel, target) :
        if self.energy >=5:
            self.energy -= 5
            self.experience += 1
            if self.experience % 5 == 0 :
                sel.level += 1
            damage = 10
            if random-random () < 0.2:
                target.energy -=5
                damage = 0
                print (f"{target.name} blocked the attack and lost 5 energy!")
            target.health -= damage
            print(f"{self.name} doesn't have enough energy to attack!")
