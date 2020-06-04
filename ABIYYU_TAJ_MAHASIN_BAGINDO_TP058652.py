#ABIYYU TAJ MAHASIN BAGINDO
#TP058652

def menu():

    print("Welcome")
    print("1. Register new patient")
    print("2. Test patients")
    print("3. Modify patient status")
    print("4. Statistics")
    print("5. Search")
    print("6. Exit")

    option = input("Choose option : ")

    if option == "1":
        registerPatient()
    elif option == "2":
        testPatient()
    elif option == "3":
        modifyPatient()
    elif option == "4":
        statPatient()
    elif option == "5":
        searchPatient()
    elif option == "6":
        print("Goodbye")
    else:
        print("Invalid option, please try again")        
        menu()        



def registerPatient():
    print("a")
    menu()
    
def testPatient():
    print("b")
    menu()

def modifyPatient():
    print("c")
    menu()

def statPatient():
    #print("d")
    getStatPatient()
    menu()

def searchPatient():
    print("e")    
    menu()

def getStatPatient():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    print(content)
    #content_list = content.split(",")
    my_file.close()

menu()