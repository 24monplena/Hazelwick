s1 = float(input("Enter one side length of the triangle"))
s2 = float(input("Enter one side length of the triangle"))
s3 = float(input("Enter one side length of the triangle"))
if s1 == s2 == s3:
    print("the triangle is equilateral")
elif s1 == s2 != s3 or s1 != s2 == s3 or s1 == s3 != s2:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")