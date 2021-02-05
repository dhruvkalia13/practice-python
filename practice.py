##############
# x = 2
# if x == 2:
#     print("x is 2")
# else:
#     print("x is not 1")
#
# print(x)

##############
# mystring = "hello"
# myfloat = float(10)
# myint = 20
# if isinstance(mystring, str) and mystring == "hello":
#     print("String is %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float is %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer is %d" % myint)

###############
#
# numbers = [1, 2, 3]
# words = ["hello", "world"]
# words.append("third_word")
# second_word = words[1]
#
# print(numbers)
# print(words)
# print("Second word is %s" % second_word)
#
# for x in words:
#     if x == "third_word":
#         print(x)

###############

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%s."
# print(format_string % data)
# print("Hello %s %s." % (data[0], data[1]))

###############
#
# s = "Strings are awesome!"
# # Length should be 20
# print("Length of s = %d" % len(s))
#
# # First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))
#
# # Number of a's should be 2
# print("a occurs %d times" % s.count("a"))
#
# # Slicing the string into bits
# print("The first five characters are '%s'" % s[:5]) # Start to 5
# print("The next five characters are '%s'" % s[5:10]) # 5 to 10
# print("The thirteenth character is '%s'" % s[12]) # Just number 12
# print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
# print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
#
# # Convert everything to uppercase
# print("String in uppercase: %s" % s.upper())
#
# # Convert everything to lowercase
# print("String in lowercase: %s" % s.lower())
#
# # Check how a string starts
# if s.startswith("Str"):
#     print("String starts with 'Str'. Good!")
#
# # Check how a string ends
# if s.endswith("ome!"):
#     print("String ends with 'ome!'. Good!")
#
# # Split the string into three separate strings,
# # each containing only a word
# print("Split the words of the string: %s" % s.split(" "))

###############

# names = ["James", "Rick"]
# name = "Rick"
# if name in names:
#     print("Your name is either of the two %s" % names)

###############

# x = [1,2,3]
# z = x
# y = [1,2,3]
# print(x == y)
# print(x is y)
# print(x is z)

###############

# str = [0,1]
# print(len(str))

##############

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
#
# count=0
# while(count<5):
#     print(count)
#     count +=1
# else:
#     print("count value reached %d" %(count))
#
# # Prints out 1,2,3,4
# for i in range(1, 10):
#     if(i%5==0):
#         break
#     print(i)
# else:
#     print("this is not printed because for loop is terminated because of break but not due to fail in condition")

##############
#
# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
#
# # your code goes here
# output = []
# for n in numbers:
#     if n == 237:
#         break
#     if n % 2 == 0:
#         output.append(n)
#
#
#
# # your code goes here
# output1 = []
# for number in numbers:
#     if number == 237:
#         break
#
#     if number % 2 == 1:
#         continue
#
#     output1.append(number)
#
# print(output == output1)

##############
#
# # Define our 3 functions
# def my_function():
#     print("Hello From My Function!")
#
# def my_function_with_args(username, greeting):
#     print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
#
# def sum_two_numbers(a, b):
#     return a + b
#
# # print(a simple greeting)
# my_function()
#
# #prints - "Hello, John Doe, From My Function!, I wish you a great year!"
# my_function_with_args("John Doe", "a great year!")
#
# # after this line x will hold the value 3!
# x = sum_two_numbers(1,2)
# print(x)

####################
"""
# Modify this function to return a list of strings as defined above
def list_benefits():
    stringsList = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return stringsList

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    out = benefit + " is a benefit of functions!"
    return out

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

########################
"""

########################
"""
from datetime import datetime

dd = '4/20/20'
date_object = datetime.strptime(dd, "%m/%d/%y")
d = date_object.strftime('%B%d')
print(d)
"""

########################
#
# nums = [1, 2, 6, 8]
# nums.app
# abs_diff_func = lambda val : abs(val - 5)
# res = min(nums, key=abs_diff_func)
# print(res)
########################

# nums1 = [1,2]
# nums2 = nums1[:]
# nums1[0] = -1
# print(nums1)
# print(nums2)

#######################
# import copy
# nums1 = [[1,1],[1,0]]
# nums2 = copy.deepcopy(nums1)
# nums1[0][0] = -1
# print(nums1)
# print(nums2)

###################
# nums1 = [[1, 1], [1, 0]]
# nums2 = [[0] * len(nums1[0])] * len(nums1)
# for i, row in enumerate(nums1):
#     nums2[i] = row.copy()
# nums1[0][0] = -1
#
# print(nums1)
# print(nums2)
#########################
# a = "asd-213-qwe2"
# print(a.split("-",3))

# a = [1,4,5,2,3]
# print(sum(a[1:3]))

###################
# nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
# nums1 = [0 if num % 2 == 0 else 1 for num in nums]
# for i in range(len(nums1)):
#     nums1[i] += nums1[i - 1]
# print(nums1)

#####################

# nums = [[5,10],[2,5],[4,7],[3,9]]
# units = [boxType[1] for boxType in nums]
# a = {}
# for unit in units:
#     a[unit] = nums[units.index(unit)][0]
# keyset = a.keys()
# keyset = sorted(keyset, reverse=True)
# for key in keyset:
#     print(key, a[key])
# a = dict(sorted(a.items(),reverse=True))
# for k, v in a.items():
#     print(k,v)
# units = sorted(units, reverse=True)

