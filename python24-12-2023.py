# task1

# def calculate(list):
#     result = 1
#     for i in list:
#         result *= i
#     return result

# print(calculate([1, 2, 3, 4]))
        

# task2

# def minimum(list):
#     result = min(list)
#     return result

# print(minimum([1, 2, 3, 4, 5]))


# task3

# def nums(num):
    
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
        
# def lists(list1):
#     count = 0
#     for i in list1:
#         if nums(i):
#             count +=1
#     return count

# list2 = [2,3,4,5,6,7,11,13]
# result = lists(list2)
# print(f"Кількість простих чисел у списку : {result}")

# task4

# def fun(num, list1):
#     list1 = list(list1)
#     list1.remove(num)
#     return list1

# print(fun(4, [1, 2, 3, 4, 5]))


# task5

# def fun(a, b):
#     result = a + b
#     return result

# print(fun([1, 2, 3, 4], [5, 6, 7, 8]))


# task6

def fun(num, list):
    result = ""
    for i in list:
        i = i ** num
        i = str(i) + " "
        result += i
    return result

print(fun(2, [1, 2, 3, 4, 5]))

