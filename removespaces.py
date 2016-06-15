#Program to remove spaces in a string

def removespaces(s):
	l = []
	for i in xrange(len(s)):
		if s[i] != ' ':
			 l.append(s[i])
	return tostring(l)

#To join final output
def tostring(l):
	return ''.join(l)


#Main program starts here
s = raw_input("Enter the string : \n")
print removespaces(s)   #function call removespaces

