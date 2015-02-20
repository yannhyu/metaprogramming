mytree = ('root',
	      ('child-L', 
	       ('child-LL', (), ()),
           ('child-LR', (), ())),
	      ('child-R',
	       ('child-RL', (), ()),
	       ('child-RR', (), ())))

def pre_order_tree_map(function, node, level=0):
	value, left, right = node
	result = [function(level, value)]
	if left: 
		result += pre_order_tree_map(function, left, level+1)
	if right:
		result += pre_order_tree_map(function, right, level+1)

	return result


def print_node(level, value):
	print('    ' * level) + repr(value)
	return value

print pre_order_tree_map(print_node, mytree)