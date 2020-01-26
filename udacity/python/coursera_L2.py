#%%
"""
+ - * /
** = exponentiation/pangkat
^ = caret / bitwise XOR
% = modulo / sisa bagi ex
// = integer division / div
"""
#%%
print(3 ** 2)

#%%
print(1^0)

#%%

print(4 % 3)
print(3 % 4)
#%%

print(8 // 3)

# %%
#Variables and Assignment Operators
"""
mypopulation = 39834
^               ^
variables name  value

variable names:
-use lowercase
-use "_"

Assignment Operators
+-*/
In variables we can use += / *= / etc
Ex: x %=4 == x = x % 4
"""
x = 5
x %=4
print(x)

# %%
"""
Quiz: Assign and Modify Variables
Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. 
After each comment write a line of code that implements the instruction.

Note that this code uses scientific notation to define large numbers. 
4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

I still dont understand why 10% == 0.9 ???
"""
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff 
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume *= 1.05

# into the reservoir in the days following the storm
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
reservoir_volume -= 2.5e5
# that's piped to arid regions.

# print the new value of the reservoir_volume variable
print (reservoir_volume)



# %%
"""
Quiz: Changing Variable Values
How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.

We're intentionally not providing a place to execute the code here, because we want to help you practice the important skill of walking through lines of code by hand.

Each line of code executes in order, one at a time, with control going from one line to the next.
"""
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
print(crs_per_rab) 

# %%
"""
int = integer = bilangan bulat
float = bilangan koma
"""
#Ex
x = int(4) 
y = float(5.5)
a = int (4.5) #convert to int
b = float (5) #convert to float 
print(x,y,a,b)
# %%
print(.1+.1==.3)

# %%
"""
Write clear and readable code
put opening parentheses after function
Ex : ded(5) correct | ded (5) incorrect
Dont put extra spaces after parentheses
Ex : print(3 * 7) incorrect
Ex : print(3*7 - 1) correct

Limit code 79-99 char per line
"""
# %%
"""
str = String = kata-kata / words
"'\'" = to make a quote following by " '' "
no differences between " " and ' '
you can multiply words 
Indexing words by using [masuin nomor]
len() = length of word ; turn strings into int ; you can even use as math operation ; you cant count int by using len 
"""
#Ex
print("anjing")
print("test anjing \'bangsat'")
mystring = "anjing"
mystring2 = 'babi'
print(mystring,mystring2)
print("\'bangsat'")
#Ex of multiply words
print("anjing"* 5)
#Ex of indexing word
kata = 'anjing'
kata[2]
#Ex of len
print(len("anjing"))
print(len("anjing")/ len("babi"))

# %%
"""
Quiz: Fix the Quote
The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. 
First run it with Test Run to view the error message.
Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.
"""
print('Whether you think you can, or you think you can\'t--you\'re right.') #backslash way
print("Whether you think you can, or you think you can't--you're right.") #doublequote way

# %%
"""
Quiz: Write a Server Log Message
In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.

You’ll be provided with example data for a user, the time of their visit and the site they accessed. 
You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

Use the Test Run button to see your results as you work on coding this piece by piece.
"""

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

print(username+" accesed the site "+url+" at "+timestamp+".")

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."


# %%
"""
Quiz: len()
Use string concatenation and the len() function to find the length of a certain movie star's actual full name.
Store that length in the name_length variable. 
Don't forget that there are spaces in between the different parts of a name!
"""

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name)+len(middle_names)+len(family_name)+2 #add 2 for spacing

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
# %%

"""
Quiz: Total Sales
In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.

Calculate and print the total sales for the week from the data provided.
Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers.
You’ll need to change the type of the input data in order to calculate that total.
"""
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
weekend = int

weekend= int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)
print ("This week's total sales:", weekend)
#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

# %%
"""
String Methods
Format = insert value in string
"""
#Ex of format()
print("ad anjing {}".format(7)) #Use " " incase of str 

# %%
#Another important string method: split()
#Basic split method
mystring = "tulis apa aja anjing"
print (mystring.split())

# %%
# maxsplit argument setelah dari index yg ditulis 
# misal "3" 0-2 misah yg 3 digabung ; use space
mystring = "tulis apa aja anjing babi kimak pantek"
print (mystring.split(' ',3))
# %%
mystring = "tulis apa aja anjing babi kimak pantek"
print (mystring.split('.')) #if there's "." in word, it will be splitted
# %%
mystring = "tulis apa aja anjing babi kimak pantek"
print (mystring.split('.')) #if there's "." in word, it will be splitted
# %%
mystring = "tulis apa aja anjing babi kimak pantek"
print (mystring.split(None,3)) # by none means none. langsung kepisah sampai di index-n

# %%
"""
Quiz: String Methods Coding Practice

What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?

"""
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
print("the index and 'is' {}".format(verse.find('and')))
print("the index and 'you' is {}".format(verse.rfind('you')))
print("the count 'you' is {}".format(verse.count('you')))


# %%
"""
"SyntaxError: unexpected EOF while parsing" 
Take a look at the two lines of code below. 

greeting = "hello"
print(greeting.upper

Executing these lines produces this syntax error message - do you see why?
the parenthesis isnt complete
"""