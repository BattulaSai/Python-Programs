def reverse(s):                  #Reverse function   
	list = tolist(s)         #returns list from tolist
	r = len(list) - 1        #making pointers for traversing left to right
	l = 0 
	while l < r:             #Conditon 
	
		if not isAlphabet(list[l]): #If not alphabet skip it
			l += 1
		
		elif not isAlphabet(list[r]): #If not alphabet skip it
			r -= 1

		else:                       #This condition executes when the letters are alphabets 
			list[l] , list[r] = swap(list[l] ,list[r])    #Swapping takes place
			l += 1                                        #Increment the pointers
			r -= 1
		
	return tostring(list)  


def isAlphabet(x):              #Checking the letter is alphabet or not  
	return x.isalpha()


def tolist(string):             #Inserting elements into list
	list = []               
	for i in string:
		list.append(i)
	return list

def tostring(list):             #Joins the letters and return to reverse function    
	return ''.join(list)

def swap(a,b):                  #swaps the letters
	return b,a


#Main program starts here
s = raw_input("Enter the string : \n")     #Taking input
string =reverse(s)                         #Calling reverse function 
print "Output string:" + string            #prints final output


#Sample input  a,b$c
#Sample output c,b$a
