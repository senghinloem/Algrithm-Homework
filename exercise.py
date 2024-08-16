# Ex1 - String 
# Enter text and display it one by one

# text = input("Enter text here: ")
# for char in text:
#     print(char)


# Ex2 - String
# Enter text and display number of letter

# text = input("Enter text: ")
# for i in range(len(text)):
#     print(i)


# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter

# text = input("Enter your text: ")
# index = 0
# result = "No"
# while index < len(text):
#     if text[index].isupper():
#         result = "Yes"
#         index = len(text)
#     index += 1  
# print(result)


# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space

# text = "3 4 5 6"
# for char in text:
#     if char != " ":
#         print(char)

# Q2 - Sum all number (Total: 18)

# text = "3 4 5 6"
# sum = 0
# for char in text:
#     if char != " ":
#         sum += int(char)
# print(sum)

# text = "3 4 5 6" 
# total = 0 
# for i in range(len(text)): 
#     if text[i] != " ": 
#         print(text[i]) 
#         total += text[i] 
# print(total)
# all in one


# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text

# text = "454639"
# countodd = 0
# counteven = 0
# for i in range(len(text)):
#     if int(text[i]) % 2 == 0:
#         counteven += 1
#     else:
#         countodd += 1
# print("Even number =",counteven)
# print("Odd number =", countodd)
    
# Q2 - Sum all number 

# text = "454639"
# sum = 0
# for i in range(len(text)):
#     sum += int(text[i])
# print(sum)

# Q3 - Sum only even number 

# text = "454639"
# sum = 0
# for i in range(len(text)):
#     if int(text[i]) % 2 == 0:
#         sum += int(text[i])
# print(sum)

# Q4 - Reverse 

# text = "454639"
# reversed_text = ""
# for i in range(len(text)):
#     reversed_text += text[len(text) - 1 - i]
# print(reversed_text)


# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# num = input("Enter number")
# if num % 2 == 1:
#     print("Odd")
# else:
#     print("Even")


# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

# isFoundNum = False
# while not isFoundNum: 
#     num = int(input("Enter number: "))
#     if num >= 10 and num <= 20:
#         print("Continue")
#         isFoundNum = False
#     else:
#         isFoundNum = True
# print("Out of range")


# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string

# text = "9394884039"
# countnum_eight = 0
# index = 0
# while index in range(len(text)):
#     if text[index] == "8":
#         countnum_eight += 1
#     index += 1
# print("Number 8 =", countnum_eight)

# Q2 - What is first index of letter 8        

# text = "9394884039"
# isFoundNum = False
# index = 0
# while not isFoundNum:
#     if text[index] == "8":
#         isFoundNum = True
#     else:
#         index += 1
# print(index)


# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"

# string = "3 4 5 6"
# result = ""
# for char in string:
#     if char != " ":
#         result += char
# print(result)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"

# string = "3 4 5 6"
# result = ""
# for char in string:
#     if char != " ":
#         result += str(int(char) * 2)  + " "
# print(result)


# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0

# num1 = int(input("Number 1: "))
# max_value = num1
# min_value = num1
# for i in range(2, 6):
#     num = int(input("Number " + str(i) + ": ")) 
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num
# print("Max: " + str(max_value))
# print("Min: " + str(min_value))
# first way

# max = 0
# min = 0
# for i in range(5):
#     num = int(input("Enter number: "))
#     if i == 0:
#         max = num
#         min = num
#     else:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
# print("Max =", max)
# print("Min =", min)
# sencond way