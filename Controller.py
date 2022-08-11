import csv
from operator import itemgetter


class Controller:

    # This function append data to the end of csv file
    def createRecord(self, csvFile):

        print("Column Names\n--------------------------------------")
        print("--------------------------------------------------------------")
        # store user input as a new record
        newRecord = input("Input the record with comma ('csv'')")
        # append the user record to the end of csv file.
        csvFile.append(newRecord)
        print("record appended")

    def editCSV(self, csvFile):
    #This function edit the record on the csv file    def editCSV(self, csvFile):
        rowNumber = int(input("Enter row number to edit: "))# store row number as integer
        columnNumber = int(input("Enter column number to edit: "))# store column number as integer
        newRecord = input("Enter new value: ") # store the new record from user

        csvFile[rowNumber][columnNumber] = newRecord # assign new record to the specified index
        print("The record has been changed")
    # This funciton delete a line that was input from the user
    def deleteLine(self, csvFile):
        lineNumber = int(input("Enter row number to delete: "))
        # uses remove method to delete a user specified line
        csvFile.remove(csvFile[lineNumber])
        print("row deleted")

    #This function stores the sorted column into a list
    # and iterate over in a for loop then print it.
    def sortColumn(self, csvFile):

        # Key=itemgetter(0) --->> this is the first index of the column.
        # reverse = True or False this parameter sort by descending or ascending order.
        firstColumn = sorted(csvFile, key=itemgetter(0), reverse=False)

        # The sorted column is printed by iterating over each row.
        for row in firstColumn:
            print(row)

    #This function receives the input from user and show that line from csv file
    def displayRecord(self, csvFile):
        # lineNumber = input("Enter line numbers: ")
        # # the input turns to integer and iterate over in the loop
        # lineNumber = list(map(int, lineNumber.split(",")))
        # for line in lineNumber:
        #     print("\n")
        #     print(str(line) + ":")
        #     print(str(csvFile[line]))
        #     print("\n")
        for row in csvFile:
            print(row)


    #This function create a new csv file and stores the data from memory
    def exportCSV(self, csvFile):
        with open("export.csv", "w", newline="") as file:  # opening the csv file
            writer = csv.writer(file)# Storing writer object in to the writer variable
            writer.writerows(csvFile) # writing the data to the new file .
            print("File created")

    #This function opens and reads the csv file then store them in a container list
    @staticmethod
    def readFromCSV(fileName):
        dataContainer = []  # create a data container
        try:
            with open(fileName) as file: #opening the csv file
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    dataContainer.append(list(row)) # Appending the rows to the container as the loop continues
        except:
            print("Something went wrong")

        return dataContainer
