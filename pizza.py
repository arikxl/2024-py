personal_pizza = 20
family_pizza = 27
huge_pizza = 35

extra_cheese = 3
bulgarit_small = 5
bulgarit_big = 8

drink = 9

print("Welcome to Arik's Pizza!🍕")
size = input("What size pizza do you want? P, F, H? ").lower()
bulgarit = input("Do you want Bulgarit on your pizza? Y or N ? ")
cheese = input("Do you want extra cheese? Y or N? ")
drinks = int(input("How many drinks do you want? "))

bill = 0

if size == 'p':
    bill += 20
elif size == 'f':
    bill += 27
else:
    bill += 35

if cheese == 'y':
    bill += 3

if bulgarit == 'y':
    if size == 'p':
        bill += 5
    else:
        bill += 8

drink_pay = drinks*9

bill += drink_pay

print(f"Your bill is ${bill}")
# https://www.youtube.com/watch?v=Z158ddgJ7S0&list=PLSzsOkUDsvdvGZ2fXGizY_Iz9j8-ZlLqh&index=33