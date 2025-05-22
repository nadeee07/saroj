def add_student():
    print("you aare add student function")


def update_student():
    print("you are on update student function")



def menu(): 
    print("enter 1 to add student ")
    print()
    print ("enter 2 to update student")
    print("enter 3 to delete student")
    print("enter the 4 to view student")
    print("enter 5 to take attendence")
    print("enter 6 to view attendences")
    print("enter 7 to exit")

option = input( "enter menu No")

while True:
    menu()
    option = input ("Enter menu ni:")
    if option == "1":
        add_student() 

    elif option =="2":
        update_student()
    elif option =="3":
        delete_student()
    elif option =="7":
     print("Exit")
     break 
    else:
        print("Invalid Option")

