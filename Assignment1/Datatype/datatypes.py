print("Question 1. to count the number of characters in a string.")
string = input("Enter a string: ")
count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(str(count))

print("Question 2. to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. ")
string = input("Enter a string: ")
count = len(string)
if count>=2:
    new_string = string[0:2] + string[count-2:count]
    print(new_string)
else:
    print("")

print("Question 3.to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.")
string = input("Enter a string: ")
char =  string[0]
string = string.replace(char,'$')
string = char + string[1:]
print (string)

print("Question 4. to get a single string from two given strings, separated by a space and swap the first two characters of each string. ")
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]
output_string = new_string1 + ' ' + new_string2
print(output_string)

print("Question 5.to add 'ing' at the end of a given string. If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.")
string = input("Enter a string: ")
count = len(string)
if count>=3:
    if string[-3:] == 'ing':
        string += 'ly'
    else:
        string += 'ing'
print(string)
 
print("Question 6. to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.")
string = input("Enter a string: ")
s_not = string.find('not')
s_poor = string.find('poor')
if s_poor>s_not and s_not>0:
    string = string.replace(string[s_not:(s_poor+4)],'good')
print(string)

print("Question 7.Function to  takes a list of words and returns the length of the longest one. ")
word = []
def longest_word(words_list):
    words = []
    for i in words_list:
        words.append((len(i),i))
    words.sort()
    return words[-1][1]
n = int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element = input("Enter element" + str(x+1) + " : ")
    word.append(element)   
print("Longest word : " + longest_word(word))


print("Question 8.to remove the nth index character from a nonempty string")
#to remove the nth index character
string = input("Enter a string: ")
n = int(input("Enter the value of n"))
a = string [:n]
b = string[n+1:]
string = a + b
print (string)


print("Question 9.to exchange first and last element of string. ")
string = input("Enter a string: ")
string = string[-1] + string [1:-1] + string[0]
print(string)


print("Question 10.to remove character which have odd index value of a string.") 
string = input("Enter a string: ")
result = ""
for i in range(len(string)):
    if i%2 == 0:
        result = result + string[i]
print(result)


print("Question 11.to count the occurrences of each word in senetence.")
string = input("Enter a sentence: ")
count = {}
words = string.split()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)


print("Question 12.to display input in upper and lower cases.")
user_input = input("Enter a string")
print("UpperCase : " + user_input.upper())
print("LowerCase : " + user_input.lower())


print("Question 13.to prints the unique words in sorted form. ")
string = input("Input comma separated sequence of words")
words = [word for word in string.spilt(",")]
print(",".join(sorted(list(set(words)))))



print("Question 14.to create HTML string with tags around the words")
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
string = input("Enter a string")
tag = input("Enter a tag")
print(add_tags(tag, string))


print("Question 15.to insert string in the middle of string")
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]
string = input("Enter a word")
str = input("Enter a string eg: [[]]/{{}} : ")
print(insert_sting_middle(str, string))

print("Question 16. to sum all items in a list")
myList = []
n = int(input('Enter number of element in list : '))
for i in range(n):
    numbers = int(input('Enter number '))
    myList.append(numbers)
print("Sum of elements in given list is :", sum(myList))


print("\nQuestion 17. to multiplies all the items in a list")
result = 1
for x in myList:
    result = result * x
print("Multiplies of item in list :", result)

print("\nQuestion 18. to get largest number from list")
myList.sort()
print("Largest number : ", myList[-1])


print("\nQuestion 19. to get smallest number from list")
print("Smallest number : ", myList[0])


print("\nQuestion 20. to count number of string where the string length is 2 or more and the first and last character are same")
myList1 = []
n = int(input('Enter number of word in list : '))
for i in range(n):
    words = input('Enter a word ')
    myList1.append(words)
count = 0
for word in myList1:
    if word[0] == word[-1] and  len(word)>1 :
        count += 1
print("Count : ",count)


print("\nQuestion 21. to sort in increasing order by the last element")
def last(n): return n[-1]
def sort_list_last(tuples):
    print("Given tuple : ",tuples)
    return sorted(tuples, key=last)
