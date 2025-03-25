#square of list
numbers=[1,2,5,6,9,10]
squared_numbers=list(map(lambda x:x**2,numbers))

print("squared_numbers:",squared_numbers)

#add 2 to each number
numbers=[1,2,3,4,5]
updated_numbers=list(map(lambda x:x+2,numbers))

print(f"Numbers after adding2:{updated_numbers}")