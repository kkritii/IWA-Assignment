print("Question 1. Function to find the Max of three numbers")
def getMaxVal ( numList ):
    numList.sort()
    return  (numList[-1]) 
myList = []

print("Enter value for three numbers: ")
for i in range(3):
    number = int(input("Enter value for number: "))
    myList.append(number)
print ("The Maximum value between ",myList," is ", getMaxVal(myList))

#  to sum all the numbers in a list. 
print("\nQuestion 2. Function to sum up all numbers in a list.")
def sumListItems (list): 
    total = 0
    for x in list:
        total += x
    return total

n = int(input("Enter the number of element in list: "))
inputList = []
for i in range(n):
    num = int(input('Enter number: '))
    inputList.append(num)
print ("Sum of elements in given list is: ", sumListItems(inputList))

#  to multiply all the numbers in a list. 
print("\nQuestion 3. Function to multiply all the numbers in a list.")
def multiplyListItems(list):
    result = 1
    for x in list:
        result= result * x
    return result

n = int(input("Enter the number of element in list: "))
inputList = []
for i in range(n):
    num = int(input('Enter number: '))
    inputList.append(num)
print ("The total multiplied value of the list ", inputList, " is ", multiplyListItems(inputList))

#  to reverse a string. 
print("\nQuestion 4. Function to reverse a string")
def reverseString (string):
    # return string[::-1]
    str = "" 
    for x in string: 
        str = x + str
    return str

inputString = input("Enter the String: ")
print ("The Reverse of String "+inputString+" is ", reverseString(inputString))

 
print("\nQuestion 5. Function to calculate factorial of a number")
def getFactorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range (1,int(num)+1):
            factorial = factorial * i
        return factorial
    elif int(num) == 0:
        return 1

number= int(input("Enter the Number: "))
print ("Factorail of ",number , " is : ",getFactorial(number))

#to check whether a number is in a given range. 
print("\nQuestion 6. Function to check if a number is in a given range")
def rangeChecker(max, min, num):
    if int(num) >= min and int(num) <= max:
        return True
    else:
        return False

min = int(input("Enter Min Value of Range: "))
max = int(input("Enter Max Value of Range: "))
num = int(input("Enter the Number: "))
if rangeChecker( max, min, num):
    print( "The number ", num, " lies in range of ", min, " and ", max)
else:
    print ("The number ", num, " doesnot lies in range of ", min, " and ", max)


# tocalculate the number of upper case letters and lower case letters. 
print("\nQuestion 7. Function accepts a string and calculate the number of upper and lower case letters")
def caseChecker(theString):
    upperCaseCount=0
    lowerCaseCount=0
    for i in theString:
        if(i.islower()):
            lowerCaseCount += 1
        elif(i.isupper()):
            upperCaseCount +=1
    print("The number of lowercase characters is:", lowerCaseCount)
    print("The number of uppercase characters is:", upperCaseCount)

theString = input("Enter the string: ")
caseChecker(theString)

#function that takes a list and returns a new list with unique elements of the first list. 
print("\nQuestion 8. Function accepts a list and returns a new list with unique elements of the first list")
def unique_list(list):
    x = []
    for a in list:
        if a not in x:
            x.append(a)
    return x

n = int(input("Enter the number of element in list: "))
inputList = []
for i in range(n):
    num = int(input('Enter number: '))
    inputList.append(num)
print( "Old List: ", inputList)
print( "New Unique List: ", unique_list(inputList))

# to check the  number is prime or not. 
print("\nQuestion 9. Function that takes a number as a parameter and check the number is prime or not. ")
def primeNumChecker(number):
    # prime number is always greater than 1
    if number > 1:
        if number == 2:
            print( number, " is a prime number")
        else:
            for i in range(2, number):
                if (number % i) == 0:
                    print (number, "is not a prime number")
                    break
                else:
                    print (number, "is a prime number")
                    break
    else:
        print (number, "is not a prime number")

number = int(input("Enter the number: "))
primeNumChecker(number)

