mytree = ('root',
	      ('child-L', 
	       ('child-LL', (), ()),
           ('child-LR', (), ())),
	      ('child-R',
	       ('child-RL', (), ()),
	       ('child-RR', (), ())))

def post_order_tree_map(function, node, level=0):
	value, left, right = node
	result = []
	if left: 
		result.extend(post_order_tree_map(function, left, level+1))
	if right:
		result.extend(post_order_tree_map(function, right, level+1))

	result.append(function(level, value))
	return result


def print_node(level, value):
	print('    ' * level) + repr(value)
	return value

print post_order_tree_map(print_node, mytree)