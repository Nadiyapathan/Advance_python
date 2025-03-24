#Exception  Handling

#Zero Division Error
def numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return"cannot divide by zero!"
    num1 =int(input("enter first number"))
    num2=int(input("enter the second number")) 
    print(numbers(num1,num2))


  #value Error
def add_numbers(num1,num2):
    try:
        result=int(num1)+int(num2)
        return result
    except valueError:
        return "error:both inputs must be valid number!"
    print(add_numbers("10","5"))
    print(add_numbers("10","abc"))
 