print("Sorted tuple : ",sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


print("\nQuestion 22. to remove duplicates from a list.")
myList = []
myList1 = []
n = int(input('Enter number of element in list : '))
for i in range(n):
    numbers = int(input('Enter number '))
    myList.append(numbers)
for i in myList:
    if i not in myList1:
        myList1.append(i)
print(myList1)


print("\nQuestion 23. to check if a list is empty or not.")
lis1 = []
print("Given list : ",lis1)
if not lis1:
    print("List is empty")
else:
    print("List isnot empty")


print("\nQuestion 24. to clone or copy list.")
new_list = list(myList1)
print("Before cloning or copying : ",myList1)
print("Clone or copy list : ",new_list)


print("\nQuestion 25. to check whether all dictionaries in a list are empty or not")
sample1 = [{},{},{}]
print("Given sample1 : ", sample1)
all_empty = True
for i in sample1:
  if i:
    all_empty = False
if all_empty == True:
    print(all_empty,"All dictionaries in a list are empty")
else:
    print(all_empty,"All dictionaries in a list arenot empty")


print("\nQuestion 26.  to insert a given string at the beginning of all items in a list.")
string = input("Enter a string")
print("Given String : ",string)
print("Given list : ", myList1)
string += '{0}'
print("Output : ", [string.format(i) for i in myList1])


print("\nQuestion 27.to replace the last element in a list with another list.")
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
print("List1 : ", list1 , "\nList2 : ",list2)
list1[-1:] = list2
print("Output : ",list1)


print("Question 28.to add a key to a dictionary.")
dic = {'a': 1, 'b': 2}
print("Dictionary : ", dic)
dic.update({'c':3})
print("After Adding : ",dic)

 
print("\nQuestion 29.to concatenate following dictionaries to create a new")
a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {'e': 5, 'f': 6}
print ("Dic1 : ", a ,"\nDic2 : ", b, "\nDic3 : ",c)
dic = {}
for d in (a,b,c): dic.update(d)
print("Output : ",dic)


print("\nQuestion 30.to check whether a given key already exists in a dictionary.")
print("Given :",a)
x = input("Enter key")
if x in a:
    print("Key is present in the dictionary")
else:
    print('Key is not present in the dictionary')


print("Question 31.to iterate over dictionaries using for loops.")
for key, value in a.items():
    print(key, 'corresponds to ', a[key]) 

 
print("Question 32.to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). ")
n=int(input("Input a number "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)


print("Question 33.to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys")
for x in range(1,16):
    d[x]=x*x
print(d)


print("Question 34. to merge two Python dictionaries.")
a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {'e': 5, 'f': 6}
print ("Dic1 : ", a ,"\nDic2 : ", b, "\nDic3 : ",c)
a.update(b)
a.update(c)
print("Output : ",a)

 
print("Question 35.to iterate over dictionaries using for loops.")
for key, value in a.items():
    print(key, 'corresponds to ', a[key]) 

 
print("Question 36.to sum all the items in a dictionary. ")
print("Dictionary : ",a)
print("Sum : ",sum(a.values()))


print("Question 37.to multiply all the items in a dictionary.")
print("Dictionary : ",a)
result = 1
for key in a:
    result = result * a[key]
print("Multiply of all items : ",result)


print("Question 37.to remove a key from a dictionary.")
print("Dictionary : ",a)
key = input("Enter key you want to delete")
if key in a:
    del a[key]
print("After deletion : ", a)

print("\nQuestion 39.to unpack a tuple in several variables")
data = (1, 2, 3)
print("Given tuple : ",data)
x, y, z = data
print("x: ",x,"\ny: ", y,"\nz: ", z)


print("\nQuestion 40.to add an item in a tuple.")
add = int(input("Enter an item1"))
data = data + (add,) 
print("Tuple : ", data)


print("\nQuestion 41. to convert a tuple to a string.")
tuple1 = ('h','e','l','l','o')
print("Given tuple : ", tuple1)
string = ''.join(tuple1)
print(tuple1 , "is converted to " , string)


print("\nQuestion 42.to convert a list to a tuple.")
list1 = [1,2,3,4]
print('Given list : ',list1)
print(list1,"is converted to", tuple(list1))

 
print("\nQuestion 43.to remove an item from a tuple.")
data = (1, 2, 3,4,5)
print("Tuple : ", data)
item = int(input("Enter an item to remove"))
data = list(data)
data.remove(item)
data = tuple(data)
print("After removing : ",data)


print("\nQuestion 44.to slice a tuple.")
print("Given tuple : ",data)
x = slice(0,5,3)
print("Slicing : ",data[x])


print("\nQuestion 45.to find the index of an item of a tuple.")
print("Given tuple : ", tuple1)
x = tuple1.index('e')
print("The index of e:",x)

 
print("\nQuestion 46.to find the length of a tuple.")
print("Given tuple : ", tuple1)
x = len(tuple1)
print("Length of Tuple1 : ", x)