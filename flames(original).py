a=list(str(input('a: ')))
b=list(str(input('b: ')))
def flame(c,d):
	flames=list('flames')
	for x in enumerate(c):
		for y in enumerate(d):
			if x[1]==y[1]:
				print(x,y)
				c.pop(x[0])
				d.pop(y[0])
				break
		pass
	length=len(c+d)
	while len(flames)!=1:
		flames.pop((length%len(flames))-1)
		print(flames)
	return(c,d,flames)
print(flame(a,b))