# %%
"""
Lists!
A data structure that contain mutable data
"""
#Ex
listrandom = [1, 3, "anjing", True] #can combine number and strings
print (listrandom[2])

listrandom[len(listrandom)-3] #kalau ga dikurangin ga bisa idk why
# %%
"""
Slice and Dice with Lists
remember that lower index is inclusive, upper index is exclusive
"""
listrandom = [1, 3, "anjing", 55, 42, 45, "bangsat"]
print (listrandom[1:4]) #yg "1" dimulai dari index 1, "4" list data dari index 1,2,3.
print (listrandom[1:]) #yg "1" dimulai dari index 1, " " because null it will print all start from index 1
print (listrandom[:4]) # :"number" will print until 3rd index.
# %%
"""
in / not in = statement used to determine ada no. atau ga
"""
'anjing' in 'ngentot'
'anjing' not in 'ngentot'
5 in [1,2,3,4,5,6] # only number 5, if 5 in second digit not counted.
# %%
"""
Mutability and Order
mutability = is can we change the or not the data in list or strings. if can, mutable. if not, immutable.
"""
mylist = [1,2,3,4,7,5]
mylist[0] = 'one'
print(mylist) # can be change because its mutable

"""
anjing = "bangsat kau"
anjing[1]='b'
error because string is immutable
"""

# %%
"""
Quiz: List Indexing
Use list indexing to determine how many days are in a particular month based on the integer variable month,
and store that value in the integer variable num_days.
For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

Remember to account for zero-based indexing!
"""
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]
print(num_days)
# %%
"""
Quiz: Slicing Lists
Select the three most recent dates from this list using list slicing notation.
Hint: negative indexes work in slices!
"""
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[7:])

# %%
"""
usefull function for list
len()
max()
min()
sorted()
"""
teststring ="\n".join(["anjing","babi","kimak","bgst"]) #insert string that assigned in the last string
print(teststring)

teststring ="\n".join(["anjing","babi","kimak","bgst"])
# %%
"""
Tuples = data structure that immutable and ordered. used for save information
U cant change information in tuples
"""
#Ex
location = (3443, 232)
print(location[0])
print(location[1])

#Ex
cube = 50, 40, 69
length, width, height = cube
print("{},{},{}".format(length,width, height))
# %%
"""
Set
data type mutable & unordered
"""
#Ex
number = [1,4,53,2,34,55]
unique_num = set(number)
print(unique_num)

# %%
buah = {"apel","mangga","orange","grape"}
print("watermelon" in buah)
buah.add("watermelon")
print("watermelon" in buah)

print(buah.pop())
print(buah)
# %%
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
"""
6, because a=10 b=4
set only count unique data
"""
# %%
"""
Dictionaries And Identity Operators
Dictionaries = mutable data that store data and immutable unique keys
"""
elements = {"air":1,"tanah":2,"api":3,"udara":4,"air":2}
print(elements["tanah"]) #shows unique key
elements["petir"]=6 #insert element
print(elements)
print("air" in elements)
print(elements.get("air")) #will return value total how many same mutable data

nigga = elements.get("dark")
print (nigga is None)
print (nigga is not None)

# %%
"""
QUESTION 4 OF 5

What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) A=B True
print(a is b) True
print(a == c) True
print(a is c) False because they are not identical
"""

# %%
"""
Compound Data Structures = nested data in data
"""
buah = {"jeruk":{"number":1,"rasa":"asam"},"apel":{"number":2,"rasa":"manis"}}
jeruk = buah["jeruk"]
print (jeruk)

anggur = {"number":5,"rasa":"manis"} #create new dict
buah["anggur"]=anggur
print(buah)
# %%
"""
Quiz: Count Unique Words
Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.

Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
Convert the list into a data structure that would keep only the unique elements from the list.
Print the length of the container.
"""

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

