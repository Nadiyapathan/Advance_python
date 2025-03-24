#index error
string=input("enter the string name")
index=int(input("enter the index"))

try:
    char=string[index]
    print(char)
except indexError:
    print("error:index is out of range!")


    #acessing an out of range index in a list:
    my_list=[10,20,30,40,50,]    

    try:
        print(my_list[10])
    except IndexError:
        print("error:index is out of range!")
