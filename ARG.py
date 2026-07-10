def is_required(name, rollno):
    print("name:",name , "rollno:", rollno)

def is_default(name,sy=4):
    print("name:",name, "class; ",sy)

def is_multiple(*favsub):
    print("favourite subject:",favsub)


# is_required("sarthak", 19)

# is_default("sarthak",5)
# is_default("sahil")

# is_multiple("sarthak", "Maths")

# is_multiple("sarthak", "maths","PL","deld")
 
sub1 = input("please enter your favourite subject : ")
is_multiple(sub1)

name=input("please Enter your name :")
srno=input("please enter your class :")
is_default(name,srno)

