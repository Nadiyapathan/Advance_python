#synatax:lambda arguments:expression
add = lambda x,y:x+y #simple addition
print(add(5,10))
def add(x,y):
    return x+y
#lambda with map()
numbers=[1,2,3,4,5]
squared=list(map(lambda x:x**2,numbers))
print(squared)