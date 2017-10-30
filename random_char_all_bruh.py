from random import randint
def randlist(r,usedlist,done):
	alpha = ['1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',"'",']','[','/',';','`',',','.','~','!','@','#','$','%','^','*',')','(','_','+','}','{','|',':','"','>','<','?','\\']
	#print(len(alpha))
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	done = True
	return c, usedlist,done
def main():
	used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	done = False
	while True:
		r = randint(0,89)
		done = 0
		c,used,done = randlist(r,used,done)
		print(c,end='')
main()
