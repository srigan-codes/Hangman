import random

# Lists of words
food = ["pizza", "pasta", "burger", "fries", "chicken", "steak", "sandwich", "salad", "tacos", "burrito"]
places = ["school", "hospital", "store", "park", "restaurant", "cafe", "mall", "movie theater"]
sports = ["basketball", "soccer", "baseball", "football", "tennis", "hockey", "swimming", "volleyball", "golf", "frisbee"]
subjects = ["math", "physics", "chemistry", "biology", "english", "history", "geography", "computer science", "physical education"]
animals = ["dog", "cat", "bird", "fish", "lion", "tiger", "elephant", "giraffe", "zebra", "horse"]
countries = ["united states", "canada", "mexico", "brazil", "australia", "china", "japan", "india", "south korea", "france"]
jobs = ["doctor", "lawyer", "teacher", "engineer", "scientist", "nurse", "accountant", "artist", "musician", "actor"]
tvshows = ["friends", "the big bang theory", "the office", "family guy", "scooby doo", "the good place", "the walking dead", "the flash", "brooklyn nine-nine", "rick and morty"]
movies = ["the matrix", "kung fu panda", "the lion king", "the hunger games", "the amazing spider-man", "the avengers", "the lion king live action version"]
brands = ["nike", "adidas", "puma", "new balance", "under armour", "vans", "converse", "reebok", "gucci", "louis vuitton"]

# Master list of arrays
masterTopics = [food, places, sports, subjects, animals, jobs, countries, tvshows, movies, brands]

# Names of all the topics
topics = ["Food", "Places", "Sports", "Subjects", "Animals", "Jobs", "Countries", "TV Shows", "Movies", "Brands"]

# Chooses a random topic from the topics list
topic = random.choice(topics)

# Finds the index of the chosen topic in the topics list
index = topics.index(topic)

# Finds the corresponding list of words by matching the index to the master topic list
words = masterTopics[index]

# Chooses a random word from the list
word = random.choice(words)

# Creates a list with underscores to represent the word
wordprog = ['_' if char != ' ' else ' ' for char in word]

# Empty array for the incorrect guesses (fills up as you get wrong letters)
incorrect = []

attempts = 6
letters = list("abcdefghijklmnopqrstuvwxyz")

# Intro and format
print("{:^60}".format("WELCOME TO HANGMAN! \n"))
print("=" * 69)
print('Topic: {:>60}'.format(topic))
print("Word: {:>60}".format(" ".join(wordprog)))
print("Lives: {:>60}".format(attempts))

while attempts > 0:
    guess = input("Enter a letter (Press ! to guess the word): ").lower()

    # Checks if the user wants to guess the word
    if guess == "!":
        if input("Enter your guess: ").lower() == word:
            print("You guessed the word!")
            break
        else:
            print("Incorrect guess!")
            attempts = 0
            continue

    # Checks if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Checks if the letter has already been guessed
    if guess in incorrect or guess in wordprog:
        print('The letter', guess, 'is already used, please try again.')
        continue

    # Checks if the guess is in the word
    if guess in word:
        for i, char in enumerate(word):
            if char == guess:
                wordprog[i] = guess
        print("Good guess!\n")
    else:
        # Adds incorrect guess to the incorrect array
        incorrect.append(guess)
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
        print("Incorrect guesses: ", " ".join(incorrect))

    # Updates the game status
    print('-' * 12)
    print('Topic: {:>60}'.format(topic))
    print("Word: {:>60}".format(" ".join(wordprog)))
    print('Letters Remaining:', " ".join(letters))
    print("Lives: {:>60}".format(attempts))

    # Checks if the user has won
    if '_' not in wordprog:
        print("Congratulations, you won! The word is: ", word)
        break

# If the person ran out of lives, tell them the word, and ask to play again
if attempts == 0:
    print("You lose! The word was: ", word)

playAgain = input("Would you like to play again? (y/n): ").lower()

# If the person wants to play again
if playAgain == 'y':
    # Reset the game
    attempts = 6
    incorrect = []
    letters = list("abcdefghijklmnopqrstuvwxyz")
    topic = random.choice(topics)
    index = topics.index(topic)
    words = masterTopics[index]
    word = random.choice(words)
    wordprog = ['_' if char != ' ' else ' ' for char in word]

    # Replay game
    print("{:^60}".format("WELCOME TO HANGMAN! \n"))
    print("=" * 69)
    print('Topic: {:>60}'.format(topic))
    print("Word: {:>60}".format(" ".join(wordprog)))
    print("Lives: {:>60}".format(attempts))
else:
    print("Thanks for playing!")
