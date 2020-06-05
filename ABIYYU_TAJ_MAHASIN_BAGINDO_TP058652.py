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
        getStatPatient()
    elif option == "5":
        searchPatient()
    elif option == "6":
        print("Goodbye")
    else:
        print("Invalid option, please try again")        
        menu()        

#TODO: Change the return to menu option into a function

def registerPatient():
    # This module registers patients
    patientName = input("Enter patient name: ")
    patientID = input("Enter patient ID: ")
    patientMail = input("Enter patient email: ")
    print("== Groups List ==")
    print("ATO: Asymptomatic Travelled Overseas")
    print("ACC: Asymptomatic Close Contact")
    print("AEO: Asymptomatic Event Outbreak")
    print("SID: Symptomatic Individual")
    print("AHS: Asymptomatic Hospital Staff")
    patientGroup = input("Enter patient group: ")
    patientCondition = input("Any past medical conditions? (A for yes, B for no): ")
    patientZone = input("Enter patient zone (A, B, C, or D): ") #TODO: change lowercase groups to uppercase

    patientData = patientName+";"+patientID+";"+patientMail+";"+patientGroup+";"+patientZone+";"+"N"+";"+"N"+";"+"N"+";"+"N"+";"+"0"+";"+"N"+";"+patientCondition+";"+"X"
    print(patientData)

    with open("patient.txt", "a") as f:
        print(patientData, file = f)

    exitMenu()    
    
def testPatient():
    # This module handles all testing
    my_file = open("patient.txt", "r") # Opens patient database and store in variable content as list
    content = my_file.readlines()

    patientID = input("Enter patient ID: ") # Prompts user to enter patient ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[1] == patientID: # Patient found, things actually start to work here
            print("Testing patient " + newContent[0])

            print(newContent)

            print("Enter test result: ")
            print("1. Positive")
            print("2. Negative")
            testResult = input("Choose option: ")
            
            patientTest, testSolution, testResult = testLaboratory(newContent[3],newContent[5],testResult)                  

            if testSolution == "QHNF" and newContent[11] == "1":
                newSolution = "quarantine in ICU, (No follow-up test required)"
            elif testSolution == "QHNF" and newContent[11] == "2":
                newSolution = "quarantine in hospital normal ward, (No follow up test required)"
            elif testSolution == "HQNF":
                newSolution = "home quarantine, (No follow-up test required)"
            elif testSolution == "QDFR":
                newSolution = "quarantine in designated centres, (Follow-up test required)"
            elif testSolution == "HQFR":
                newSolution = "home quarantine, (Follow-up test required)" 
            elif testSolution == "RU":
                newSolution = "go home and reunite with family, (No follow-up test required)"
            elif testSolution == "CW":
                newSolution = "work, (No follow-up test required)"           
           

            print("Patient should do " + newSolution)

            if patientTest == "t1":
                if testResult == "1":
                    newContent[7] = "1"

            if newContent[5] == "N":
                newContent[5] = "t1"
            elif newContent[5] == "t1":
                newContent[5] = "t2"
            elif newContent[5] == "t2":
                newContent[5] = "t3"
            else:
                print("mampus")

                

            print(newContent[5])
            print(testResult)

            #newPatientData = newContent[0]+";"+       

            break
            

        counter = counter + 1
        
    my_file.close()

    exitMenu()
    
def modifyPatient():
    modifyFeatureA()

