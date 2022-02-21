import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
lettersUsed = 0
symbolsUsed = 0
numbersUsed = 0
password = ""

for character in range(0, nr_letters + nr_numbers + nr_symbols):
    choice = random.randint(0, 2)
    if choice == 0 and lettersUsed < nr_letters:
        rand = random.randint(0, len(letters) - 1)
        password += letters[rand]
    elif choice == 1 and symbolsUsed < nr_symbols:
        rand = random.randint(0, len(symbols) - 1)
        password += symbols[rand]
    elif choice == 2 and numbersUsed < nr_numbers:
        rand = random.randint(0, len(numbers) - 1)
        password += numbers[rand]
print(f"Your password is {password}")
