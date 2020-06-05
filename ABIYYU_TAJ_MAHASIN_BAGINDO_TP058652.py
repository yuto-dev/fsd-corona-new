#ABIYYU TAJ MAHASIN BAGINDO
#TP058652

def menu():
    # First page of the program, prompts user to choose between the 5 options available
    print("Welcome")
    print("1. Register new patient")
    print("2. Test patients")
    print("3. Modify patient status")
    print("4. Statistics")
    print("5. Search")
    print("6. Exit")
    # Receives input from user
    option = input("Choose option : ")
    # Runs function depending on the user input
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

def registerPatient():
    # This module registers patients
    patientName = input("Enter patient name: ")
    patientID = input("Enter patient ID: ")
    patientMail = input("Enter patient email: ")
    print("== Groups List ==")  # Prints the list of groups for users to refer to
    print("ATO: Asymptomatic Travelled Overseas")
    print("ACC: Asymptomatic Close Contact")
    print("AEO: Asymptomatic Event Outbreak")
    print("SID: Symptomatic Individual")
    print("AHS: Asymptomatic Hospital Staff")
    patientGroup = input("Enter patient group: ")
    patientCondition = input("Any past medical conditions? (1 for yes, 2 for no): ")
    patientZone = input("Enter patient zone (A, B, C, or D): ") #TODO: change lowercase groups to uppercase

    # Combines all data into one variable

    patientData = patientName+";"+patientID+";"+patientMail+";"+patientGroup+";"+patientZone+";"+"N"+";"+"N"+";"+"N"+";"+"N"+";"+"0"+";"+"N"+";"+patientCondition+";"+"X"

    # Store patient data to text file
    with open("patient.txt", "a") as f:
        print(patientData, file = f)

    # Function to prompt user whether they want to go back to the main menu
    # or exit the program
    exitMenu()    
    
def testPatient():
    # This module handles all patient testing.
    my_file = open("patient.txt", "r") # Opens patient database and store in the variable content as a list.
    content = my_file.readlines()

    patientID = input("Enter patient ID: ") # Prompts user to enter patient ID.

    counter = 0 # Set counter for the for loop.

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent.
        del newContent[-1] # Delete the extra index to remove "\n".
        

        if newContent[1] == patientID: # Patient found, things actually start to work here.
            print("Testing patient " + newContent[0]) # Shows the user who is being tested.

            print("Enter test result: ") # Prompts user to choose the test result.
            print("1. Positive")
            print("2. Negative")
            testResult = input("Choose option: ")
            
            # Sends patient data to the function testLaboratory for patient testing.
            patientTest, testSolution, testResult, positive = testLaboratory(newContent[3],newContent[5],testResult)                  

            # Prints advice for patient based on their test result according to 
            # Table 2 in the assignment question.
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
           
            # Advices patient on what they should do.
            print("Patient should do " + newSolution)

            # Assign new test number, test result, case ID, and status to 
            # patient data depending on the test outcome.
            if patientTest == "N":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[6] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t1"
                    newContent[6] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()
            elif patientTest == "t1":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[7] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t2"
                    newContent[7] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()
            elif patientTest == "t2":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[8] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t3"
                    newContent[8] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()

            # The function patientBuilder takes in a list (the patient data) and 
            # combines all indexes with a semicolon in between to separate the data.
            newPatientData = patientBuilder(newContent)
            
            # Index is the location of the patient data in the main patient list.
            # Patient ID is subtracted by 1 due to indexes start from 0 while ID start from 1.
            newIndex = int(newContent[1]) - 1
            content[newIndex] = newPatientData

            # Opens the text file where all data is stored and writes everything
            # in the text file sequentially, overwriting the previous data.
            f = open("patient.txt", "w")
            counterIn = 0
            for items in content:
                f.writelines(content[counterIn])
                counterIn = counterIn + 1
            f.close()
                         


            #newPatientData = newContent[0]+";"+       

            break
            
        # Counter increment for the for loop to browse through the patient list
        counter = counter + 1
        
    my_file.close()

    exitMenu()
    
