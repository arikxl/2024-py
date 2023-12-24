def countEven(x):
    count = 0
    for num in range(1, x+1):
        if num % 2 == 0:
            count += 1
            print(num)

    print(f"the number of even numbers is {count}")
# countEven(100)


def findRoot(x):
    for num in range(1, x):
        if num*num == x:
            print(f"the root of {x} is {num}")


# findRoot(100)


def findMaxMin():
    nums = [1,34,435,435,4634542,6457,6765,434,646,54754,534]
    print(f"The max number is {max(nums)}")
    print(f"The min number is {min(nums)}")

# findMaxMin()
    

def isItPrime(x):
    count =0
    for num in range(2, x):
        if x%num==0:
            count+=1
        
    if count==0:
        print(f"{x} is a prime number")
    else:
        print(f"{x} is not a prime number")

# isItPrime(19)