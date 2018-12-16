def square(x):
	return x * x

def my_func(var_x, var_func):
	var_result = var_func(var_x)
	return var_result

new_var = my_func(5, square)
print new_var