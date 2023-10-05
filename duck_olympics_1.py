#FIRST ROUND
#addition and substraction
def addition(a,b):
  x = a + b
  return x

def substraction(a,b):
  x = a - b
  return x

print("give me the first number")
a = int(input())
print("give me the second number:")
b = int(input())
print(f"the addition is {addition(a,b)} and the substraction is {substraction(a,b)}")

#multiplication and division
def multiplication(a,b):
  x = a * b
  return x

def division(a,b):
  x = a/b
  return x

print("give me the first number")
a = int(input())
print("now the second number")
b = int(input())
print(f"the multiplication is {multiplication(a,b)} and the division is {division(a,b)}. Vavoom.")

#SECOND ROUND
#unit conversion
def conversion():
  meters = kilometers*100
  return meters

print("hello, can you give me the distance from point a to point b in km?")
kilometers = int(input())
print(f"the distance in meters is {conversion()}")

#ROUND THREE
#triangle area
def triangle_area(base, height):
  area = (base*height)/2
  return area

print("hello!! can you tell me the length of the base of this triangle?")
base = int(input())
print("now, can you tell me the length of the height?")
height = int(input())
print(f"the triangle area is {triangle_area(base, height)}. Wahoo.")
