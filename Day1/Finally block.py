def perfrom_operation():
    try:
        num1=10
        num2=5
        result=num1/num2
        print(f"Result of division:{result}")
    except ZeroDivisionError:
         print(f"Error:cannot div by Zero")
    finally:   
        print("operation is complete.")
perfrom_operation() 
print()      

def perfrom_operation():
    try:
        num1=10
        num2=0
        result=num1/num2
        print(f"Result of division:{result}")
    except ZeroDivisionError:
         print(f"Error:cannot div by Zero")
    finally:   
        print("operation is complete.")
perfrom_operation() 
print()      


