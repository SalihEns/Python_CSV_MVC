class Record:

    #Name of the csv file. 
    csv_file = 'Monthly_average_retail_prices.csv'
    
    #Constant Column Names
    COLUMN_NAMES = ['Jan_20',  'Feb_20','Mar_20','Apr_20',
    'May_20','Jun_20', 'Jul_20',  'Aug_20','Sep_20','Oct_20',
    'Nov_20','Dec_20 ','Jan_21 ','Feb_21 ','Mar_21 ','Apr_21 ', 'May_21 ',
    'Jun_21','Jul_21', 'Aug_21', 'Sep_21', 'Oct_21','Nov_21','Dec_21',
    'Jan_22', 'Feb_22', 'Mar_22']
    
    #Constructor
    def __init__(self,csv_file) :
       self.csv_file = csv_file
    
    
   


    
        
    