def modifyPatient():
    # This module executes different functions that modify
    # patient data based on user input.
    print("Available options")
    print("1. Set all non-active positive patients' status to positive")
    print("2. Modify patient status")
    print("3. Return to main menu")
    option = input("Choose option: ")

    if option == "1":
        modifyFeatureA()
    elif option == "2":
        modifyFeatureB()
    elif option == "3":
        menu()
    else:
        print("Wrong option, please choose from the")
        modifyPatient()        

def getStatPatient():
    #This module displays all the requested statistics by the assignment question.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    print(content)

    counter = 0

    # Initializes variables.
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

    # loops through all patients.
    for element in content:
        newContent = content[counter].split(";")
        del newContent[-1]
        print(newContent)
        # Amount of patient tested increases when the index 5
        # of a patient shows that it has been tested.
        if newContent[5] != "N":
            patientTested = patientTested + 1

        # Checks all the test results, the total test counter
        # increments when there is a test result in a patient's data.
        if newContent[6] != "N":
            totalTest = totalTest + 1
        if newContent[7] != "N":
            totalTest = totalTest + 1
        if newContent[8] != "N":
            totalTest = totalTest + 1    
        # Counter increments when a patient status says recovered.
        if newContent[10] == "R":
            patientRecovered = patientRecovered + 1       
        # If a patient belongs to the ATO group and one of the test result says
        # positive, the counter increments.
        if newContent[3] == "ATO" and newContent[6] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[7] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[8] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        # If a patient belongs to the ACC group and one of the test result says
        # positive, the counter increments.
        if newContent[3] == "ACC" and newContent[6] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[7] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[8] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        # If a patient belongs to the AEO group and one of the test result says
        # positive, the counter increments.
        if newContent[3] == "AEO" and newContent[6] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[7] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[8] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        # If a patient belongs to the SID group and one of the test result says
        # positive, the counter increments.
        if newContent[3] == "SID" and newContent[6] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[7] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[8] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        # If a patient belongs to the AHS group and one of the test result says
        # positive, the counter increments.
        if newContent[3] == "AHS" and newContent[6] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[7] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[8] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1   
        # When a patient belongs to zone A and has a case ID
        # the counter increments.
        if newContent[4] == "A" and newContent[10] == "A":
            ActiveCaseZoneA = ActiveCaseZoneA + 1     
        # When a patient belongs to zone B and has a case ID
        # the counter increments.
        if newContent[4] == "B" and newContent[10] == "A":
            ActiveCaseZoneB = ActiveCaseZoneB + 1 
        # When a patient belongs to zone C and has a case ID
        # the counter increments.
        if newContent[4] == "C" and newContent[10] == "A":
            ActiveCaseZoneC = ActiveCaseZoneC + 1 
        # When a patient belongs to zone D and has a case ID
        # the counter increments.
        if newContent[4] == "D" and newContent[10] == "A":
            ActiveCaseZoneD = ActiveCaseZoneD + 1                      
                    
        # Counter increments for the for loop to browse through
        # all the patients
        counter = counter+1
    # Converts total test counter to string for concatenation.
    totalTest = str(totalTest)
    # Converts patients tested counter to string for concatenation.
    patientTested = str(patientTested)
    # Converts patients recovered counter to string for concatenation.
    patientRecovered = str(patientRecovered)
    # Converts positive patients based on group counter to string for concatenation.
    patientPositiveGroupATO = str(patientPositiveGroupATO)
    patientPositiveGroupACC = str(patientPositiveGroupACC)
    patientPositiveGroupAEO = str(patientPositiveGroupAEO)
    patientPositiveGroupSID = str(patientPositiveGroupSID)
    patientPositiveGroupAHS = str(patientPositiveGroupAHS)
    # Converts active cases based on zone counter to string for concatenation.
    ActiveCaseZoneA = str(ActiveCaseZoneA)
    ActiveCaseZoneB = str(ActiveCaseZoneB)
    ActiveCaseZoneC = str(ActiveCaseZoneC)
    ActiveCaseZoneD = str(ActiveCaseZoneD)
    # Concatenate all data and print all data. 
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
    # Prompts user to go back to the main menu or exit the program
    exitMenu()

