"""EX02 - One Shot Wordle"""

__author__ = "730463543"

word: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx_word: int = 0
emoji_string: str = ""
yellow_bool: bool = False
idx_yellow: int = 0


while playing:
    if (len(guess) != len(word)): #if the length of the guess isnt the same as the secret word
        guess = input(f"That was not {len(word)} letters! Try again: ")
    if (len(guess) == len(word) and guess != word): #if the length of the guess is the same as the secret word but they didn't get it right
        print("Not quite. Play again soon!")
        playing = False
    if (guess == word): #if they guessed the right word
        print("Woo! You got it!")
        playing = False

while idx_word < len(word):
    if (guess[idx_word] == word[idx_word]): #if the letter in the guess is the same as the letter of the secret at the same index
        emoji_string = str(emoji_string) + str(GREEN_BOX) #add a green box at that index
    else:
        yellow_bool = False #resetting the bool variable for yellow square test
        idx_yellow = 0 #resetting the index variable for yellow square test
        while yellow_bool == False and idx_yellow < len(word): #while the bool is false and yellow index is less than length of secret word
            if (guess[idx_word] == word[idx_yellow]): #testing if the letter in the guess is the same as any of them in the secret word
                yellow_bool = True #if it is change bool to true
            else:
                idx_yellow = idx_yellow + 1 #if not add 1 to yellow index and restart loop again until we run out of indexes
        if (yellow_bool == True): #if yellow bool is true at this index
            emoji_string = str(emoji_string) + str(YELLOW_BOX) #add a yellow box to emoji string
        else:
            emoji_string = str(emoji_string) + str(WHITE_BOX) #if not add white box
    idx_word = idx_word + 1
print(emoji_string) #print emoji string