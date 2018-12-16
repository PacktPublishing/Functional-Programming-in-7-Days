def do_some_op(x):
	def func_square_add(y, z):
		return y * y + z
	return func_square_add(x, x+1)


my_new_var = do_some_op(4)
print my_new_var