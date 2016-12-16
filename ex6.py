# define variables
x = "There are %d types of people." % 10 
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print out variables
print x 
print y 

# this I don't know, but I guess %r & %s are formatters which represent the two string variables (string inside string)
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
# I don't understand the code below
joke_evaluation = "Isn't that joke so funny?! %r"

# don't understand the % sign
print joke_evaluation % hilarious

# two strings 
w = "This is the left side of ..."
e = "a string with a right side."

# add up two strings by + 
print w + e
