# import functions for the Stock Data Visualizer
from StockFunctions import *
from StockTime import *
from ping import *
from RenderGraph import *
from flask import Flask, render_template, request, redirect, url_for



def main():
    cont = "y"
    while(cont == "y"):
        start_time = None
        print("Stock Data Visualizer\n------------------------\n")
    
        # function to get the stock symbol from user
        stock_symbol = get_stock_symbol() 
    
        print("\n\nChart Types\n--------------\n1. Bar\n2. Line\n")
    
        # function to get chart type from user
        chart_type = get_chart_type() 
    
        # Call the function to get the time series option from the user
        time_series_option = get_time_series_option()

        # If the time series is 1, we need at time as well
        if time_series_option == 1:
            start_time = get_start_time()

        # Call the function to get the start date from the user
        start_date = get_start_date()
        # if there is a time, we need to combine it with the date
        if(start_time != None):
            start_date = datetime.combine(start_date, start_time)

        # Call the function to get the end date from the user
        end_date = get_end_date(start_date)
        # if there is a time we need to combine it with the date
        if(start_time != None):
            end_date = datetime.combine(end_date, start_time)

        # pings API and gathers information then stores it in an array
        data = pingAPI(time_series_option, stock_symbol, start_date, end_date)

        # We need to get a start/end date string for the title, so I converted the start_date to a string
        if(start_time != None):
            start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
            end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            start_date_str = start_date.strftime("%Y-%m-%d")
            end_date_str = end_date.strftime("%Y-%m-%d")

        # render the graph in the browser
        graph = render_graph(chart_type, start_date_str, end_date_str, data, stock_symbol)

        # asking the user to continue
        return render_template('results.html', graph=graph)
    

    print("Goodbye!")

main()



