a = 5
b = 6
c = 7
# calculate the semi-perimeter
s = (a + b + c) 

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is with sides as (%2d, %2d, %2d) is %0.2f' %a %b %c %area)