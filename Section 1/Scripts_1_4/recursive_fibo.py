def fibo_rec(n):
    if n == 0:
    	return 0
    elif n == 1:
    	return 1
    else:
    	return fibo_rec(n-1)+fibo_rec(n-2)


n = 10

for i in xrange(0, 10):
	print fibo_rec(i),