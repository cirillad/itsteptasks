# task1

# def func(a, b):
#     if b == 0:
#         return a
#     return func(b, a % b)


# print(func(36, 12))


# task 2 

# def BullCows(secret_num, num, attemts=1):
#     bulls = 0
#     cows = 0

#     if len(secret_num) != len(num):
#         print('Please try again with the correct four-digit number.')
#         return BullCows(secret_num, input("Attempt №" + str(attemts) + ": "))
    
#     for i in range(len(secret_num)):
#         if num[i] in secret_num:
#             bulls += 1
#         if num[i] == secret_num[i]:
#             cows += 1

#     if cows == len(secret_num):
#         print(f"You won! You guessed the number {secret_num} with {attemts} attempts.")
#     else:
#         print(f"Bulls: {bulls}, Cows: {cows}.")
#         return BullCows(secret_num, input("Attempt №" + str(attemts) + ": "), attemts + 1)


# def PlayBullsCows():
#     secret_number = '1234'
#     print("Guess the four-digit number.")
#     number = input("Attempt №1: ")
#     BullCows(secret_number, number)


# PlayBullsCows()


# task3

# def is_valid_move(x, y, board):
#     return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1

# def print_board(board):
#     for row in board:
#         print(row)

# def solve_knight_tour(board, x, y, move_count):
#     if move_count == len(board) * len(board[0]):
#         print_board(board)
#         return True

#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
#              (-2, -1), (-1, -2), (1, -2), (2, -1)]

#     for move in moves:
#         new_x, new_y = x + move[0], y + move[1]
#         if is_valid_move(new_x, new_y, board):
#             board[new_x][new_y] = move_count
#             if solve_knight_tour(board, new_x, new_y, move_count + 1):
#                 return True
#             board[new_x][new_y] = -1

#     return False

# def knight_tour(n):
#     board = [[-1 for _ in range(n)] for _ in range(n)]
#     start_x = int(input("Enter x: "))
#     start_y = int(input("Enter y: "))
#     board[start_x][start_y] = 0
#     if not solve_knight_tour(board, start_x, start_y, 1):
#         print("No solution exists.")
#     else:
#         print("Knight's tour:")
#         print_board(board)

# knight_tour(8)


# task4

# import random

# def generate_puzzle():
#     puzzle = list(range(1, 16))
#     random.shuffle(puzzle)
#     puzzle.append("X")
#     return [puzzle[i:i+4] for i in range(0, 16, 4)]

# def print_puzzle(puzzle):
#     for row in puzzle:
#         print(" ".join(map(str, row)))

# def find_blank(puzzle):
#     for i in range(4):
#         for j in range(4):
#             if puzzle[i][j] == "X":
#                 return i, j

# def is_valid_move(i, j):
#     return 0 <= i < 4 and 0 <= j < 4

# def move_puzzle(puzzle, direction):
#     blank_i, blank_j = find_blank(puzzle)
#     if direction == "UP" and is_valid_move(blank_i - 1, blank_j):
#         puzzle[blank_i][blank_j], puzzle[blank_i - 1][blank_j] = puzzle[blank_i - 1][blank_j], puzzle[blank_i][blank_j]
#     elif direction == "DOWN" and is_valid_move(blank_i + 1, blank_j):
#         puzzle[blank_i][blank_j], puzzle[blank_i + 1][blank_j] = puzzle[blank_i + 1][blank_j], puzzle[blank_i][blank_j]
#     elif direction == "LEFT" and is_valid_move(blank_i, blank_j - 1):
#         puzzle[blank_i][blank_j], puzzle[blank_i][blank_j - 1] = puzzle[blank_i][blank_j - 1], puzzle[blank_i][blank_j]
#     elif direction == "RIGHT" and is_valid_move(blank_i, blank_j + 1):
#         puzzle[blank_i][blank_j], puzzle[blank_i][blank_j + 1] = puzzle[blank_i][blank_j + 1], puzzle[blank_i][blank_j]

# def is_solved(puzzle):
#     return all(puzzle[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4) if puzzle[i][j] != "X")

# def play_puzzle(puzzle):
#     print("Welcome to 15 Puzzle!")
#     print_puzzle(puzzle)

#     while not is_solved(puzzle):
#         move = input("Enter move (UP/DOWN/LEFT/RIGHT): ").upper()
#         move_puzzle(puzzle, move)
#         print_puzzle(puzzle)

#     print("Congratulations! You solved the puzzle!")

# if __name__ == "__main__":
#     puzzle = generate_puzzle()
#     play_puzzle(puzzle)










