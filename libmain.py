import activity_1 

lib=activity_1.functions()
user=activity_1.users()

while True:
    print("\n Sarthak Library")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book ")
    print("4. Display all books")
    print("5.to add user ")
    print("6.remove user")
    print("7. display all users")
    print("8. Exit")



    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        lib.addbook(title)
    elif choice == 2:
        title = input("Enter book title: ")
        lib.borrowbook(title)
    
    elif choice == 3:
        title = input("Enter book title: ")
        lib.returnbook(title)   
        print("BOOK RETURNED SUCCESS FULLY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ")

    elif choice == 4:
        print("\n alll available books are :")
        lib.display()

    elif choice == 5:
        user = input("Enter user name: ")
        user.adduser(user)  \
    
    elif choice==6: 
        user = input("Enter user name: ")
        user.removeuser(user)  \
    
    elif choice==7:
        print("\n alll available users are :")
        user.display()    

    elif choice == 8:
        print("Exited Successfully,  Thank you for using Sarthak LIbrary ")
        break
    
    