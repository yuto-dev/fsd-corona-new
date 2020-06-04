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

    totalTest = 0

    patientTested = 0

    patientRecovered = 0

    patientPositiveGroupATO = 0
    patientPositiveGroupACC = 0
    patientPositiveGroupAEO = 0
    patientPositiveGroupSID = 0
    patientPositiveGroupAHS = 0

    ActiveZoneCase = 0

    for ele in content:
        newContent = content[counter].split(";")
        del newContent[-1]
        print(newContent)

        if newContent[5] != "N":
            patientTested = patientTested + 1

        if newContent[6] != "N":
            totalTest = totalTest + 1
        if newContent[7] != "N":
            totalTest = totalTest + 1
        if newContent[8] != "N":
            totalTest = totalTest + 1    

        if newContent[10] == "R":
            patientRecovered = patientRecovered + 1       

        if newContent[3] == "ATO" and newContent[6] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[7] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[8] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1

        if newContent[3] == "ACC" and newContent[6] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[7] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[8] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1

        if newContent[3] == "AEO" and newContent[6] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[7] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[8] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1

        if newContent[3] == "SID" and newContent[6] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[7] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[8] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1

        if newContent[3] == "AHS" and newContent[6] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[7] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[8] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1             
                    
        
        counter = counter+1

    totalTest = str(totalTest)

    patientTested = str(patientTested)

    patientRecovered = str(patientRecovered)

    patientPositiveGroupATO = str(patientPositiveGroupATO)
    patientPositiveGroupACC = str(patientPositiveGroupACC)
    patientPositiveGroupAEO = str(patientPositiveGroupAEO)
    patientPositiveGroupSID = str(patientPositiveGroupSID)
    patientPositiveGroupAHS = str(patientPositiveGroupAHS)

    print("Total tests : " + totalTest)
    print("Tested patients : " + patientTested)
    print("Patient recovered : " + patientRecovered)
    print("Asymptomatic Travelled Overseas tested positive: " + patientPositiveGroupATO)
    print("Asymptomatic Close Contact tested positive: " + patientPositiveGroupACC)
    print("Asymptomatic Event Outbreak tested positive: " + patientPositiveGroupAEO)
    print("Symptomatic Individuals tested positive: " + patientPositiveGroupSID)
    print("Asymptomatic Hostpital Staffs tested positive: " + patientPositiveGroupAHS)

    my_file.close()

# Run program    
menu()