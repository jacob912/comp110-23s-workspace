#Expected code
def mimic(mywords: str) -> str:
    """Given the string my_words, outputs the same string"""
    return mywords

#Calling it
mimic("Hello!") #doesn't work

print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

#any of the last two options