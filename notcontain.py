def notinelement(l,k):
	for i in l:
		if i in k:
			continue
		else:
			print i

l = [1,2,3,4,5,6,7,8,9]
k = [4,5,6,7]
notinelement(l,k)
