# task1
#
# num_of_day = int(input('Enter the number of day : '))
#
# match num_of_day:
#     case 1: print('Monday')
#     case 2: print('Tuesday')
#     case 3: print('Wednesday')
#     case 4: print('Thursday')
#     case 5: print('Friday')
#     case 6: print('Saturday')
#     case 7: print('Sunday')


# task2

# num_of_month = int(input('Enter the number of month : '))
#
# match num_of_month:
#     case 1: print('January ')
#     case 2: print('February ')
#     case 3: print('March ')
#     case 4: print('April ')
#     case 5: print('May ')
#     case 6: print('June ')
#     case 7: print('July ')
#     case 8: print('August ')
#     case 9: print('September   ')
#     case 10: print('October  ')
#     case 11: print('November ')
#     case 12: print('December ')


# task3

# number = int(input('Введіть число: '))
#
# match number:
#     case _ if number > 0:
#         print('Number is positive')
#     case _ if number < 0:
#         print('Number is negative')
#     case 0:
#         print('Number is equal to zero')


# task4

first_num = int(input('Enter the first number : '))
second_num = int(input('Enter the second number : '))

if first_num == second_num:
    print('Numbers are equal')
else:
    print(min(first_num, second_num), max(first_num, second_num))
