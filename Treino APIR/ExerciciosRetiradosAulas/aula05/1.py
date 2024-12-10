def inputFloatList():
	lst=[]
	n1=input("N: ")
	while n1!="":
		lst.append(float(n1))
		n1=input("N: ")
	
	return lst
	
def countLower(lst,v):
	count=0
	for a in lst:
		if a<v:
			count+=1
	return count

def minmax(lst):
	min = lst[0]
	max = lst[1]
	
	for v in lst:
		if v<min:
			min=v
		elif v>max:
			max=v
	return min, max
	
def main():
	lst = inputFloatList()
	min, max = minmax(lst)
	media = (min+max)/2
	print(media)
	print(countLower(lst,media))

main()