n=3
lst = [8,1,8,8,8]

for a in lst:
	if lst.count(a)>2:
		c = lst.count(a) - n
		for b in range(c):
			d = lst.index(a)
			lst.pop(d)


print(lst)