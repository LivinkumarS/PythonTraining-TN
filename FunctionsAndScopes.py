# def printSteps(a,b):
#     return a+b

# printSteps(30,40)
# printSteps(40,60)
# printSteps("40","60")

# printSteps(45,30)
# printSteps(b=10,a=70)
# printSteps(30)


# print(printSteps(printSteps(10,40),80))


# def calcBMI(weight,height):
#     return (weight/(height**2))

# print(calcBMI(73,1.79))

# def odd_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(odd_even(90))


name="Parthiban"

def sayHi():
    name="Leo"
    print(f"The name is {name}. From inside the Function1!")

def sayHello():
    print(f"The name is {name}. From inside the Function2!")

sayHi()
sayHello()