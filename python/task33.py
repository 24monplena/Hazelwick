import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)
num4 = random.randint(0,100)
num5 = random.randint(0,100)
answer1 = int(input("i have generated 5 random numbers input your guess"))
answer2 = int(input("i have generated 5 random numbers input your guess"))
answer3 = int(input("i have generated 5 random numbers input your guess"))
answer4 = int(input("i have generated 5 random numbers input your guess"))
answer5 = int(input("i have generated 5 random numbers input your guess"))
score = 0
if num1 == answer1:
    print ("correct")
    score = score + 10
else:
    print("wrong")

if num2 == answer2:
    print ("correct")
    score = score + 10
else:
    print("wrong")

if num3 == answer3:
    print ("correct")
    score = score + 10
else:
    print("wrong")

if num4 == answer4:
    print ("correct")
    score = score + 10
else:
    print("wrong")

if num5 == answer5:
    print ("correct")
    score = score + 10
else:
    print("wrong")

print(score)