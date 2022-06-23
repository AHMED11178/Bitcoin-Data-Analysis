#Hello this is a test
# In[3]:


# Task 1 
# This program prints the starting and ending dates of the dataset.
# SED is a short for the starting and ending dates.
def SED():
    # Open the input file.
    datesFile = open("dates.txt", "r")
    # Read the first line which is the starting date.
    startingDate = datesFile.readline().rstrip("\n")
    # Loop for saving the last line, which is the ending date, in a variable.
    for line in datesFile:
        endingDate = line.rstrip("\n")
    # Printing the starting date and the ending date of the dataset. 
    print("The starting date of the dataset is %s and the ending date is %s." %(startingDate ,endingDate))
    # Close the file.
    datesFile.close()
    
# Start the program.
SED()


# In[ ]:


# Task 2
# This program prints the day that has the maximum volume of traded bitcoin.
# MVD is a short for the maximum volume date.
def MVD():
    # Open the input files to read.
    volumeFile = open("volume.txt", "r")
    datesFile = open("dates.txt", "r")
    # Creating list and loop to store volumes.
    volumeList = []
    for line in volumeFile:
        line = line.rstrip()
        line = float(line)
        volumeList.append(line)
    # Computing the maximum volume.
    maxVolume = max(volumeList)
    # Creating list and loop to store dates.
    datesList = []
    for line in datesFile:
        datesList.append(line)
    # Finding the index of the maximum volume so we can find its date by the index.
    maxVolumeIndex = volumeList.index(maxVolume)
    maxVolumeDate = datesList[maxVolumeIndex].rstrip()
    # Printing the day that has the maximum volume of traded bitcoin.
    print("The day that has the maximum volume, which is %.1f, of traded bitcoin is %s." %(maxVolume,maxVolumeDate))
    # Close the files.
    datesFile.close()
    volumeFile.close()
    
# Start the program.
MVD()


# In[4]:


# Task 3
# This program prints the day that has the maximum gain in the Bitcoin price.
# MGD is a short for maximum gain date

def MGD():
    # Open the input files to read.
    openFile  = open("open.txt","r")
    closeFile = open("close.txt","r")
    datesFile = open("dates.txt", "r")
    # Creating list and loop to store open prices.
    openList = []
    for line in openFile:
        line = line.rstrip()
        line = float(line)
        openList.append(line)
    # Creating list and loop to store close prices.
    closeList = []
    for line in closeFile:
        line = line.rstrip()
        line = float(line)
        closeList.append(line)
    # Creating list and loop to store dates.
    datesList = []
    for line in datesFile:
        line = line.rstrip()
        datesList.append(line)
    # Creating list and loop to obtain the gain price by subtract openList from closeList.
    differList = []
    for i in range(len(closeList)):
        differList.append(closeList[i] - openList[i])
    # Computing the maximum gain price.
    maxGainPrice = max(differList)
    # Finding the index of the maximum gain price so we can find its date by the index.
    maxGainPriceIndex = differList.index(maxGainPrice)
    maxGainPriceDate = datesList[maxGainPriceIndex].rstrip()
    # Printing the day that has the maximum gain in the bitcoin price.
    print("The maximum gain in the bitcoin price is %f and the date is %s." %(maxGainPrice,maxGainPriceDate))
    # close the files.
    openFile.close()
    closeFile.close()
    datesFile.close()
    
MGD()    


# In[7]:


# Task 4
# This program prints the day that has the maximum drop in the Bitcoin price.
# MDD is a short for maximum drop date

def MDD():
    # Open the input files to read.
    openFile  = open("open.txt","r")
    closeFile = open("close.txt","r")
    datesFile = open("dates.txt", "r")
    # Creating list and loop to store open prices.
    openList = []
    for line in openFile:
        line = line.rstrip()
        line = float(line)
        openList.append(line)
    # Creating list and loop to store close prices.
    closeList = []
    for line in closeFile:
        line = line.rstrip()
        line = float(line)
        closeList.append(line)
    # Creating list and loop to store dates.
    datesList = []
    for line in datesFile:
        line = line.rstrip()
        datesList.append(line)
    # Creating list and loop to obtain the drop price by subtract closeList from openList.
    differList = []
    for i in range(len(openList)):
        differList.append(openList[i] - closeList[i])
    # Computing the maximum drop price.
    maxDropPrice = max(differList)
    # Finding the index of the maximum Drop price so we can find its date by the index.
    maxDropPriceIndex = differList.index(maxDropPrice)
    maxDropPriceDate = datesList[maxDropPriceIndex].rstrip()
    # Printing the day that has the maximum Drop in the bitcoin price.
    print("The maximum Drop in the bitcoin price is %f and the date is %s." %(maxDropPrice,maxDropPriceDate))
    # close the files.
    openFile.close()
    closeFile.close()
    datesFile.close()
    
