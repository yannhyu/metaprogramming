def reverse_list_1(lst):
    return lst[::-1]

def reverse_list_2(lst):
    lst.reverse()
    return lst

def reverse_list_3(lst):
    lst = list(reversed(lst))
    return lst

print reverse_list_1([0,1,2,3])
print reverse_list_2([0,1,2,3])
print reverse_list_3([0,1,2,3])
