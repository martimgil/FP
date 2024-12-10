def add(n1, n2):
	print("{} + {} = {}".format(n1,n2,n1+n2))

def subtract(n1,n2):
	print("{} - {} = {}".format(n1,n2,n1-n2))

def multiply(n1,n2):
	print("{} x {} = {}".format(n1,n2,n1*n2))

def divide(n1,n2):
	print("{} / {} = {}".format(n1,n2,n1/n2))



def main():
	n1 = int(input("n1 - "))
	n2 = int(input("n2 - "))
	print("You can do one of the folowwing things: \n[A] - add them\n[S] - subtract them\n[M] - multiply them\n[D] - divide them\n")
	option = str(input("What would you like to do? - "))
	if option=="A":
		add(n1,n2)
	elif option=="B":
		subtract(n1,n2)
	elif option=="M":
		multiply(n1,n2)
	elif option=="D":
		divide(n1,n2)
main()
		