MDD()


# In[ ]:


# Task 5
# This program prints the average of all closing prices from 20 days ago.
# ACP is a short for average closing prices.

def ACP():
    # Open the input files to read.
    closeFile = open("close.txt","r")
    datesFile = open("dates.txt", "r")
    
    # Seting variables.
    daysAgo = 20
    n = 1
    # Seting a container for the total closing prices.
    container = 0
    
    # Creating list and loop to store close prices.
    closeList = []
    for line in closeFile:
        line = line.rstrip()
        line = float(line)
        closeList.append(line)
    # Creating list and loop to store dates.
    datesList = []
    for line in datesFile:
        line = line.rstrip()
        datesList.append(line)
    # Computing the date from the user.
    day = input("Enter the number of the day: ")
    # loop for prompting the user again for the valid day.
    while not day.isdigit():
        print("Invalid value, please try again.")  
        day = input("Enter the number of the day: ")
            
    month = input("Enter the number of the month: ")
    # loop for prompting the user again for the valid month.
    while not month.isdigit():
        print("Invalid value, please try again.")  
        month = input("Enter the number of the month: ")
            
    year = input("Enter the number of the year: ")
    # loop for prompting the user again for the valid year.
    while not year.isdigit():
        print("Invalid value, please try again.")  
        year = input("Enter the number of the year: ")
    date = month + "/" + day + "/" + year
    # Finding the index of the date so we can take the average of the closing prices.
    dateIndex = datesList.index(date)
    # Loop for suming all closing prices from 20 days ago in the container.
    while n <= daysAgo:
        container  = container + closeList[dateIndex-n]
        n = n + 1
    # Computing the average of all closing prices from 20 days ago.
    Average = container / daysAgo
    # Displaying the result.
    print("The average of all closing prices from 20 days ago of %s is %.2f" %(date, Average))
    # Close the files.
    closeFile.close()
    datesFile.close()
    

# Start the program.
ACP()   


# In[1]:


# Task 6/8
# This program adds new values in the same format as the data already in the dataset to new files. 

def newValues():
    # Creating new files to write.
    dateFile = open("_dates.txt", "w")
    openFile = open("_open.txt", "w")
    highFile = open("_high.txt", "w")
    lowFile = open("_low.txt", "w")
    closeFile = open("_close.txt", "w")
    volumeFile = open("_volume.txt", "w")

    # Sepicify how many times to run the program.
    times = input("How many records you want to enter: ")
    # Raising an error in case of an invalid input(times not an integer).
    if not times.isdigit():
        raise ValueError("Error: Invalid input! the input should be an integer.")

    # Loop for repeating the program as many times as have chosen.
    for i in range(int(times)):
        
        # prompting the user for the new data.
        day = input("Enter the number of the day: ")
        # loop for prompting the user again for the valid day.
        while not day.isdigit():
            print("Invalid value, please try again.")  
            day = input("Enter the number of the day: ")
            
        month = input("Enter the number of the month: ")
        # loop for prompting the user again for the valid month.
        while not month.isdigit():
            print("Invalid value, please try again.")  
            month = input("Enter the number of the month: ")
            
        year = input("Enter the number of the year: ")
        # loop for prompting the user again for the valid year.
        while not year.isdigit():
            print("Invalid value, please try again.")  
            year = input("Enter the number of the year: ")   

        date = month + "/" + day + "/" + year
        
        openPrice = input("Enter the opening price of Bitcoin at the start of the day: ")
        # loop for prompting the user again for the valid value.
        while isfloat(openPrice):
            print("Invalid value, please try again.")  
            openPrice = input("Enter the opening price of Bitcoin at the start of the day: ")   

        high = input("Enter the highest price of Bitcoin within the day: ")
        # loop for prompting the user again for the valid value.
        while isfloat(high):
            print("Invalid value, please try again.")  
            high = input("Enter the highest price of Bitcoin within the day: ")   

        low = input("Enter the lowest price of Bitcoin within the day: ")
        # loop for prompting the user again for the valid value.
        while isfloat(low):
            print("Invalid value, please try again.")  
            low = input("Enter the lowest price of Bitcoin within the day: ")   

        closePrice = input("Enter the closing price of Bitcoin at the end of the day: ")
        # loop for prompting the user again for the valid value.
        while isfloat(closePrice):
            print("Invalid value, please try again.")  
            closePrice = input("Enter the closing price of Bitcoin at the end of the day: ")

        volume = input("Enter the total amount of Bitcoin traded on that day: ")
        # loop for prompting the user again for the valid value.
        while isfloat(volume):
            print("Invalid value, please try again.")  
            volume = input("Enter the total amount of Bitcoin traded on that day: ")   

        # Writing the new values into the new files.
        dateFile.write(date+"\n")
        openFile.write(openPrice+"\n")
        highFile.write(high+"\n")
        lowFile.write(low+"\n")
        closeFile.write(closePrice+"\n")
        volumeFile.write(volume+"\n")
    # Printing a staement that indicates the end of the program.
    print("New data is successfully added")
    
    
    # Close the files.
    dateFile.close()
    openFile.close()
    highFile.close()
    lowFile.close()
    closeFile.close()
    volumeFile.close()
    
    
