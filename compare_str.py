a = str(input())
b = str(input())
def compare_str(a, b):
	if type(a) == str and type(b) == str:
		if a == b:
			return ('1')
		elif len(a) > len(b):
				return ('2')
		elif b == ('learn'):
				return ('3')
	else :
		return ('0')
compare_str(a, b)
print (compare_str(a, b))