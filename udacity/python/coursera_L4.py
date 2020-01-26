# %%
"""
If = conditional statement true or false
== equal to 
!= not equal to 

If
elif harus di ikuti oleh if
else harus ada if or elif dulu

Indentation = block space
Ex
                
"""
# %%
"""
Practice: Which Prize
Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, 
which is stored in the integer variable points.

Points	Prize
1 - 50	wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin
All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. 
If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
If there's no prize, the message should state "Oh dear, no prize this time."

Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174.
You can hide your other inputs by commenting them out.
"""
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
# %%
"""
Quiz: Guess My Number
You decide you want to play a game where you are hiding a number from someone. 
Store this number in a variable called 'answer'. 
Another user provides a number called 'guess'. 
By comparing guess to answer, you inform the user if their guess is too high or too low.

Fill in the conditionals below to inform the user about how their guess compares to the answer.
"""

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 42
guess = 42

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)


# %%
"""
Quiz: Tax Purchase
Depending on where an individual is from we need to tax them appropriately.
The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.
"""

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA"
purchase_amount = 300

if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":#provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

# %%
"""
Complex Boolean Expressions
You can use if statement separately
"""
#Example
if 5 < 1:
    print("anjing")

if 8^2 > 2:
    print("y")

# %%
"""
Good and Bad Examples
1. Dont use true and false as condition because its useless. if statement need true if the condition is false it wont run. same with statement or not
2. careful with writing operations that use logical operators. Examples: and, or, not. because it doesnt have specific meanings
3. Dont compare boolean variable with == True or == false. because same as no.1 useless. 
"""

#Ex
satan = 1 #if >1 will print setan of 0= bangsat if -1 = setan
if satan:
    print("setan")
else:
    print("bangsat")


# %%
"""
Loops
Python have 2 loops. For and while. For is used for iteration and while looping until the statement is fulfilled. 
"""
#Ex
buah = ['apel','jeruk','manggis','sirsak']
for buahbuah in buah: #buahbuah is new variable for iteration variable
    print(buahbuah)
print("")

"""
using range() function for loops.
range is used iteration until that we want
range(start=0, stop, step=1) 
    start iteration. if empty the default is 0
    stop = the last iteration
    step = how many step in sequence
"""
for i in range(5): 
    print(1+1)

# %%
"""
Creating and Modifying Lists
"""
#EX
buah = ['jeruk','mangga','apel','sirsak']
buah_gede = [] #new container for temporary

for buahbuah in buah: #buahbuah container iterative
    buah_gede.append(buahbuah.title()) #capitalise
print(buah_gede)
# %%
#EX
buah = ['jeruk','mangga','apel','sirsak']
for index in range(len(buah)):
    buah[0] = buah[2].title() #it replace strings example buah[0] replaced by buah [2] + capitalise
print(buah)


# %%
"""
Practice: Multiples of 5
Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.

This should output:

5
10
15
20
25
30
"""
for i in range(5,31,5):
    print(i)
# %%
"""
Quiz: Create Usernames
Write a for loop that iterates over the names list to create a usernames list. 
To create a username for each name, make everything lowercase and replace spaces with underscores. 
Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores. 
Check out how to use this method in this Stack Overflow answer.
"""
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ','_'))

print(usernames)
# %%
"""
Quiz: Modify Usernames with Range
Write a for loop that uses range() to iterate over the positions in usernames to modify the list.
Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. 
After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
"""
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ','_')

print(usernames)
# %%
"""
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
XML is a data language similar to HTML. 
You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.
"""
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
# %%
"""
Quiz: Create an HTML List
Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list.
For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. 
Following that is one line per element in the source list, surrounded by <li> and </li> tags. 
The final line of the string should be the closing tag </ul>.
"""

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print(html_str)

# %%
"""
Building Dictionaries
"""
#Method 1: Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {} #empty container

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)


# %%
#Method 2: Using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)

# %%
#Iterating Through Dictionaries with For Loops
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
#it only print keys
for key in cast:
    print(key)

