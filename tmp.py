#/bin/python
# fxn of this script

def read_restaurant():

	file_r=open("./restaurant.txt", "r")
	file_w1=open("output.txt","w")
	tmp = [] 
	count = 0	

	for line in file_r:
		count = count + 4
		tmp.append(line)
	
	file_w1.writelines(tmp)
	file_r.close()
	file_w1.close()
	return 

read_restaurant()
	   



