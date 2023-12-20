import random

random_number = random.randint(1,1000)
if random_number%2==0:
    print(f"{random_number} is a even number")
else:
    print(f"{random_number} is a odd number")