x = 123

print "Unique Id of x is", id(x)

y = 123

print "Unique Id of y is", id(y)

print "\n\n After Update\n"

y = y + 1

print "Unique Id of x is", id(x)
print "Unique Id of y is", id(y)