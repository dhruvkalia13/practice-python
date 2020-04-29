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
'''
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
keyword arguments are laways on the right side
"""
def namedArgs(*args, **kargs):
    print(list(args), list(kargs))


def namedFunction(capacity, area, grassType):
    print(capacity, area, grassType)

namedArgs(1, 2, 3, 4, 5, area = 100, capacity = 6, grassType = "green")
'''

from datetime import datetime

dd = '4/20/20'
date_object = datetime.strptime(dd, "%m/%d/%y")
d = date_object.strftime('%B%d')
print(d)
