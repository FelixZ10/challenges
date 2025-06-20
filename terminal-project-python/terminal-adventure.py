import random

# Initial Life
player_hp = 100
player_cash = 0
player_level = 1
enemy_hp = 100

# Start of the Game
print("Welcome to the Terminal Adventure Game 🧙‍♂️")
print("You found a monster in the woods, thirsty for blood...")

# Initial Fight
while player_hp > 0 and enemy_hp > 0:
    print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
    print("1. Attack")
    print("2. Heal")
    print("3. Run")

    choice = input("Choose an action: ")

    if choice == "1":
        damage = random.randint(10, 30)
        enemy_hp -= damage
        print(f"\nYou attacked the monster and dealt {damage} damage!")
    
    elif choice == "2":
        heal = random.randint(5, 20)
        player_hp += heal
        if player_hp > 100:
            player_hp = 100
        print(f"\nYou healed yourself for {heal} HP!")
    
    elif choice == "3":
        print("\nYou ran away safely!")
        break

    else:
        print("\nInvalid choice, please try again.")
        continue

    if enemy_hp > 0:
        enemy_damage = random.randint(5, 25)
        player_hp -= enemy_damage
        print(f"The monster attacked you and dealt {enemy_damage} damage!")

# End of The Game
if player_hp <= 0:
    print("\nYou have been defeated by the monster... Game Over 💀")
elif enemy_hp <= 0:
    print("\nYou defeated the monster!")
    player_cash += 50
    player_level += 1
    print(f"You earned 50 gold! Total cash: {player_cash}")
    print(f"You leveled up! Current Level: {player_level}")
    print("Congratulations! You survived the adventure! Great job, Knight 🏆")
