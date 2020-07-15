# %%
"""
Defining function = def
used to make function inside def with local variable inside them 
"""
#Ex
def rectangle(height, width):
    return height * width

print(rectangle(10,5))

# %%
"""
Print vs return in def
print wont return value in def it only print
return will give value in def 
"""
#Ex
def test(num):
    print(num+10)

def test2(num):
    return(num+10)

print(test(10))
print(test2(10))

# %%
"""
Default argument
use default argument for a function
"""
#Ex
def triangle(base=4,height=10):
    return 0.5 * base * height

print(triangle(input()))

# %%
"""
Quiz: Population Density Function
Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. 
I've included two test cases that you can use to verify that your function works correctly. 
Once you've written your function, use the Test Run button to test your code.
"""
# write your function here
def population_density(population,land_area):
    return (population/land_area)



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# %%
"""
Quiz: readable_timedelta
Write a function named readable_timedelta. 
The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
For example, calling the function and printing the result like this:
"""
 # write your function here
def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return('{} week(s) and {} day(s).'.format(weeks,remainder))
# test your function
print(readable_timedelta(10))

# %%
"""
Variable scope = jangkauan variable that can be used. 
if you make variable inside def function it only can be used inside them if call the variable outside it will print error
if there are 2 variable outside def and inside it will be choosen the inside one.
"""
#Ex
def test():
    word = 'hello bangsat'

print(word)
#Error

# %%
"""
Another method that can be used for variable scope
"""
def test():
    word = 'hello'
    return(word)

def test2():
    word = 'bangsat'
    return(word)

test(),test2()

# %%
"""
Another method
"""
word = 'bangsat'

def test():
    return(word)

def test2():
    return(word)

test(),test2()

# %%
"""
Lambda
anonymous variables used in function jd u gaperlu repot2 lagi. ???
"""
#Ex
multiply = lambda x, y: x * y

multiply(5,3)

# %%
"""
Quiz: Lambda with Map
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().
"""
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x)/len(x), numbers))
print(averages)

# %%
"""
Quiz: Lambda with Filter
filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)