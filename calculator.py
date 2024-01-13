def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def divisiond(a, b):
    return a / b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculator():
    a = float(input('Enter the first num: '))
    operation = int(input('Choose the operation: \n 1 --- addition \n 2 --- subtraction \n 3 --- multiplication \n 4 --- division \n 5 --- factorial \n Enter the operation : '))
    if operation in [1, 2, 3, 4]:
        b = float(input('Enter the second num: '))
    else:
        b = None
    
    match operation:
        case 1:
            print(add(a, b))
        case 2:
            print(minus(a, b))
        case 3:
            print(mult(a, b))
        case 4:
            if b != 0:
                print(divisiond(a, b))
            else:
                print("Error! Division by zero.")
        case 5:
            print(factorial(a))
        

calculator()