# Function to test whether the input is float/integer or not.
def isfloat(n):
    try:
        float(n)
        return False
    except ValueError:
        return True
    

# Start the program.
newValues()


# In[2]:


##### Task 7
# This program will validate the new data
# VND is a short for validate new data

def VND():
    
    # Open the input files to read.
    newHighFile  = open("_high.txt", "r")
    newLowFile   = open("_low.txt", "r")
    newDatesFile = open("_dates.txt", "r")
    oldDatesFile = open("dates.txt", "r")
    
    # Creating list and loop to store new high prices.
    newHighList = []
    for line in newHighFile:
        line = line.rstrip()
        line = float(line)
        newHighList.append(line)
        
    # Creating list and loop to store new low prices.
    newLowList = []
    for line in newLowFile:
        line = line.rstrip()
        line = float(line)
        newLowList.append(line) 
        
    # Creating list and loop to store new dates.
    newDatesList = []
    for line in newDatesFile:
        line = line.rstrip()
        newDatesList.append(line)
        
    # Creating list and loop to store old dates.
    oldDatesList = []
    for line in oldDatesFile:
        line = line.rstrip()
        oldDatesList.append(line)
        
    # Seting variables.
    index = 0
    
    # validate that the high price is greater than or equal to the low price.
    for i in newHighList:
        
        if i >= newLowList[index]:
            index = index + 1
        
        else :
            dateError = newDatesList[index]
            print("There is an error in the prices data in %s" %dateError)
            index = index + 1
            
    print("All new prices were checked")
    
    # validate that the new dates does not exist in the old dates list.
    for i in newDatesList:
        
        for j in oldDatesList:
            
            if i == j:
                print("The %s date is already exist" %i)
                
    print("All new dates were checked")    
    
    # Close the files.
    newHighFile.close()
    newLowFile.close()
    newDatesFile.close()
    oldDatesFile.close()
        
            
        
VND()


# In[ ]:


# The menu.
# This menu will help the user to get what he want easily.

def menu() :
    
    # Run the program and display its functions.
    print("Welcome to the bitcoin data analytics software")
    print("Here are the functions that we can do for you")
    print("1. Finding the starting and ending dates of the dataset.")
    print("2. Find the day that has the maximum volume of traded bitcoin.")
    print("3. Find the day that has the maximum gain in the Bitcoin price.")
    print("4. Find the day that has the maximum drop in the bitcoin price.")
    print("5. Find the average of all closing prices from 20 days ago.")
    print("6. Enter new values in the same format as the data already in the dataset and store the updated data to new files..")
    print("7. Check the validity of the new data")
    
    # Prompting the user to choice the function.
    choice = int(input("please enter the number of the function that you want: "))
    
    # Meet the user choice
    if choice == 1 :
        SED()
        
    if choice == 2 :
        MVD()
        
    if choice == 3 :
        MGD()
        
    if choice == 4 :
        MDD()
        
    if choice == 5 :
        ACP()
        
    if choice == 6 :
        newValues()
        
    if choice == 7 :
        VND()
    
menu()


# In[ ]:




