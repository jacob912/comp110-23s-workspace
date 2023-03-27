"""Practice with dictionaries"""

ice_cream: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}  #can use single or double quotes
print(len(ice_cream))
#Adding
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#Removing
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")  #have to use single quotes for f strings

#Updating a value
ice_cream["vanilla"] += 1
print("After adding 1 Vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")  #have to use single quotes for f strings

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)