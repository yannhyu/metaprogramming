def range_2d(width, height):
    ''' produce a stream of two dimensional coordinates '''
    for y in range(height):
    	for x in range(width):
    		yield x, y


# usage
my_width = 5
my_height = 4

for col, row in range_2d(my_width, my_height):
	print "(%d, %d)" % (col, row),
	if col == 3 and row == 3:
	    break
