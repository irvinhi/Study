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

"""
Variable scope = jangkauan variable that can be used. 