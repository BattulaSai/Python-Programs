l =[0,1,2,3,4,5,6,7,8,9]
k = []
for i in l:
	if i not in k:
		k.append(i)
print sorted(k)
print k[::-1]
print [x + y for x, y in zip(k, l)]
