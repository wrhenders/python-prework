# Question 1
# Write a funtion to print "hello_USERNAME!" 
# USERNAME is the input of the function

def hello_name(user_name):
    print(f'hello_{user_name}!')

USERNAME = input('Please enter your username: ')
hello_name(USERNAME)


# Question 2
# Write a function, first_odds that prints the odd number from 1-100 
# and returns nothing

def first_odds():
    x = 1
    while x < 100:
        if x % 2 == 1:
            print(x, end=' ')
            x = x+1
        else:
            x = x+1

first_odds()

# Question 3
# Please write a Python function, max_num_in_list 
# to return the max number of a given list.

def max_num_in_list(a_list):
    new_list = sorted(a_list)
    return new_list.pop()

# Question 4
# Write a function to retun if the given year is a leap year. 
# A leap year is divisible by 4 but not divisible by 100, 
# unless it is also divisible by 400. Return Bool

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Question 5
# Write a function to check to see if all numbers in list 
# are consecutive numbers. Return a bool

def is_consecutive(a_list):
    for num in range(len(a_list)-1):
        if a_list[num]+1 == a_list[num+1]:
            check = True
        else:
            check = False
            break
    return check

