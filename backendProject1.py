import random

def guess_number(n, m, max_attempts):
    target_number = random.randint(n, m)
    
    print(f"Guess a number between {n} and {m}.")
    
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
        
        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempt} attempts!")
            return
    
    print(f"Sorry, you didn't guess the number {target_number}. It was {target_number}.")

def main():
    n = int(input("Enter the minimum number: "))
    m = int(input("Enter the maximum number: "))
    max_attempts = int(input("Enter the maximum number of attempts: "))
    
    if n > m:
        print("Error: The minimum number must be less than or equal to the maximum number.")
        return
    
    guess_number(n, m, max_attempts)

if __name__ == "__main__":
    main()
