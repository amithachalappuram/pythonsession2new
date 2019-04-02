f = open('/Users/amitha/Desktop/atvars assignment/santa_input1.txt')
floor = f.read()
z = floor.count('(') - floor.count(')')
print "Floor is :", z 