my_list = [1, 2, 3]

print my_list
print "Unique ID of my_list is", id(my_list)

my_list.append(4)
my_list.append(5)

print "\nAfter Update\n"
print my_list
print "Unique ID of my_list is", id(my_list)