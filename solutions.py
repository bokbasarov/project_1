#26.05, 1-solution
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
#
# def get_prime_numbers(limit):
#     prime_numbers = []
#     for num in range(2, limit + 1):
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers
#
#
# user_input = int(input("Введите число: "))
#
# prime_numbers_list = get_prime_numbers(user_input)
#
# print("Простые числа до", user_input, ":", prime_numbers_list)




# 2-solution
# word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# probel = int(input("пробелы: "))
# message = input("послание: ").upper()
# itog = ''
#
# for i in message:
#     mesto = word.find(i)
#     new_mesto = mesto + probel
#     if i in word:
#         itog += word[new_mesto]
#     else:
#         itog += i
#
# print(itog)



# 3-solution
# def is_palindrome(word):
#     return word == word[::-1]
#
#
# def find_palindrome_pairs(words):
#     palindrome_pairs = []
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if is_palindrome(words[i] + words[j]):
#                 palindrome_pairs.append((words[i], words[j]))
#             if is_palindrome(words[j] + words[i]):
#                 palindrome_pairs.append((words[j], words[i]))
#     return palindrome_pairs
#
#
# user_input = input("Введите список слов через пробел: ")
#
# word_list = user_input.split()
#
# palindrome_pairs_list = find_palindrome_pairs(word_list)
#
# print("Палиндромные пары:")
# for pair in palindrome_pairs_list:
#     print(pair[0], pair[1])
#----------------------------------------------------------------------------------------------



