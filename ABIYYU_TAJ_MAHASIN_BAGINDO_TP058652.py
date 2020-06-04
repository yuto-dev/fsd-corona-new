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
    
def testPatient():
    print("b")

def modifyPatient():
    print("c")

def statPatient():
    #print("d")
    getStatPatient()

def searchPatient():
    print("e")    

def getStatPatient():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    print(content)

    counter = 0

    patientTested = 0

    for ele in content:
        newContent = content[counter].split(";")
        del newContent[-1]
        print(newContent)
        
        if newContent[5] != "N":
            patientTested = patientTested + 1

        counter = counter+1

    patientTested = str(patientTested)

    print("There are " + patientTested + " patients tested")    

    

    #content_list = content.split(",")
    my_file.close()

    patientTested = 0
    patientRecovered = 0
    patientPositiveGroup = 0
    ActiveZoneCase = 0


menu()