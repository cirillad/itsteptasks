# task1
#
# first_num = float(input('Enter the first number : '))
# second_num = float(input('Enter the second number : '))
# third_num = float(input('Enter the third number : '))
# operation = input('Enter the operation you want : ')
#
# match operation:
#     case '+': print(first_num + second_num + third_num)
#     case '*': print(first_num * second_num * third_num)


# task2
#
# first_num = float(input('Enter the first number : '))
# second_num = float(input('Enter the second number : '))
# third_num = float(input('Enter the third number : '))
# operation = input('Enter the operation you want : ')
#
# match operation:
#     case 'min': print(min(first_num, second_num, third_num))
#     case 'max': print(max(first_num, second_num, third_num))
#     case 'avg': print((first_num + second_num + third_num) / 3)
#
# task3

meters = float(input('Enter amount of meters : '))
operation = input('Enter the operation you want : ')

match operation:
    case 'miles': print(meters * 0.000621371)
    case 'inches': print(meters * 39.3701)
    case 'yards': print(meters * 1.09361)

