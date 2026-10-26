import random

print("==============================")
print("      🏰 NUMBER QUEST")
print("==============================")

player_name = input("Enter your name, adventurer: ")

print(f"\nWelcome, {player_name}!")
print("You have entered a mysterious cave.")
print("There are three paths in front of you.")
print("\n1. The Dark Forest")
print("2. The Treasure Room")
print("3. The Dragon's Cave")

choice = input("\nChoose your path (1, 2, or 3): ")

if choice == "1":
    print("\nYou entered the Dark Forest!")
    print("You found a mysterious key.")

elif choice == "2":
    print("\nYou entered the Treasure Room!")
    treasure = random.randint(100, 1000)
    print(f"You found {treasure} gold coins!")

elif choice == "3":
    print("\nYou entered the Dragon's Cave!")
    dragon_number = random.randint(1, 5)
    guess = int(input("Guess a number between 1 and 5: "))

    if guess == dragon_number:
        print("Amazing! You escaped the dragon!")
    else:
        print(f"The dragon caught you! The number was {dragon_number}.")

else:
    print("\nInvalid choice! Please select 1, 2, or 3.")

print("\nThanks for playing Number Quest!")