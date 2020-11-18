import math
"""
Inverting a string
"""
# test = "Madam, i'm Adam"
# cp = ""
# for ch in test:
#     cp = cp + ch # prints the same string as test, because cp is first
#     cp = ch + cp # prints inverted string of test, because cp is after ch

# M = [ [ 13, -2, 5],
# [ 0, 100, 9],
# [-13, 27, -10] ]
# for row in M:
#     for e in row:
#         print (e, end="\t")
#     print()

# sum = 0
# for row in M:
#     for e in row:
#         sum += e
# print(sum)
# c = 8
# s = [[0]*c] * 3
# n = s[1][1]
# s [1][1] = 8
# print(s)


# data = """
#
# Example text for experimenting with regular expressions.
# Most of the text is just nonsense.
#
# We start with a piece of program copied from the introduction to debugging:
#
# def sum_to(n):
#     total = 0
#     for i in range(n+1):
#         new_total = total + i
#         total = new_total
#     return total
#
# def sum_of_sums(n):
#     total = 0
#     for i in range(n+1):
#         new_total = total + sum_to(i)
#         total = new_total
#     return total
#
# --------------------------------------------------------
#
# Texts for single character patterns and sequences:
#
# If we want to specify one of the special characters ("()[].*+?|^${\")
# as a pattern, we have to put a backslash ("\") in front of it --
# like we had to do for quotes in a string literal.
# Other non-letters-or-digits: , : ; ! ' " ` - / < = > ~ @ # % &
#
# Note that Sum, sum, sUm, SUM, etc. are all distinct names for Python.
#
# --------------------------------------------------------
#
# Texts for wildcards:
#
# abacadabra contains characters a as well as b ....
# what matches a.a?
#
# --------------------------------------------------------
#
# Texts for character sets and character ranges:
#
# Any of ...
# 62740200 83518400 5917777
# specifies a weird round number... many ways exist
#
# --------------------------------------------------------
#
# Texts for repetition:
#
# Any of ...
# 62740200 83518400 5917777
# specifies a weird round number... many ways exist
#
# searching a regular expression
# just searching
#
# --------------------------------------------------------
#
# Texts for parentheses and alternatives:
#
# oxxxoxxxxoxoxoxoxxoxxxoxooo
# For example, the pattern "def|for|return" matches any of these three words,
# xooxxxxxoxooxxoooxxxxoooooo
# and the pattern "[a-z]+|[A-Z]+" matches a sequence of letters
# all in lower case or all in upper case, but not mixed case.
# ooooxoxxoxooxooxxoooxoxooox
# ALL IN LOWER CASE OR ALL IN UPPER CASE, BUT NOT MIXED CASE.
# AlL In lOwEr cAsE Or aLl iN UpPeR CaSe, BuT NoT MiXeD CaSe.
#
# --------------------------------------------------------
#
# Texts for substituting groups:
#
# text = 'ab[cd:ef]gh'
# Let's do that again:
#     text = 'ab{cd:ef}gh'
# and again:
#         text = 'ab{cd:ef}gh'
# one more time...
#             text = 'ab{cd:ef}gh'
#
# text = 'Some stup1d text example; test 123'
#
# Just to make sure we have enough identical examples:
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
# inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur inf22306wur
#
# data = 'inf22306wur tutorial1a assignments3b'
# wrong = '[abc}x:y{def]' # or right??
# 2222.2955646
# 6.50000E+01
# <sadasdasd>
# """
#
# import re
# # pattern = re.compile(r"\{(.*:.*)\}")
# # find = pattern.finditer(data)
# # for match in find:
# #     print (match)
#
# matcher = re.compile('([a-z]+)([0-9]+)([a-z]+)')
# data = 'inf22306wur tutorial1a assignments3b'
# print(matcher.sub(r'\1\2\3',data))
# #output# inf-22306-wur tutorial-1-a assignments-3-b
# print(matcher.sub(r'\1-\2-\3',data, 1))
# #output# inf-22306-wur tutorial1a assignments3b
# print(matcher.sub(r'\1-\2-\3',data, 0))
# #output# inf-22306-wur tutorial-1-a assignments-3-b
# print(matcher.sub(r'\1-\2-\3',data, 5))
# #output# inf-22306-wur tutorial-1-a assignments-3-b
# print(matcher.sub(r'\1...\3',data))
# #output# inf...wur tutorial...a assignments...b

# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """
# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30
#
# start = Time()
# start.hour = 9
# start.minute = 45
# start.second = 0
#
# duration = Time()
# duration.hour = 1
# duration.minute = 35
# duration.second = 0
#
#
# def add_time(t1,t2):
#     sum = Time()
#     sum.hour = t1.hour + t2.hour
#     sum.minute = t1.minute + t2.minute
#     sum.second = t1.second + t2.second
#     print (sum)
#
# add_time(start,duration)

# l = [(4,10),(10,4),(10,16)]
#
# def on_circle(coords, center, dist):
#     circle = True
#     i = 0
#     while circle and i < len(coords):
#         x, y = coords[i]
#         i_dis = math.sqrt((center[0]-x)**2+(center[1]-y)**2)
#         if i_dis != dist:
#             circle = False
#         i += 1
#     return circle
# print (on_circle([(4,10),(10,4),(10,16)],(10,10), 6))
# # print (on_circle([(4,10),(10,4),(16,16)],(10,10), 6))
#
# def check_capital(string_value):
#     capital = False
#     for i in range(65,91):
#         if chr(i) in string_value:
#             capital = True
#     return capital
#
# def keep_capitals(iterable_data):
#     result = []
#     for item in iterable_data:
#         if check_capital(item):
#             result.append(item)
#     return result
#
#
# def check(matrix, value):
#     p_list = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == value:
#                 p_list += [(i,j)]
#     return p_list
# A=[[1, 0, -1], [1,3,1]]
# check1 = 1
#
# scores = {'ID1': (3, 3, 4, 5),
#           'ID2': (2, 5, 4, 5),
#           'ID3': (3, 3, 4, 3),
#           }
# def evaluation_score(score_dic):
#     for key, value in score_dic.items():
#         total_average = 0
#         for score in value:
#             total_p_s = 0
#             total_p_s += score
#             print (total_p_s)
#             average_p_s = total_p_s / 4
#             total_average += average_p_s
#         return total_average
#
# def calculate_final_grade (score, weight):
#     total = 0
#     for s, w in zip(score,weight):
#         score = s*w
#         total += score
#     final_score = total / 100
#     h = final_score - int(final_score)
#     if 0.3 <= h < 0.8:
#         final_score2 = int(final_score) + 0.5
#     elif h >= 0.8:
#         final_score2 = int(final_score) + 1
#     else:
#         final_score2 = int(final_score)
#     return final_score2
# print (calculate_final_grade((8, 8, 7, 6), (10, 20, 30, 40)))
