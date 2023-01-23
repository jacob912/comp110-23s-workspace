"""Knock Knock joke with conditionals"""

inter_cow: str = input("Do you want an interrupting cow?")

print("Knock Knock")
if (inter_cow == "yes"):
    print("... who's there?")
    print("Interrupting cow.")
    print("...interrupting cow wh---")
    print("MOO!!!")
else:
    print("Oh... okay... :(")
    if (inter_cow == "you're not funny"):
        print("that's not cool")