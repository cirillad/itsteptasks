# task1

# from colorama import *

# init()

# def BillGates():
#     print(Fore.LIGHTBLACK_EX + '"Don`t compare yourself with anyone in this world...' + Style.RESET_ALL)
#     print(Fore.LIGHTRED_EX + 'if' + Style.RESET_ALL + ' you' + Fore.LIGHTRED_EX + ' do so' + Style.RESET_ALL + ', you are insulting yourself.' + Fore.LIGHTBLACK_EX + '"' + Style.RESET_ALL )
#     print("Bill Gates")

# BillGates()


# task2

# def EvenNums(a, b):
#     for i in range(a, b):
#         if i % 2 == 0:
#             print(i)

# EvenNums(1, 20)


# task3

# def square(leng, symbol, operation):
#     string = ""
#     if operation == True:
#         for i in range(leng):
#             string +=  symbol + " "
#         for i in range(leng):
#             print(string)
#     if operation == False:
#         for i in range(leng):
#             string += symbol + ' '
#         print(string)
#         for i in range(leng - 2):
#             print( symbol + " " * (leng + (leng - 3)) + symbol)
#         print(string)
        
            

# square(5, "+", False)
# square(5, "+", True)


# task4

# def minimum(a, b, c, d, e):
#     list = [a, b, c, d, e]
#     print(min(list))

# minimum(10, 2, 3, 4, 5)


# task5

# def suma(a, b):
#     count = 0
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         count += i
#     print(count)

# suma(1, 5)


# task6

# def countnums(a):
#     a = str(a)
#     print(len(a))

# countnums(1234)


# task7

def palindrome(a):
    str_a = str(a)
    if str_a == str_a[::-1]:
        print(True)
    else:
        print(False)
    
palindrome(123121)

