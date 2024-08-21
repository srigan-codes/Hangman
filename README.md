# Hangman
A typical hangman game created using python. Users get 6 chances to guess the word when given the topic and number of letters
To  create this game, there were many stages involved. 

First we had to create a list of topics that would fit towards another list of themes. For example Sports was in the master list, but within that master list, we would pick a random sport like Tennis.

Now,  the program would select a random topic from the list, using the random.choice function. Then it would match this topic to a random choice. Then it would convert that choice into a word that can be guessed.
 
Next, the program would initialize the game and UI. This also indicated the beginning of the while loop 'while attempts > 0' that would continue for the rest of the game.

The rest of the loop code displays what happens depending on the user's input. For example if the user got an incorrect guess we would remove it from the 'Letters Remaining' list and append it to the 'Incorrect guesses' list.