def getStatPatient():
    #This module displays the requested statistics
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

    ActiveCaseZoneA = 0
    ActiveCaseZoneB = 0
    ActiveCaseZoneC = 0
    ActiveCaseZoneD = 0

    for element in content:
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

        if newContent[4] == "A" and newContent[10] == "A":
            ActiveCaseZoneA = ActiveCaseZoneA + 1     

        if newContent[4] == "B" and newContent[10] == "A":
            ActiveCaseZoneB = ActiveCaseZoneB + 1 

        if newContent[4] == "C" and newContent[10] == "A":
            ActiveCaseZoneC = ActiveCaseZoneC + 1 

        if newContent[4] == "D" and newContent[10] == "A":
            ActiveCaseZoneD = ActiveCaseZoneD + 1                      
                    
        
        counter = counter+1

    totalTest = str(totalTest)

    patientTested = str(patientTested)

    patientRecovered = str(patientRecovered)

    patientPositiveGroupATO = str(patientPositiveGroupATO)
    patientPositiveGroupACC = str(patientPositiveGroupACC)
    patientPositiveGroupAEO = str(patientPositiveGroupAEO)
    patientPositiveGroupSID = str(patientPositiveGroupSID)
    patientPositiveGroupAHS = str(patientPositiveGroupAHS)

    ActiveCaseZoneA = str(ActiveCaseZoneA)
    ActiveCaseZoneB = str(ActiveCaseZoneB)
    ActiveCaseZoneC = str(ActiveCaseZoneC)
    ActiveCaseZoneD = str(ActiveCaseZoneD)

    print("")
    print("Total tests: " + totalTest)
    print("")
    print("Tested patients: " + patientTested)
    print("")
    print("Patient recovered: " + patientRecovered)
    print("")
    print("Asymptomatic Travelled Overseas tested positive: " + patientPositiveGroupATO)
    print("Asymptomatic Close Contact tested positive: " + patientPositiveGroupACC)
    print("Asymptomatic Event Outbreak tested positive: " + patientPositiveGroupAEO)
    print("Symptomatic Individuals tested positive: " + patientPositiveGroupSID)
    print("Asymptomatic Hostpital Staffs tested positive: " + patientPositiveGroupAHS)
    print("")
    print("Active cases in Zone A: " + ActiveCaseZoneA)
    print("Active cases in Zone B: " + ActiveCaseZoneB)
    print("Active cases in Zone C: " + ActiveCaseZoneC)
    print("Active cases in Zone D: " + ActiveCaseZoneD)
    print("")

    my_file.close()

    exitMenu()

def searchPatient():
    print("e")    

def exitMenu():
    print("Return to menu?")
    print("1. Return to menu")
    print("2. Exit")
    exitOption = input("Choose option: ")

    if exitOption == "1":
        menu()
    elif exitOption == "2":
        print("Goodbye and have a nice day.")
    else:
        print("You entered the wrong option but goodbye and have a nice day. ;)")

def testLaboratory(patientGroup, patientTest, testResult):

    if testResult == "2":
        testResult = "0"

    if patientTest == "N": # First test
                
        if testResult == "1": # First test positive 
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")
                

        elif testResult == "0": # First test negative

            if patientGroup == "ATO":
                testSolution = "QDFR"
            elif patientGroup == "ACC":
                testSolution = "QDFR"  
            elif patientGroup == "AEO":
                testSolution = "QDFR"
            elif patientGroup == "SID":
                testSolution = "HQFR"    
            elif patientGroup == "AHS":
                testSolution = "CWFR"
            else:
                print("Invalid Group")

    elif patientTest == "t1": # Second test

        if testResult == "1": # Second test positive
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")

        elif testResult == "0": # Second test negative

            if patientGroup == "ATO":
                testSolution = "QDFR"
            elif patientGroup == "ACC":
                testSolution = "QDFR"  
            elif patientGroup == "AEO":
                testSolution = "QDFR"
            elif patientGroup == "SID":
                testSolution = "HQFR"    
            elif patientGroup == "AHS":
                testSolution = "CWFR"
            else:
                print("Invalid Group")

    elif patientTest == "t2": # Third test
        
        if testResult == "1": # Third test positive
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")

        elif testResult == "0": # Third test negative

            if patientGroup == "ATO":
                testSolution = "RU"
            elif patientGroup == "ACC":
                testSolution = "RU"  
            elif patientGroup == "AEO":
                testSolution = "RU"
            elif patientGroup == "SID":
                testSolution = "RU"    
            elif patientGroup == "AHS":
                testSolution = "CW"
            else:
                print("Invalid Group")

    return patientTest, testSolution, testResult               
    
def modifyFeatureA():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]

        
        print(newContent)
        if newContent[6] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[7] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[8] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"

        newPatientData = newContent[0]+";"+newContent[1]+";"+newContent[2]+";"+newContent[3]+";"+newContent[4]+";"+newContent[5]+";"+newContent[6]+";"+newContent[7]+";"+newContent[8]+";"+newContent[9]+";"+newContent[10]+";"+newContent[11]+";"+"X\n"
        print(newPatientData)

        newIndex = int(newContent[1]) - 1
        content[newIndex] = newPatientData

        f = open("patient.txt", "w")
        counterIn = 0
        for items in content:
            f.writelines(content[counterIn])
            counterIn = counterIn + 1
        f.close()
            #open and read the file after the appending:
        f = open("patient.txt", "r")
        print(f.read())


        counter = counter + 1


# Run program    
menu()