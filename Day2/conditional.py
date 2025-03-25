#Lambda function to check if a number is even or odd
check=lambda x :"Even" if x % 2 == 0 else "odd"
num=int(input("enter the number:"))
result=check(num)
print(f"the number {num} is {result}")

# Lambda function to check if a number is greater than 10
check_greater_than_10 =lambda x:"yes" if x>10 else "no"
num =int(input("enter the number: "))
result =check_greater_than_10(num)
print(f"Is{num} greater than 10?{result}")