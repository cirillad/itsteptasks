# task1

# try:
#     name = str(input("Enter your name : "))
#     age = int(input("Enter your age : "))

#     if 0 < age < 130:
#         print(f"Hello, {name}! Your age - {age}")
#     else:
#         raise Exception('Incorrect number')
# except Exception as i:
#     print(f'ERROR: {i}')


# ---------------------------------------------------------------

# task2

# def HelloNameAge(name, age):
#     try:
#         if 0 < age < 130:
#             print(f"Hello, {name}! Your age - {age}")
#         else:
#             raise Exception('Incorrect number')
#     except Exception as i:
#         print(f'ERROR: {i}')


# HelloNameAge('John', 23)






# def HelloNameAge(name, age):
#         if 0 < age < 130:
#             print(f"Hello, {name}! Your age - {age}")
#         else:
#             raise Exception('Incorrect number')

# try:
#     HelloNameAge('John', 23)
# except Exception as i:
#     print(f'ERROR: {i}')


# ---------------------------------------------------------------

# task3

# nums = []

# while True:
#     try:
#         num = input("Enter a number (or 'Stop' to end): ")

#         if num.lower() == 'stop':
#             nums.clear()
#             break
        
#         num = int(num)

#         if num < 0:
#             raise ValueError("The number should be non-negative.")

#         nums.append(num)
#         print(nums)

#     except ValueError as ve:
#         print(f"ERROR: {ve}")


# ---------------------------------------------------------------
        
# task4

# nums = []

# def numsList():
#     try:
#         num = input("Enter a number (or 'Stop' to end): ")

#         if num.lower() == 'stop':
#             nums.clear()
#             raise StopIteration
    
#         num = int(num)

#         if num < 0:
#             raise ValueError("The number should be non-negative.")

#         nums.append(num)
#         print(nums)

#     except ValueError as ve:
#         print(f"ERROR: {ve}")

# while True:
#     try:
#         numsList()
#     except StopIteration:
#         break



# nums = []

# def numsList():
#     num = input("Enter a number (or 'Stop' to end): ")

#     if num.lower() == 'stop':
#         nums.clear()
#         raise StopIteration
#     num = int(num)

#     if num < 0:
#         raise ValueError("The number should be non-negative.")

#     nums.append(num)
#     print(nums)

# while True:
#     try:
#         numsList()
#     except StopIteration:
#         break
#     except ValueError as ve:
#         print(f"ERROR: {ve}")






    
    
        
        




