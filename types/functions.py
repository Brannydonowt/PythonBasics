# References for functions

# interestingly, a python function can return multiple values
# https://python.land/return-multiple-values-from-function

# example function definition

def say_hello():
    print('Hello World')

say_hello()

# IMPORTANT
# Indenting is extremely important
# indentation defines code blocks, as opposed to {}

# function with paramter
def say_helloto(name):
    print('Hi', name)
    # ^ Note this print syntax
    # It adds a space too
say_helloto('Random GitHub Stalker')

# function with default parameters
# We cannot mix default and non default parameters
def default_param(example='Look!', target='A Shark!'):
    print(example, target)

default_param()




