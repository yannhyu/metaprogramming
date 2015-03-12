# list comprehension
lst = [ord(i) for i in "ABCDEFGHI"]
print lst
 
# equivalent generator expression
gen = list(ord(i) for i in "ABCDEFGHI")
print gen


lst2 = ['provider.' + i for i in "ABCDEFGHI"]
print lst2

gen2 = list('provider.' + i for i in "ABCDEFGHI")
print gen2
