import  random

easy_words = ["apple", "train", "tiger", "money", "india"]
Medium_words = ["python", "botton", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbtralla", "computer", "mountain"]

print("Welcome to the password gussing game")
print("choose a difficult level: easy, medium or hard")

level = input('enter difficulty:').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "Medium_words":
    secret = random.choice(Medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice.Deaulting to easy leve")
    secret = random.choice(easy_words)

attempts = 0 
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! you guessed it in {attempts} attempts.')
        break
    hint = ""
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint = "-"

        print("Hint:", hint)
    print("Game over")         