#if you want print both key and values use "built-in"
for key, value in cast.items():
    print("actor: {} role: {}".format(key, value))
# %%
"""
Quiz: Fruit Basket - Task 1
You would like to count the number of fruits in your basket. 
In order to do this, you have the following dictionary and list of fruits. 
Use the dictionary and list to count the total number of fruits, but you do not want to count the other items in your basket.
"""
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items(): #buat iteration baru tapi masuin basket items
    if fruit in fruits: #jadi fruit = fruits dicocokan
        result += count #jumlahin
    

#if the key is in the list of fruits, add the value (number of fruits) to result
print(result)
# %%
"""
Quiz: Fruit Basket - Task 2
If your solution is robust, you should be able to use it with any dictionary of items to count the number of fruits in the basket. 
Try the loop for each of the dictionaries below to make sure it always works.
"""
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count 
print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count 
print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count 
print(result)

# %%
"""
So, a couple of things about the above examples:

It is a bit annoying having to copy and paste all the code to each spot - wouldn't it be nice to have a way to repeat the process without copying all the code? Don't worry! You will learn how to do this in the next lesson!

It would be nice to keep track of both the number of fruits and other items in the basket.
Use the environment below to try out this second part.
"""
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        fruit_count += count 
    else:
        not_fruit_count += count
        
#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print(fruit_count, not_fruit_count)
# %%
"""
While Loops = selama condition belum terpenuhi akan jalan terus sampai terpenuhi
"""
#Ex
card = [4,3,63,22,434,53,56,64,31,32,4353,343,543]
hand = [] #empty container
while sum(hand) <= 10:
    hand.append(card.pop()) #remove index usually in last
print(hand)

# %%
"""
Practice: Factorials with While Loops
Find the factorial of a number using a while loop.

A factorial of a whole number is that number multiplied by every whole number between itself and 1. 
For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.
We can write a while loop to take any given number and figure out what its factorial is.
Example: If number is 6, your code should compute and print the product, 720.
"""
# %%
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
# multiply the product so far by the current number
    product *= current
# increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

"""
Practice: Factorials with For Loops
Now use a for loop to find the factorial!

It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, but this time, using a for loop. 
Try it in the code editor below!
"""
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number+1):
    product *= num
# print the factorial of number
print(product)
# %%
"""
Quiz: Count By Check
Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

Now in addition, address what would happen if someone gives a start_num that is greater than end_num. 
If this is the case, set result to "Oops! Looks like your start value is greater than the end value. 
Please try again." Otherwise, set result to the value of break_num.
"""
start_num = 1#provide some start number
end_num = 10#provide some end number that you stop when you hit
count_by = 2#provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
if start_num > end_num:
    result = 'Oops! Looks like your start value is greater than the end value. Please try again.'
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
print(result)
# %%
"""
Quiz: Nearest Square
Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. 
A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.
"""
# %%
limit = 40
num = 0
# write your while loop here
while (num+1)**2 < limit:
    num += 1
    
    nearest_square = num**2

