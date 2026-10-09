mark = int(input("Enter your test mark out of 100:"))
if mark > 90:
    print("you got an A")
elif mark >= 80 and mark <= 89:
    print("you got a B")
elif mark >= 70 and mark <= 79:
    print("you got a C")
elif mark >= 60 and mark <= 69:
    print("you got a D")
else:
    print("you failed")