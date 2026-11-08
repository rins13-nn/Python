import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum attempts
attempts = 3

while attempts > 0:
    try:
        guess = int(input("Guess the number (between 1 and 10): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check if guess is within range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

    attempts -= 1
    print("Attempts left:", attempts)

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

    # Multiplication Table Generator

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

    # BMI Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is:", round(bmi, 2))