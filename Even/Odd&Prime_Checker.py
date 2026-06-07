def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_even(num):
    print("Even Number")
else:
    print("Odd Number")

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")