#to print the even numbers from a given list. 
print("\nQuestion 10.to print the even numbers from a given list. ")
def getOnlyEvenOnes(list):
    evenList = []
    for x in list:
        if (x % 2) == 0:
            evenList.append(x)
    return evenList

num1 = int(input("Enter the number of element in list: "))
inputList = []
for i in range(num1):
    num = int(input('Enter number: '))
    inputList.append(num)

print ("The EvenNumber list: ", getOnlyEvenOnes(inputList))

#  to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result. 
print("\nQuestion 11. to create Lambda function to add 15 to given number and also lambda function that mutiplies x and y argument. ") 
num = int(input("Enter the number: "))
add15 = lambda num : num + 15
print (num, " + 15 = ", add15(num))
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
mulXY = lambda x, y : x * y
print (x, " x ", y, " = ", mulXY(x,y))

#to create a function that takes one argument, and that argument will be multiplied with an unknown given number. 
print("\nQuestion 12.to create a function that takes one argument, and that argument will be multiplied with an unknown given number. ")
def func_compute(n):
    return lambda x : x * n
    
n = int(input("Enter a number"))
result = func_compute(n)
print("Output =", result(15))

#to sort a list of tuples using Lambda.
print("\nQuestion 13.to sort a list of tuples using Lambda.")
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),]
print("Tuples:",subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

#to sort a list of dictionaries using Lambda. 
print("\nQuestion 14.to sort a list of dictionaries using Lambda.")
list1 = [{ "name" : "Kriti", "age" : 20},  
{ "name" : "Lucky", "age" : 21 }, 
{ "name" : "Shristi" , "age" : 14 }, 
{ "name" : "Sushil" , "age" : 19 }]   
print ("The list sorting by age: ")
print (sorted(list1, key = lambda i: i['age']))

#to filter a list of integers using Lambda. 
print("\nQuestion 15.to filter a list of integers using Lambda.")
myList = []
n = int(input('Enter number of element in list : '))
for i in range(n):
    numbers = int(input('Enter number '))
    myList.append(numbers)
print("Given list :",myList)
even_myList = list(filter(lambda x: x%2 == 0, myList))
print("Even numbers from given list",even_myList)
odd_myList = list(filter(lambda x: x%2 != 0, myList))
print("Odd numbers from the said list: ",odd_myList)

#to square and cube every number in a given list of integers using Lambda. 
print("\nQuestion 16.to square and cube every number in a given list of integers using Lambda.")
print("Given list :",myList)
square_myList = list(map(lambda x: x ** 2, myList))
print("Square of every element of given list: ",square_myList)
cube_myList = list(map(lambda x: x ** 3, myList))
print("Cube of every element of given list: ",cube_myList)

# to find if a given string starts with a given character using Lambda. 
print("\nQuestion 17.to find if a given string starts with a given character using Lambda." )
string = input("Enter a string")
char = input("enter a character")
starts_with = lambda string: True if string.startswith(char) else False
print(starts_with)

# to check whether a given string is number or not using Lambda. 
print ("\nQuestion 18.to check whether a given string is number or not using Lambda.")
str1 = 'kri123ti'
print(str1,str1.isnumeric())
str2 = '123'
print(str2,str2.isnumeric())

# to create Fibonacci series upto n using Lambda. 
print("\nQuestion19. to create Fibonacci series upto n using Lambda ")
from functools import reduce
number = int(input("Enter the n value: "))
getFibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1]) 
print(getFibonacci(number))


#to find intersection of two given arrays using Lambda. 
print ("\nQuestion 20.to find intersection of two given arrays using Lambda")
array1 = []
n1 = int(input("Enter length of Array1: "))
for i in range(n1):
    number = int(input("Enter number: "))
    array1.append(number)
array2 = []
n2 = int(input("Enter length of Array2: "))
for i in range(n2):
    number = int(input("Enter number: "))
    array2.append(number)
print ("OLD arrays: ")
print (array1)
print (array2)
intersection = list(filter(lambda x: x in array1, array2)) 
print ("Intersection of two given arrays are: ",intersection)