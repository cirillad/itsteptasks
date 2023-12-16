# task1

# palindrome = str(input('Enter the text : '))

# if palindrome == palindrome[::-1]:
#     print('Its palindrome')
# else:
#     print('Its not palindrome')


# task2

# text = input('Enter the text: ')
# reserved_words = input('Enter reserved words: ').split()
# split_text = text.split()

# for i in range(len(split_text)):
#     word = split_text[i].strip(".,!?;:'\"()[]{}")
#     punctuation = split_text[i][len(word):]
#     if word.lower() in reserved_words:
#         split_text[i] = word.upper() + punctuation

# text1 = ' '.join(split_text)
# print(text1)


# task3

# text = input('Enter the text: ')
# znaks = ['.', '!', '?']
# count = 0

# for znak in znaks:
#     split_text = text.split(znak)
#     count += len(split_text) - 1

# print(count)



