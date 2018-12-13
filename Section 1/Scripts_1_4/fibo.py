def fib(n):
	num1 = 0
	num2 = 1
	count = 2
	if n == 0:
		return
	elif n == 1:
		print num1
	elif n >= 2:
		print num1, num2,

	while count <= n:
		num3 = num1 + num2
		print num3,
		count += 1
		num1 = num2
		num2 = num3
	return

fib(5)

