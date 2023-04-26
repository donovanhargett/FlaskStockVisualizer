import unittest
from StockFunctions import *
from StockTime import *
from unittest.mock import patch

#Mocking input since most functions don't pass as paramter
#The ones that fail and throw error are due to expection handling in code


class TestStringMethods(unittest.TestCase):
    #1: 
        #Test 1/2 chart type: 1 numeric character, 1 or 2]
        def test_chart_type_valid(self):
            valid_options = ["1", "2"]
            for option in valid_options:
                with patch('builtins.input', return_value=option):
                    self.assertEqual(get_chart_type(), int(option))

        #TEST (2/2) Fails  with an error because of ValueError exception in function
        def test_chart_type_invalid(self):
            invalid_options = ["-1", "0", "3", "9", "_9", "=_9A"]
            valid_option = "2"
            with patch('builtins.print'):
                for invalid_input in invalid_options:
                    with patch('builtins.input', side_effect=[invalid_input, valid_option]):
                        self.assertEqual(get_chart_type(), int(valid_option))   
    #2: 
        #Test(1/2) symbol: capitalized, 1-7 alpha characters
        def test_stock_symbol_valid(self):
            stock_symbols = ['GOOG', 'ABC', 'TSLA', 'SPY']
            for symbol in stock_symbols:
                with patch('builtins.input', return_value=symbol):
                    self.assertEqual(get_stock_symbol(), symbol)
        
       #Test (2/2) = FAILS
        def test_stock_symbol_invalid(self):
            stock_symbol_invalid = ['g00g', 'A3C', 'TS1a', 'sP_']
            valid_symbol = 'GOOG'
            for symbol in stock_symbol_invalid:
                with patch('builtins.input', side_effect=[symbol, valid_symbol]):
                    self.assertEqual(get_stock_symbol(), valid_symbol)
        
        
    #3: 
        #TEST (1/2) TIME SERIES (1-4)
        def test_time_series_valid(self):
            time_series = ["1", "2", "3", "4"]
            with patch('builtins.print'):
                for validInput in time_series:
                    with patch('builtins.input', return_value=validInput):
                        self.assertEqual(get_time_series_option(), int(validInput))

        
        #TEST (2/2) 
        def test_time_series_invalid(self):
           invalid_options = ["-5", "10", "0", "ASDP5", "_1"]
           valid_option = "2"
           incorrect_option = "9"
           with patch('builtins.print'):
               for invalid_input in invalid_options:
                   with patch('builtins.input', side_effect=[invalid_input, valid_option]):
                        self.assertEqual(get_time_series_option(), int(incorrect_option))

                        
    #4: 
        #TEST (1/2) START DATE FORMAT
        def test_start_date_valid(self):
            start_date_valid = ['2022-05-10', '2002-04-26', '2009-05-03', '2004-09-26']
            for date in start_date_valid:
                with patch('builtins.input', return_value=date):
                    self.assertEqual(get_start_date(), datetime.strptime(date, "%Y-%m-%d"))

       
       #TEST (2/2) START DATE INVALID - (FAILS)
        def test_start_date_invalid(self):
            invalid_dates = ['2005-13-09', '2000-02-30', '2021-04-31', '2004-06-00']
            valid_date = '2005-01-09'
            incorrect_date = '2021-01-33'  
            for date in invalid_dates:
                with patch('builtins.input', side_effect=[date, valid_date]):
                    self.assertEqual(get_start_date(), datetime.strptime(incorrect_date, "%Y-%m-%d"))

      #5: 
        #TEST (1/3) END DATE FORMAT 
        def test_end_date_valid(self):
            end_date = datetime.strptime('2002-05-10', "%Y-%m-%d")
            valid_dates = ['2002-05-10', '2022-12-31', '2022-02-28', '2022-06-30']
            for date in valid_dates:
                with patch('builtins.input', return_value=date):
                    self.assertEqual(get_end_date(end_date), datetime.strptime(date, "%Y-%m-%d"))
          
        #TEST (2/2) END DATE FORMAT - (FAILS)
        def test_end_date_invalid(self):
            end_date = datetime.strptime('2022-01-05', "%Y-%m-%d")
            invalid_dates = ['2022-13-01', '2023-02-30', '2022-04-31', '2024-06-00']
            valid_date = '2022-01-02'
            for date in invalid_dates:
                with patch('builtins.input', side_effect=[date, valid_date]):
                    self.assertEqual(get_end_date(end_date), datetime.strptime(valid_date, "%Y-%m-%d"))
     
if __name__ == '__main__':
    unittest.main()