def searchPatient():
    # This module executes different functions that search
    # patient data based on user input.

    # Prints all the available options
    print("Available options")
    print("1. Patient records")
    print("2. Case status")
    print("3. Deceased patient records")
    print("4. Return to main menu")
    option = input("Choose option: ")
    # Executes funtion based on user input
    if option == "1":
        searchFeatureA()
    elif option == "2":
        searchFeatureB()
    elif option == "3":
        searchFeatureC()
    elif option == "4":
        menu()    
    else:
        print("Wrong option, please choose from the")
        modifyPatient()    

def exitMenu():
    # This function is used throughout the program
    # to prompt user whether they want to go back
    # to the main menu or exit the program.
    print("Return to menu?")
    print("1. Return to menu")
    print("2. Exit")
    exitOption = input("Choose option: ")

    if exitOption == "1":
        menu()
    elif exitOption == "2":
        print("Goodbye and have a nice day.")
    else: # Easter egg
        print("You entered the wrong option but goodbye and have a nice day. ;)")

def patientBuilder(patient):
    # Important function that combines patient data into one string
    patientData = patient[0] +";"+ patient[1] +";"+ patient[2] +";"+ patient[3] +";"+ patient[4]+";"+patient[5]+";"+patient[6]+";"+patient[7]+";"+patient[8]+";"+patient[9]+";"+patient[10]+";"+patient[11]+";"+"X\n"
    return patientData

def testLaboratory(patientGroup, patientTest, testResult):
    # Function where different patients are tested and return
    # different values based on patient data received.

    # Converts test result to binary kinda.
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

            positive = 1    # This variable is kinda useless, you can ignore it.
                            # I want to delete it but I don't want to risk ruining the whole program.
                            # "If it works don't touch anything."
                

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

            positive = 0    

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

            positive = 1     

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

            positive = 0    

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

            positive = 1     

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

            positive = 0
    # If patient tests positive or has done all 3 tests.
    else:
        print("No tests required for this patient, returning to main menu")
        testSolution = 0
        positive = 0
        menu()            

    return patientTest, testSolution, testResult, positive               
    
def modifyFeatureA():
    # This is the first function of the modify patient data
    # module. It sets all non-active cases to active when a patient
    # is infected. However it's kinda useless since patients case turns active
    # when they test positive. I added it because it's in the assignment question.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]

        # If one of the test results show positive and
        # the patient's status is N or neutral, it will be changed
        # to A or active
        if newContent[6] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[7] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[8] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        # Combines all data into one string with the very useful function patientBuilder.
        # I love this function it makes my time coding this program so much easier in certain parts.
        newPatientData = patientBuilder(newContent)

        # Index is ID - 1 because index starts at 0 as opposed to 1.
        newIndex = int(newContent[1]) - 1
        content[newIndex] = newPatientData

        # Writes patient data sequentially.
        f = open("patient.txt", "w")
        counterIn = 0
        for items in content:
            f.writelines(content[counterIn])
            counterIn = counterIn + 1
        f.close()
            #open and read the file after the appending:

        # Counter for the for loop to progress
        counter = counter + 1
    # Success message!
    print("All active patients' status has been changed to Active!")
    # Prompts user to go back or leave
    exitMenu()    

def modifyFeatureB():
    # Second function for the third module.
    # Allows user to modify active patients' status to
    # Recovered or Deceased, preferably the former.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    patientID = input("Enter patient ID: ") # Prompts user to enter patient ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[1] == patientID: # Patient found, things actually start to work here
            # Prompts user to choose the new status.
            print("Modify patient " + newContent[0] + "'s status to?")
            print("1. Recovered")
            print("2. Deceased")
            print("3. Go back to the main menu")
            option = input("Choose option: ")
            # Sets status based on user input.
            if option == "1":
                newContent[10] = "R"
            elif option == "2":
                newContent[10] = "D"
            elif option == "3":
                menu()
            # Combines data to one string.
            newPatientData = patientBuilder(newContent)

            newIndex = int(newContent[1]) - 1
            # Index is id - 1 because index starts at 0
            content[newIndex] = newPatientData
            # Opens text file and write everything sequentially.
            f = open("patient.txt", "w")
            counterIn = 0
            for items in content:
                f.writelines(content[counterIn])
                counterIn = counterIn + 1
            f.close()
            
            # prompts user to go back or leave because this only happen once.
            exitMenu()

        counter = counter + 1    

