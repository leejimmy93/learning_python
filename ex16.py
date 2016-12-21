from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)." # this is new stuff 
print "If you want that, hit RETURN."

raw_input("?") # raw input start with ?

print "Opening the file..."
target = open(filename, 'w') # open a file, with write

# print "Truncating the file. Goodbye!" # print 
# target.truncate() # empty target 

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:") # raw input
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

# target.write(line1) # write to target 
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write("%s\n%s\n%s\n" %(line1, line2, line3))

target.close()

print "Type the filename again:"
target_again = raw_input("> ")
txt_again = open(target_again)
print txt_again.read()

print "And finally, we close it."
txt_again.close() # close target 
