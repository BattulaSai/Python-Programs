#Coded by Battula sai

with open("pallindrome.txt",'r') as f:  #Opening a file
	i = f.read()                    #Reading a file
	l = i.split()                   #Splitting file into words and inserting in a list.
k = []                                  #Declaration of new list
for word in l:                          #For word in list
	t = word[::-1]                  #Reverse the word in list and store in a variable t
	k.append(t)                     #Append the reversed data into a newly declared list k 
print k                                 #Prints the list k
result = set(l).intersection(k)         #Compares the list l and k and returns the common words in a file. 
print result                            #Prints those common words
j = max(result, key=len)                #To find maxing length pallindrome from above result.
print j                                 #Prints the longest pallindrome in the file.
f.close()                               #Closing a file
