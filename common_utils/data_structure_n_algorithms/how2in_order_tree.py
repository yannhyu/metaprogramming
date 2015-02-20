mytree = ('root',
	      ('child-L', 
	       ('child-LL', (), ()),
           ('child-LR', (), ())),
	      ('child-R',
	       ('child-RL', (), ()),
	       ('child-RR', (), ())))

def in_order_tree_map(function, node, level=0):
	value, left, right = node
	result = []
	if left: 
		result += in_order_tree_map(function, left, level+1)
	result.append(function(level, value))
	if right:
		result += in_order_tree_map(function, right, level+1)

	return result


def print_node(level, value):
	print('    ' * level) + repr(value)
	return value

print in_order_tree_map(print_node, mytree)