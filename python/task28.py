temp = int(input("Enter the temperature in degrees celsius"))
if temp <= 0:
    print("its freezing!")
elif temp > 0 and temp <= 20:
    print("its cold")
elif temp > 21 and temp <= 30:
    print("its warm")
else:
    print("its hot")