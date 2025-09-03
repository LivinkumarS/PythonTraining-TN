# try:
#     b="Two"+2
#     print(b)
#     a=5/0
#     print(a)
# except ZeroDivisionError:
#     print("You cannot divide a number by 0")
# except TypeError:
#     print("Cannot concat a str with int")
    
    
while True:
    try:
        inp = int(input("Enter a number: "))
        if(inp%2==0):
            print("Even")
        else:
            print("Odd")
        
    except ValueError:
        print("Please enter valid number!")
    
    finally:
        print("Calculation completed!")

