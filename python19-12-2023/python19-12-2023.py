# task1
# first method

# input1 = input('Enter an arithmetic expression (for example "15+29") : ')
# print(eval(input1))


# second method

# input = input('Enter an arithmetic expression (for example "15 + 29") : ')
# split_input = input.split()
# split_input[0] = float(split_input[0])
# split_input[2] = float(split_input[2])

# if split_input[1] == '+':
#     print(split_input[0] + split_input[2])
# if split_input[1] == '-':
#     print(split_input[0] - split_input[2])
# if split_input[1] == '*':
#     print(split_input[0] * split_input[2])
# if split_input[1] == '/':
#     print(split_input[0] / split_input[2])
# else:
#     print('Try one more time.')


# task2

# import random
 
# list = [random.randint(-100, 100) for i in range(10)]

# print(list)

# print(f'Max: {max(list)}, min: {min(list)}')

# count_less_zero = 0
# for i in range(len(list)):
#     if list[i] < 0:
#         count_less_zero += 1
# print(f'Number of negative numbers :{count_less_zero}')

# count_more_zero = 0
# for i in range(len(list)):
#     if list[i] > 0:
#         count_more_zero += 1
# print(f'Number of positive numbers :{count_more_zero}')

# count_zero = 0
# for i in range(len(list)):
#     if list[i] == 0:
#         count_more_zero += 1
# print(f'Number of numbers equal to zero :{count_zero}')



