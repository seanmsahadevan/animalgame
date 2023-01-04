print("Welcome to my game!")
secret_word = "horse"
guess =input("Guess what animal im thinking of").lower()

while guess != secret_word:
    print("Nope")
    guess = input("Guess what animal im thinking of").lower()
else:
    print("You win!")