print(nearest_square)
# %%
"""
For loops vs while loops
for is using iterative that we want
while is will repeat until the condition is met.
"""
# %%
"""
Solution: What type of loop should we use?
Question: You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. 
If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

Our solution: 
We would write a while loop to write this code for the following reasons:

We don't need a break statement that a for loop will require. Without a break statement, a for loop will iterate through the whole list, which is not efficient.
We don't want to iterate over the entire list, but only over the required number of elements in the list that meets our condition.
It is easier to understand because you explicitly control the exit conditions for the loop.

Here's the code we wrote:
"""
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0
list_sum = 0
i = 0
len_num_list=len(num_list)
print(len_num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print(count_odd)
print(list_sum)

# %%
"""
Break = 
continue =
"""
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
print('method 1') #if the weight is more 100 it will break the loops
weight = 0 
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight {}'.format(weight))
    if weight >= 100:
        print('break')
        break
    else:
        print('adding {} ({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("final weight: {}".format(weight))
print("final item: {}".format(items))

# %%
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
print('method 2')
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight {}'.format(weight))
    if weight >= 100:
        print('break')
        break
    elif weight + cargo_weight > 100:
        print('skipping {} ({})'.format(cargo_name,cargo_weight))
        continue
    else:
        print('adding {} ({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("final weight: {}".format(weight))
print("final item: {}".format(items))

# %%
"""
Quiz: Break the String
Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. 
You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. 
If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 
Consider adding print statements to your code to help you resolve bugs.
"""
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]


print(news_ticker)
# %%
"""
Coding Quiz: Check for Prime Numbers
Prime numbers are whole numbers that have only two factors: 1 and the number itself. 
The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.
1 X 6 = 6
2 X 3 = 6
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

If the numbers are prime, the code should print "[number] is a prime number."
If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
Example output:
"""
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
for num in check_prime: #iteration in check prime
    for i in range(2, num): #range to dimulai dari 2
        if (num % i) == 0:
            print('{} is NOT a prime number, because {} is a factor of {}'.format(num,i,num))
        
        if i == num-1: 
            print('{} IS a prime number'.format(num))
## HINT: You can use the modulo operator to find a factor

# %%
"""
Zip: combining 2 containers into one
"""
#Ex
china = ['cin','conk','chink']
chino = [7,6,3,] #misal ad value yg tdk sesuai di container tdk akan terbaca ex: ada '5' dichino tp china ga ad value jd gakebaca

for china, chino in zip(china,chino):
    print('{},{}'.format(china,chino))

"""
Unzip=kebalikan dari zip, separating the container
"""
chink_chonk = [('anjing',1),('babi',2),('cacing',3)]
chink,chonk = zip(*chink_chonk)
print(chink,chonk)

"""
enumerate = adding index number/key to value container
"""
# %%
#Ex
word = ['a','b','c','d','e']
for i, words in enumerate(word): #buat 2 new iterative i, and words
    print(i,words)
# %%
"""
Quiz: Zip Coordinates
Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. 
Each string should be formatted as label: x, y, z. 
For example, the string for the first coordinate should be F: 23, 677, 4.
"""
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels,x_coord,y_coord,z_coord):
    points.append('{}: {}, {}, {}'.format(*point))

for point in points:
    print(point)

# %%
"""
Quiz: Zip Lists to a Dictionary
Use zip to create a dictionary cast that uses names as keys and heights as values.
"""
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))
print(cast)

# %%
"""
Quiz: Unzip Tuples
Unzip the cast tuple into two names and heights tuples.
"""
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names,heights = zip(*cast)
print(names)
print(heights)

# %%
"""
Quiz: Transpose with Zip
Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. 
There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
"""
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# %%
"""
Quiz: Enumerate
Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".
"""
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, character in enumerate(cast):
    cast[i]=character + " " + str(heights[i])

print(cast)

# %%
"""
List comprehensions
in python we can mempersingkat penggunaan iterative looping if by using list compherensions. dimana masukin if ke container
"""
#ex
china = ['JNJFE','WDWN']
lower_china = [low.lower() for low in china]
print(lower_china)

# %%
"""
conditionals in list compherension
you can use conditiona after following by iterative
in case else it should start by if else then for
"""
#ex
square = [x**2 for x in range(9) if x%2 == 0]
print(square)
square2 = [x**2 if x%2==0 else x+3 for x in range(9)]
print(square2)

# %%
"""
Quiz: Extract First Names
Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
"""
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [first.split()[0].lower() for first in names]# write your list comprehension here
print(first_names)
# %%
"""
Quiz: Multiples of Three
Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
"""
multiples_3 = [x*3 for x in range(1,21)]
print(multiples_3)
# %%
"""
Quiz: Filter Names by Scores
Use a list comprehension to create a list of names passed that only include those that scored at least 65.
"""
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65] #dictionary 

print(passed)