import random
x = random.randint(1,6)
word = ""

match x:
    case 1:
        word = "one"
    case 2:
        word = "two"
    case 3:
        word = "three"
    case 4:
        word = "four"
    case 5:
        word = "five"
    case 6:
        word = "six"

print("i have generated the number " + word + " !")