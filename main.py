import random
import string
from collections import Counter

best_score = 0

def guessing_game():
    global best_score
    print("\n--- NUMBER GUESSING GAME ---")
    secret_number = random.randint(1, 100)
    attempt = 0
    max_attempt = 10
    while attempt < max_attempt:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue
            attempt += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                score = 100 - ((attempt - 1) * 10)
                print("Congratulations! You won!")
                print("Attempts:", attempt)
                print("Your score:", score)
                if score > best_score:
                    best_score = score
                break
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Game over!")
        print("The correct number was:", secret_number)
        print("Your score: 0")
    print("Best score:", best_score)

def word_counter():
    print("\n--- WORD COUNTER ---")
    filename = input("Enter file name (sample.txt): ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        word_count = Counter(words)
        print("\nTotal words:", len(words))
        print("Unique words:", len(word_count))
        print("\nTop 10 Most Common Words")
        print("------------------------")
        for word, count in word_count.most_common(10):
            print(word.ljust(15), count)
    except FileNotFoundError:
        print("File not found! Please check the file name.")

while True:
    print("\n===== MAIN MENU =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you for using this program!")
        break
    else:
        print("Invalid choice! Try again.")