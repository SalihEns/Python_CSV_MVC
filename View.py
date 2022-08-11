
import csv
import Controller


Controller = Controller.Controller()

#This function gets input from a user and assign that input value in a switch case
#structure for each option. And options are inside a while loop structure exits because
# after each option the loop starts over again and ask the user
# if they want to manipulate the data agagin
@staticmethod
def view():
    while True:
        print("---------program by Salih.--------- ")
        print("Options:")
        print(" 1-load records\n 2-create record\n 3-display record\n"
              " 4-sort Column\n 5-edit record\n 6-Export csv\n 7-delete\n 8-Quit")
        option = input("Enter a number: ")

        if option == "1":
            try:
                csvData = Controller.readFromCSV(
                    'Monthly_average_retail_prices.csv')
            except:
                print("Error occurred when loading the data")
                break

            print("The data is loaded\n")

        elif option == "2":
            Controller.createRecord(csvData)

        elif option == "3":
            Controller.displayRecord(csvData)

        elif option == "4":
            Controller.sortColumn(csvData)

        elif option == "5":
            Controller.editCSV(csvData)

        elif option == "6":
            Controller.exportCSV(csvData)
        elif option == "7":
            Controller.deleteLine(csvData)
        elif option == "8":
            print("Quit")
            break
        else:
            print("Please enter a valid option")

class View:
    pass



