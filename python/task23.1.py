print("question 1: what is 56+73")
print("question 2: what is 112-45")
print("question 3: what is 15*8")
print("question 4: what is 84/12")
Q1 = int(input("enter your answer for q1"))
Q2 = int(input("enter your answer for q2"))
Q3 = int(input("enter your answer for q3"))
Q4 = int(input("enter your answer for q4"))
a1 = 56 + 73
a2 = 112 - 45
a3 = 15 * 8
a4 = 84 / 12
correct = 0

if Q1 == a1:
    print("correct")
    correct = correct+1
else:
    print("wrong")
if Q2 == a2:
    print("correct")
    correct = correct+1
else:
    print("wrong")
if Q3 == a3:
    print("correct")
    correct = correct+1
else:
    print("wrong")
if Q4 == a4:
    print("correct")
    correct = correct+1
else:
    print("wrong")

print("score = " + str(correct))