# print(a)

##################################
# s = "1)2)3"
# if s.__contains__(")"):
#     print("contains")
#     s = (s[::-1].replace(")", "", 1))[::-1]
#     # s = s1[::-1]
# print(s)
###################################
# s = [")","(",")"]

# if s.__contains__(")"):
###################################

# def fitIntoRectangleBoxes(operations: [[int]]):
#     area = []
#     output = []
#     for rect in operations:
#         if len(rect) < 3:
#             continue
#         if rect[0] == 0:
#             area.append([rect[1],rect[2]])
#         elif rect[0] == 1 and rect[1] == 1 and rect[2] == 1:
#             output.append(True)
#         elif rect[0] == 1:
#             if len(area) > 0:
#                 found = False
#                 for box in area:
#                     if rect[1] > box[0] or rect[2] > box[1]:
#                         output.append(False)
#                         found = True
#                         break
#                 if not found:
#                     output.append(True)
#             else:
#                 output.append(True)
#     return output
# # print(fitIntoRectangleBoxes([[0,3,3], [0,5,2], [1,3,2],[1,2,4]]))
# # print(fitIntoRectangleBoxes([[1,1,1]]))
# print(fitIntoRectangleBoxes([[1,44289,71416],
#  [0,21,29],
#  [0,24,36],
#  [1,18,11],
#  [0,30,34],
#  [1,1,26],
#  [1,24,11],
#  [0,28,21],
#  [1,23,190],
#  [0,22,25],
#  [1,12,14],
#  [1,286,498],
#  [0,23,22],
#  [0,21,32],
#  [0,25,36],
#  [0,37,38],
#  [0,31,35],
#  [0,20,26],
#  [0,25,26],
#  [0,27,27],
#  [0,20,32],
#  [1,271,56],
#  [1,474,166],
#  [0,25,32],
#  [0,34,39],
#  [1,21,16],
#  [0,37,35],
#  [1,342,65],
#  [1,322,80],
#  [0,20,26],
#  [0,31,36],
#  [0,23,22],
#  [0,35,31],
#  [0]]))
#################
# i = "1"*400000
# print(int(i,2))

# print(int(a,2))

##
# def solution(a):
#     #
#     output = []
#     temp = 0
#     for i in a:
#         if i < 0:
#             output.append(temp)
#             temp = 0
#         else:
#
#             temp += i
#     output.append(temp)
#     return max(output)
# # a = [1,2,-3,4,5,-6]
# # a = [-8,3,0,5,-3,12]
# a = [-1,2,1,2,0,2,1,-3,4,3,0,-1]
# print(solution(a))
# a = [1,2,3,4,5]
# for i in a:
#     print(i)

# a = [1,2,3,4,5]
# for i, v in enumerate(a):
#     print(i, v)

# a = [1,2,3,4,5]
# for i in range(0,5):
#     print(i, a[i])


#
# output = ""
# for i in a:
#     if i > 0:
#         output += str(i)
#     else:
#         output += "*"
# a = output.split("*")
# for i in a:
#     i = int(i)

# def counts(a: [int], b: [int]):
#     count = []
#     a = sorted(a)
#     for i in b:
#         s = 0
#         for j in a:
#             if j > i: break
#             s += 1
#         count.append(s)
#     return count

# def counts(a: [int], b: [int]):
#     count = []
#     for i in b:
#         count.append(sum(i >= j for j in a))
#     return count

# def counts(a: [int], b: [int]):
#     count = []
#     a = sorted(a)
#     m = min(a)
#     for i in b:
#         if i < m:
#             count.append(0)
#             continue
#         f = lambda list_value: abs(list_value - i)
#         closest_value = min(a, key=f)
#         count.append(a.index(closest_value) + 1)
#     return count

# from bisect import bisect
# def counts(a: [int], b: [int]):
#     count = []
#     a.sort()
#     for i in b:
#         count.append(bisect(a, i))
#     return count
# a = [2,1,3]
# b = [2,1,0, 5]
# print(counts(a, b))

# from collections import OrderedDict
# a = OrderedDict()
# a[1] = "a"
# a[2] = "b"
# print(a)
# a.move_to_end(1)
# a.pop(list(a)[0])
# print(a)

# a = [9,2]
# a.remove(a[-1])

# a = [9,1,2]
# print(a[::-1])

# print(a.isdigit())

# a = "hello! how are oyu"
# words = a.split(" ")
# print(words)

# a = 23
# b = format(a, "b")
# print(b + "asd")
# print(b)
#
# a = "1001"
# print(a.count("1"))

# a = [1,2,3,1]
# temp = set()
# print(temp.add(1))
# print(temp.add(2))

# a = ["1","2","3"]
# b = ["2","1","2"]
# print(sorted(a) == sorted(b))

# a = [1,2,2,1]
# b = [2,2]
# print(set(a+b))


# a = [1, 2, 2, 1]
# i1 = 1
# i2 = 2
# print(max(i1, i2))

# a = [2,4,6]
# from stack import LinkedStack
# a = LinkedStack()
# a.push(2)
# a.push(4)
# a.push(6)
# a.push(8)
# print(a.pop())

# a = [2,4,6]
# #
# print(a.pop())
# a.re
#
# a = "a"
# print(not a)

# delimiter = '/'
# a = ["a","b"]
#
# print(delimiter.join(a))

a = {1:2}
for i in a:
    print(i, val)