def searchFeatureA():
    # First feature of the final module.
    # Allows user to look for patient record based on their name
    # or ID.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    # Prints options.
    print("Available options")
    print("1.Search by name")
    print("2.Search by ID")
    option = input("Choose option: ")
    # If user chooses name.
    if option == "1":
        patientName = input("Enter patient name (case sensitive): ")

        counter = 0
        # Browse through all the patients
        for element in content:

            newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
            del newContent[-1]

            if newContent[0] == patientName: # Patient found, things actually start to work here
                # Translates the initials in the patient data into
                # actual words for user to read.
                if newContent[10] == "N":
                    status = "Healthy"
                elif newContent[10] == "A":
                    status = "Infected"
                elif newContent[10] == "R":
                    status = "Recovered"
                elif newContent[10] == "D":
                    status = "Deceased"
                else:
                    status = "status not found"
                # Again, same thing. Translates data.
                if newContent[11] == "1":
                    cond = "Yes"
                elif newContent[11] == "2":
                    cond = "No"
                else:
                    print("condition not found")        
                # Prints patient record.
                print("---------------------------------")
                print("Patient name: " + newContent[0])
                print("Patient ID: " + newContent[1])
                print("Patient mail: " + newContent[2])
                print("Patient group: " + newContent[3])
                print("Patient zone: " + newContent[4])
                print("Patient status: " + status)
                print("Have any past medical condition: " + cond)
                print("---------------------------------")
                # another exit prompt.
                exitMenu()

            counter = counter + 1
    # If user chooses ID
    elif option == "2":

        patientID = input("Enter patient ID: ")

        counter = 0
        # browses through all patient data
        for element in content:
            
            newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
            del newContent[-1]

            if newContent[1] == patientID: # Patient found, things actually start to work here
                # same thing, translations.
                if newContent[10] == "N":
                    status = "Healthy"
                elif newContent[10] == "A":
                    status = "Infected"
                elif newContent[10] == "R":
                    status = "Recovered"
                elif newContent[10] == "D":
                    status = "Deceased"
                else:
                    status = "status not found"
                # more translations.
                if newContent[11] == "1":
                    cond = "Yes"
                elif newContent[11] == "2":
                    cond = "No"
                else:
                    print("condition not found")        
                # print user records.
                print("---------------------------------")
                print("Patient name: " + newContent[0])
                print("Patient ID: " + newContent[1])
                print("Patient mail: " + newContent[2])
                print("Patient group: " + newContent[3])
                print("Patient zone: " + newContent[4])
                print("Patient status: " + status)
                print("Have any past medical condition: " + cond)
                print("---------------------------------")
                # exit prompt.
                exitMenu()

            counter = counter + 1

def searchFeatureB():
    # Second feature, allows user to search for
    # case status based on case ID.

    # read data base.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    caseID = input("Enter case ID: ") # Prompts user to enter case ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[9] == caseID: # Patient found, things actually start to work here
            # Translate patient status from data to English.
            if newContent[10] == "A":
                status = "Active"
            elif newContent[10] == "R":
                status = "Recovered"
            elif newContent[10] == "D":
                status = "Deceased"
            else:
                status = "status not found"            
            # prints case status.
            print("---------------------------------")
            print("Patient status for case " + newContent[9] + " is " + status)
            print("---------------------------------")
            # yay exit prompt.
            exitMenu()
        # counter increment
        counter = counter + 1            

def searchFeatureC():
    # third feature of the search module.
    # Allows user to look for deceased patients'
    # records.

    # read database.
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        # filters patients to deceased only.
        if newContent[10] == "D":
            # checks whether patient has pre-existing
            # medical conditions.
            if newContent[11] == "1":
                cond = "Yes"
            elif newContent[11] == "2":
                cond = "No"
            else:
                print("condition not found")        
            # print records
            print("---------------------------------")
            print("Patient name: " + newContent[0])
            print("Patient ID: " + newContent[1])
            print("Patient mail: " + newContent[2])
            print("Patient group: " + newContent[3])
            print("Patient zone: " + newContent[4])
            print("Patient case ID: " + newContent[9])
            print("Have any past medical condition: " + cond)
            print("---------------------------------")
        # counter to browse through data.
        counter = counter + 1    
    # exit prompt            
    exitMenu()

# Run program    
menu()

#成功だ！