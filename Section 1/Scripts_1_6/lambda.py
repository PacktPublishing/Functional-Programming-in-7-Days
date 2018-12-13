my_sqr = lambda x: x * x
my_prod = lambda x,y : x * x

print "Square of 5 is ",my_sqr(5)

print "Product of 5 and 7 is", my_prod(5, 7)

list_str = [ 'aa', 'bbbb', 'c', 'dddddd']
dict_str = { 1: 'a', -2: 'bbbb', 3: 'c', 4:'dddddd'}

print sorted(dict_str, key = lambda x: len(dict_str[x]))