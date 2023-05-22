#! /usr/bin/nv python3

# strings as kys and values
phones = {"AND": "Android",
          "BB": "Black Berry",
          "IOS": "iphone X",
          "WIN": "Windows"}
print("Strings as keys and Values")
print(phones)
print()

# numbers as keys and strings as values
print("Numbers as Keys and Strings as Values")
numbers = {5: "Five", 6: "Six", 7: "Seven"}
print(numbers)
print()

# strings as keys, values as mixed types
print("Strings as Keys and Mixed Types as Values")
movie = {"name": "The Princess Bride",
         "year": 1987,
         "price": 9.99}
print(movie)
print()

# Accessing an item by key
print("Accessing an item by Key")
phone = phones["IOS"]
print(phone)
print()

# Updating an item in the dicionary
print("Updating an item in the dictionary")
phones["IOS"] = "iPhone X"
phone = phones["IOS"]
print(phone)
print()

# Testing for a key in the dictionary
print("Testing for a key in the dicionary")
phone = "WIX"
if phone in phones:
    print(phones[phone])
else:
    print(phone, "is not a valid phone key.")
print()

# Dictionary get method
print("Using the dicionary get method")
phone = phones.get("AND")
print(phone)
phone = phones.get("IOX")
print(phone)
phone = phones.get("IOX", "Unkown")
print(phone)
print()

# Deleting a dictionary item
print("Deleting a dicionary item")
print("Starting Count", str(len(phones)))
del phones["WIN"]
print("Count after delete", str(len(phones)))
phone = phones.pop("BB")
print(phone, "was deleted. Count after delete", str(len(phones)))
phones.clear()
print("Count after clear", str(len(phones)))
print()

# Reload the dicionary
phones = {"AND": "Android",
          "BB": "Black Berry",
          "IOS": "iPhone",
          "WIN": "Windows"}
# loop thorugh all items by key
print("Loop through all items by key")
for code in phones.keys():
    print(code, phones[code])
print()

# Alternate loop through all items by key
print("Alternate loop through all items by key")
for code in phones:
    print(code, phones[code])

print()

# loop thorugh all items by item
print("Loop thorugh all items by item")
for code, phone in phones.items():
    print(code, phone)
print()

print("Loop through all values by value")
for phone in phones.values():
    print(phone)

print()

# convert dictionary to list and sort
print("Convert dictionary to list and sort")
codes = list(phones.keys())
codes.sort()
for code in codes:
    print(code, phones[code])

print()

# create dictionary from two-dimensional array
phones = [["BB", "Black Berry"],
          ["WIN", "Windows"],
          ["IOS", "iPhone"],
          ["AND", "Android"]]

print("Convert two dimensional list to dictionary")
# Convert two-dimensional list to dictionary
phones = dict(phones)
print(phones)
print()
print()
phones = {"iPhone": ["6", "6s", "SE", "7", "8", "X"],
          "Android": ["Lollipop", "Marshmellow", "Nougat", "Oreo"],
          "Windows": ["7", "7.5", "7.8", "8", "8.1", "10"],
          "Blackberry": ["1.0", "3.6", "5.0", "6.0", "7.0", "7.1"]}
print("Creating complex dictionary objects")
phones = dict(phones)
print(phones)
                      



