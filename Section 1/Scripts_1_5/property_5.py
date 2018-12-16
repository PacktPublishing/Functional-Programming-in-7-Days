def sqr(x):
	return x * x	

def cube(x):
	return x * x * x

def four_pow(x):
	return x * x * x * x

funcs_list = [ sqr, cube, four_pow ]

for fnc in funcs_list:
	print fnc(6)

