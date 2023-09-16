#functionmachine
def f(x):
  f_x=-2*x+34
  return f_x

y=f(10)
print(y)

def f(x):
  f_x=x/3-10
  return f_x

y=f(3)
print(y)

def f(x):
  f_x=-abs(3*x)
  return f_x

y= f(1)
print(y)

#codingrushcode
def name():
  print("what is your name?")
  variable = input()
  print("would you like me to give you the weather in different scales?",variable)
  print("give me today's weather in celsius!")
  number = input()
  result = int(number)*1.8+32
  print("today's weather expressed in Fahrenheit degrees is",result)
  print("now, remind me of what today's weather is, so i can give you the weather in Kelvin degrees!",variable)
  number = input()
  result = int(number)+273.15
  print("the weather expressed in Kelvin degrees is",result)

name()

#codethatprintshelloworld
print("Hello, world!!")

#2examreview exercises
def promedio():
  print("hello!! i am a grade calculation bot! what is your name?")
  variable = input()
  print("would you like me to calculate the grades")
  print("tell me, what was Mouse's grade in math?")
  math = input()
  print("now, what was Mouse's grade in spanish?")
  spanish = input()
  print("and how was science?")
  science = input()
  print("now, history?")
  history = input()
  print("and programming?")
  programming = input()
  print("lastly, how was french?")
  french = input()
  average = (float(math)+float(spanish)+float(science)+float(history)+float(programming)+float(french))/6
  print("your average is",average)

promedio()


def name():
  print("hello, can i help you calculate the interest of your investments?")
  print("if so, how much have you invested?")
  investment = input()
  print("ok, then what is the annual interest rate?")
  interest = input()
  result = int(interest)/100*int(investment)
  print("here is the interest you would have gained after a year!",result)
  print("would you like to know what you would have earned x years after?")
  number = input()
  result = (int(investment)+int(result))*int(number)
  print("here it would be!",result)

name()

#codefrommymidtermexam
"""partial exam, instuctions: In the laboratory, work is being done on acquiring a new vibration machine. 
The vibration machine costs 20,000. The lab manager wants to know how much the company will have to pay after applying a 10% discount if he decides to buy 
it today. Juan (a robot) has been progremmed to calculate this in case you don't know what to input: 
vibration machine costs 20000 PLEASE DO NOT USE COMMAS. temperature machine = 15000 DO NOT USE COMMAS PLEASE I BEG YOU. 
thermal shock machine = 16500 THANKS HAVE A NICE DAY"""


#STEP1EASYPROBLEM
def machine():
  print("hello!! i am Juan and will calculate the discount on your machine!")
  print("could you tell me the initial cost of the machine?")
  cost = input()
  print("lovely!! with the cost being 20,000, i will now calculate the 10% discount!")
  discount = int(cost)*10/100
  result = int(cost)-int(discount)
  print("here is your result!",result) 

#STEP2EASYPROBLEM
machine()

#STEP1NORMALPROBLEM
def othertwomachines():
  print("oh! i see you want to buy other machines!")
  print("can we start with the price of the thermal machine? let's go :)!!")
  temperature = input()
  print("can we now do the temperature machine's price, please?")
  thermal = input()
  print("i see, the temperature machine's price is 15,000 and the thermal machine is 16,500")
  print("i will now calculate the total price, then i will discount :))")
  total = int(temperature)+int(thermal)
  print("here would be your total WITHOUT a discount!!",total)
  print("now, let's apply the 10% discount to your total!!")
  result = int(total)*10/100
  print("here is the price with the 10%discount applied :D",result)

#STEP2NORMALPROBLEM
othertwomachines()

#STEP1HARDPROBLEM
def moneyexchange():
  print("you want to know how much you paid in dollars AND yens? great!")
  print("assuming that the price before was in pesos, can you tell me what the price was before?")
  price = input()
  dollars = float(price)*0.057
  print("thak you! your price in dollars would be:",dollars)
  print("now yen, right? can you remind me of the original price in pesos, please?")
  price = input()
  yen = float(price)*8.37
  print("wonderful!! your price in yen would be",yen)
  print("have a nice day!! :D")

  
#STEP2HARDPROBLEM
moneyexchange()
