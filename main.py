import random  # Import the random module to generate random numbers

# Define a class named Character to represent a character in the game
class Character:
    # Initialize the character with a name, health, energy, experience, and level
    def __init__(self, name, health=100, energy=100, experience=0, level=1):
        self.name = name
        self.health = health
        self.energy = energy
        self.experience = experience
        self.level = level

    # Define a method for the hero's attack
    def hero_attack(self, target):
        if self.energy >= 5:  # Check if the hero has enough energy to attack
            self.energy -= 5  # Reduce the hero's energy by 5
            self.experience += 1  # Increase the hero's experience by 1
            if self.experience % 5 == 0:  # Check if the experience is a multiple of 5
                self.level += 1  # Increase the hero's level by 1
                print(f"The Python Hero leveled up to level {self.level}!")
            target.health -= 10  # Reduce the target's health by 10
            print(f"{self.name} attacked {target.name} for 10 damage!")
        else:
            print(f"{self.name} doesn't have enough energy to attack!")

    # Define a method for the monster's attack
    def monster_attack(self, target):
        if self.energy >= 10:  # Check if the monster has enough energy to attack
            self.energy -= 10  # Reduce the monster's energy by 10
            target.health -= 15  # Reduce the target's health by 15
            print(f"{self.name} attacked {target.name} for 15 damage!")
        else:
            print(f"{self.name} doesn't have enough energy to attack!")

# Define the gameplay function to handle the game logic
def gameplay():
    # Create a Python hero object
    hero = Character(name="Python Hero", experience=0, level=1)
    
    # Create a Java monster object
    monster = Character(name="Java Monster", experience=10, level=3)

    while True:
        # Print hero’s stats and monster’s stats
        print(f"\nPython Hero's stats: Health = {hero.health}, Energy = {hero.energy}, Experience = {hero.experience}, Level = {hero.level}")
        print(f"Java Monster's stats: Health = {monster.health}, Energy = {monster.energy}, Experience = {monster.experience}, Level = {monster.level}")

        # At 0 health points or lower, hero dies
        if hero.health <= 0:
            print(f"{hero.name} has died. Game over!")
            break

        # Display options to the player
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter your choice (1 or 2): ")

        # Handle the player's choice
        if choice == "1":
            # Hero attacks the monster
            print("The Python Hero attacks the Java Monster!")
            hero.hero_attack(monster)

            # Monster attacks the hero if it's still alive
            if monster.health > 0:
                print("The Java Monster attacks the Python Hero!")
                monster.monster_attack(hero)

            # Randomness - Hero blocks attack
            if random.randint(1, 10) <= 3:
                print("The Python Hero blocked the Java Monster's attack!")
                monster.energy -= 5

            # Randomness - Monster blocks attack
            elif random.randint(1, 10) <= 3:
                print("The Java Monster blocked the Python Hero's attack!")
                hero.energy -= 2

            # At 20 health points, set a warning for player
            if hero.health <= 20:
                print("Warning: Your health is very low!")

        elif choice == "2":
            # If hero decides to run, exit the game
            print("The Python Hero ran away!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        # If hero kills monster, hero gets 10 experience points
        if monster.health <= 0:
            print(f"{monster.name} has been defeated. You win!")
            hero.experience += 10
            # Each time hero accumulates 5 experience points, hero levels up
            if hero.experience % 5 == 0:
                hero.level += 1
                print(f"The Python Hero leveled up to level {hero.level}!")
            # Each time the hero kills monster, game asks if player wants to play again
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                hero = Character(name="Python Hero", experience=hero.experience, level=hero.level)
                monster = Character(name="Java Monster", experience=10, level=3)
            else:
                print("Thanks for playing!")
                break

        # If hero or monster dies, end the game
        if hero.health <= 0 or monster.health <= 0:
            if hero.health <= 0:
                print("The Python Hero has been defeated.")
            else:
                print("The Python Hero has defeated the Java Monster!")
                hero.experience += 10
                if hero.experience % 5 == 0:
                    hero.level += 1
                    print(f"The Python Hero leveled up to level {hero.level}!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                break
            else:
                hero = Character(name="Python Hero", experience=hero.experience, level=hero.level)
                monster = Character(name="Java Monster", experience=10, level=3)

# Run the gameplay function if this script is executed
if __name__ == "__main__":
    gameplay()
