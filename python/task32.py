num = int(input("Enter a whole number"))

if num % 3 == 0:
    print("the number is divisible by 3")
    if num % 5 == 0:
        print("the number is divisible by 5")
    elif num % 7 == 0:
        print("the number is divisible by 7")
elif num % 5 == 0:
    print("the number is divisible by 5 by but not 3 or 7")
    if num % 5 == 0:
            print("the number is divisible by 5")
    elif num % 7 == 0:
            print("the number is divisible by 7")
elif num % 7 == 0:
    print("the number is divisible by 7 by but not 3 or 5")
    if num % 5 == 0:
            print("the number is divisible by 5")
    elif num % 7 == 0:
            print("the number is divisible by 7")
else:
    print("the number is not divisible by 3,5 or 7")
