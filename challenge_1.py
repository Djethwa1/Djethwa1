'''Request use to input length of llsides of a triangle,
use these values to calculate the area of the triangle'''
a=input("What is the length of side one of the triangle:")
b=input("What is the length of side two of the triangle:")
c=input("What is the length of side three of the triangle:")
print("side 1 =", a)
print("side 2 =", b)
print("side 3 =", c)
side_1=(int(a))
side_2=(int(b))
side_3=(int(c))
s=(side_1 + side_2 + side_3)/2
print("s=" , s)
t=(s*s - s*a) *(s-b)*(s-c)
area=s.isqrt(t)