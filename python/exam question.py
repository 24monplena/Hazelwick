people = 0
height = int(input("enter your height in cm:"))
while people < 8:
    if height >= 140:
        print ("you may enter")
        people = people + 1
    elif height < 140 and height >= 120:
        print ("you may ride with an adult")
        people = people + 2
    else:
        print("you may not ride")