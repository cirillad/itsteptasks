# task1
#
# first_num = int(input('Enter first number : '))
# second_num = int(input('Enter second number : '))
# third_num = int(input('Enter third number : '))
#
# first_num = str(first_num)
# second_num = str(second_num)
# third_num = str(third_num)
#
# result = str(first_num + second_num + third_num)
# print(f'Result : {result}')
#
# task2
#
# number = input('Введіть чотиризначне число: ')
#
# if len(number) != 4:
#     print('Введіть чотиризначне число і спробуйте знову :')
# else:
#     product = 1
#     for digit in number:
#         product = product * int(digit)
#     print(f'Результат : {product}')
#
# task3
#
# meters = float(input('Enter the number of meters: '))
#
# centimeters = meters * 100
# decimeters = meters * 10
# millimeters = meters * 1000
# miles = meters / 1609.34
#
# print(f'{centimeters} centimeters in {meters} meters')
# print(f'{decimeters} decimeters in {meters} meters')
# print(f'{millimeters} millimeters in {meters} meters')
# print(f'{miles:.6f} miles in {meters} meters')

# task4

# base_of_a_triangle = int(input('Enter the base of triangle : '))
# height_of_a_triangle = int(input('Enter the height of triangle : '))
# result = base_of_a_triangle * height_of_a_triangle / 2
# print(f'The area of triangle : {result}')

# task5

number = input('Введіть чотиризначне число: ')

if len(number) != 4 or not number.isdigit():
    print('Введіть коректне чотиризначне число і спробуйте знову.')
else:
    result = number[::-1]
    print(f'Результат: {result}')
