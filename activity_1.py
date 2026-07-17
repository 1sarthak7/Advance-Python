
class functions():
    def __init__(self):
        self.books = []

    def addbook(self,book):
        self.book=book
        self.books.append(book)
        print("book added successfully !!!!!!!!!!")

    def borrowbook( self,title):
        self.title=title
        if title in self.books:
            self.books.remove(title)
            print("book borrowed successfully !!!!!!!!!!")
        else:
            print("book not found !!!!!!!!!!")
    
    def returnbook(self,book):
        self.book=book
        self.books.append(book)
        print("book Returned successfully !!!!!!!!!!")
    
    def display(self):
        print("Available books: ",self.books)


class users():
    def __init__(self):
        self.users = []

    def adduser(self,user):
        self.user=user
        self.users.append(user)
        print("user added successfully !!!!!!!!!!")

    def removeuser( self,user):
        self.user=user
        if user in self.users:
            self.users.remove(user)
            print("user removed successfully !!!!!!!!!!")
        else:
            print("user not found !!!!!!!!!!")
    
    def display(self):
        print("Available users: ",self.users)
