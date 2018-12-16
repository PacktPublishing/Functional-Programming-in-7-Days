def square( x ):
	return x * x

print "Using original function name"
print square( 6 )


func_var = square
print "Using variable"
print func_var( 6 )