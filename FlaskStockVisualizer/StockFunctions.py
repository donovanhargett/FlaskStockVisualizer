#Functions to get stock information from user
import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row[0])
    return data
csv_data = read_csv_file('stocks.csv')


def get_stock_symbol():
    x = True
    while x is True:
        stock_symbol = input("Enter the stock symbol you are looking for: ")
        if stock_symbol == "":
            print('Please enter a stock symbol')
            x = True
        else:
            return stock_symbol

#function to get chart type from user as user input
def get_chart_type():
    i = True
    while i is True:
        try:
            chart_type = int(input("Enter the chart type you want (1,2): "))
            i = False
        except ValueError:
            print('Please enter an integer')
            i = True
        if chart_type <= 0 or chart_type > 2 or chart_type == "":
            print("Please choose option 1 or 2")
            i = True
        
    return chart_type
