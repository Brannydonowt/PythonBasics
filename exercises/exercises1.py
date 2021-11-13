import sys

def get_python_ver():
    print(sys.version)

# 1 - Calculate the multiplication and sum of two numbers
# given two ints, return their product if it is greater than 1000, else return their sum.
def exercise1():
    in1 = int(input(["Please Enter a first number"]))
    in2 = int(input(["Please Enter a second number"]))

    prod = in1 * in2
    if prod > 1000:
        return in1 + in2
    else:
        return prod

# 2 - print the sum of the current number and previous number
# iterate the first 10 numbers in each iteration, print the sum of the current and previous number
def exercise2():
    for x in range(0, 10):
        prev = 0
        if x - 1 >= 0:
            prev = x - 1
        print (f"Current Number {x} Previous Number {prev} Sum: {x + prev}")

# 3 - accept a user string and display that characters at an even index
def exercise3():
    usrStr = input(["Please enter a string"])
    index = 0
    for char in usrStr:
        if index % 2 == 0:
            print (char)
        index += 1

# 4 - remove first n characters from a string
# there is a remove_chars() method
def exercise4():
    inputstring = input(["Please enter a string"])
    toRemove = int(input(["How many characters shall I trim?"]))

    if (toRemove > len(inputstring)):
        print("You asked for too many characters to be trimmed...")
        exercise4()
        return

    x = inputstring[toRemove:]
    print(x)

# 5 - check first and last member of list is the same
def exercise5():
    numbers = [10, 20, 30, 40, 10]

    if (numbers[0] == numbers[len(numbers) - 1]):
        return True
    else:
        return False


# 6 - Display numbers divisble by 5 from a list
def exercise6():
    list = [10, 25, 13, 100, 3, 27]

    for i in list:
        if i % 5 == 0:
            print (i)

# 7 - return the count of a given substring from a string
# .count method returns instances of a sublist in a list
def exercise7():
    str_x = "John likes to eat Bacon. John likes meat. John is a meat-eater"
    print (str_x.count("John"))

# 8 - Check palindrome number
# palindrome is a number that is the reversed, e.g 545
def exercise8():
    num1 = 121
    reversed = 0

    number = num1
    while number > 0:
        remainder = number % 10
        reversed = (reversed * 10) + remainder
        number = number // 10

    if reversed == num1:
        print("Number is palindrome")
    else:
        print("Number is not a palindrome")

# 9 - Create a list from two lists
# Add odd numbers from list 1, even numbers from list 2
def exercise9():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    newlist = []
    
    for i in list1:
        if i % 2 > 0:
            newlist.append(i)

    for i in list2:
        if i % 2 == 0:
            newlist.append(i)

    print(newlist)

# 10 - Calculate income tax for a given income
# include taxable incomes so as
# first 10K = 0%
# next 10K = 10%
# the remaining = 20%
# e.g 45K, 10000*0% + 10000*10% + 25000*20% = $6000
def exercise10(wage):
    tax = 0

    if wage <= 10000:
        return 0
    
    if wage <= 20000:
        return 1000

    remaining = wage - 20000

    tax = (remaining * 0.2) + 1000

    print (tax)





        
    

