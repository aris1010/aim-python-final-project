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
def gameplay () :
    hero = Character (name = "Python Hero", experince=0, level=1)
    monster = Character(name="Java Monster", experience=10, level=3)
    while True:
        print(f"\n{hero.name} stats: Health = {hero.health}, Energy = {hero.energy}, Experience = {hero.experience}, Level = {hero.level}")
        print(f"{monster.name} stats: Health = {monster.health}, Energy = {monster.energy}, Experience = {monster.experience}, Level = {monster.level}")
        if hero.health <= 0 :
            print (f"{hero.name} has died. The Game is Over!")
            break
        if monster.health <= 0 or monster.health <= 10 or monster.energy <= 10 :
            print (f"{monster.name} has been defeated or retreated. You win!")
            hero.experience += 10
            if hero.experience % 5 == 0:
                hero.level += 1
            play_again = input ("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                hero = Character (name="Java Monster", experience=hero.experience, level=hero.level)
                monster = Character(name="Java Monster", experience=10, level=3)
            else:
                print("Thank you for playing!")
                break
        print("\nOptions: 1. Attack 2. Run")
        choice = input ("Choose your action: ")
        if choice == "1":
            hero.hero_attack(monster)
            if monster.monster > 0:
                monster.monster_attack(hero)
            if hero.health <=20:
                print ("Warning: Your health is very low!")
        elif choice == "2" :
            print("You chose to run away. The Game is over !")
            break
        else:
            print("Invalid choice. Please choose again.")
if __name__ == "__main__":
    gameplay