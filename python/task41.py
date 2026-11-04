total = 0
while True:
    num = int(input("Enter a whole number"))
    total = total + num
    if total >= 100:
        break
print(total)