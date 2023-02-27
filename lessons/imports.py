"""Practice importing from other modules"""

#from lessons import my_functions
from lessons.my_functions import addition  #(import just addition function)

if __name__ == "__main__":
    print("Howdy!")

print(addition(1,2))