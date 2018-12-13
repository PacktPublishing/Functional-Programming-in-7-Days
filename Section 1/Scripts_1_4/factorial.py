def factorial(n):
	
	result = 1
	
	for x in range(2, n+1):
		result = result * x

	return result

print factorial(4)