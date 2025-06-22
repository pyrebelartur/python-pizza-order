print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
if size == "S":
    bill = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        bill+=2
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese == "y":
        bill+=1
    print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese == "y":
        bill+=1
    print(f"Your final bill is: ${bill}.")
elif size == "L":
    bill = 25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese == "y":
        bill+=1
    print(f"Your final bill is: ${bill}.")
else:
    print("Invalid size. Please choose S, M or L.")