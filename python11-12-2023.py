# task1
#
# start = int(input('Enter the first number : '))
# finish = int(input('Enter the second number : '))
#
# for i in range(start, finish):
#     i += 1
#     if i % 7 == 0:
#         print(i)


# task 2

# start = int(input('Enter the first number : '))
# finish = int(input('Enter the second number : '))
#
# print('All numbers in the range')
# for i in range(start, finish + 1):
#     print(i, end=' ')
#
# print('\nAll numbers in the range in descending order')
# for i in range(finish, start - 1, - 1):
#     print(i, end=' ')
#
# print('\nAll numbers are multiples of 7')
# for i in range(start, finish + 1):
#     if i % 7 == 0:
#         print(i, end=' ')
#
# count = 0
# print('\nThe number of numbers that are multiples of 5')
# for i in range(start, finish + 1):
#     if i % 5 == 0:
#         count += 1
# print(count)


# task 3

start = int(input('Enter the first number : '))
finish = int(input('Enter the second number : '))

for i in range(start, finish + 1):
    if i % 5 == 0 and i % 3 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Buzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 5 != 0 and i % 3 != 0:
        print(i)
