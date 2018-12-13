def do_some_op(x):
	print "Inside the outer function\n"
	
	def inside_func(y):
		print "Inside the inner function\n"
		return y.lower() + " " + x

	return inside_func

print "Only the returned function is initialized\n"
my_new_var = do_some_op("world")

print "\nAfter making a call to inner function"
print my_new_var("hello")