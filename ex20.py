from sys import argv # import module

scripts, input_file = argv # argument variable and unpack in order

def print_all(f): # define a function
	print f.read() # print the f

def rewind(f): # define a function
	f.seek(0) # don't understand, set the 

def print_a_line(line_count, f): # define a function
	print line_count, f.readline() # readline don't understand

current_file = open(input_file) # assign a file object

print "First, let's print the whole file:\n" # print something

print_all(current_file) # use defined function to print curren_file

print "Now let's rewind, kind of like a tape." # print

rewind(current_file) # rewind? what this is doing?

print "Let's print three lines:" # print something

current_line = 1 # assign a variable
print_a_line(current_line, current_file) # use defined function to print 

current_line = 2
print_a_line(current_line, current_file)

current_line = 3
print_a_line(current_line, current_file)

