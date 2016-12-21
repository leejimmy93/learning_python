tabby_cat = "\tI'am tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat."

fat_cat_1 = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

fat_cat_2 = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat_1
print fat_cat_2

print tabby_cat + persian_cat + backslash_cat + "\n" + "%s" %'snow' + "%r" %'snow'  

# while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r"%i, 
