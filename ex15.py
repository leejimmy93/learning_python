# from sys import argv

# script, filename = argv 

# txt = open(filename) # open a file, which is a argument variable

# print "Here's your file %r:" %filename # print the filname
# print txt.read() # read the content of txt and print it out

print "Type the filename again:"
file_again = raw_input("> ") # set raw_input to a variable

txt_again = open(file_again) # open the variable

print txt_again.read() # read and print out the variable content

txt_again.close() # don't know how to close a file
