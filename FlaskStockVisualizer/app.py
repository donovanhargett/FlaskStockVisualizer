from flask import Flask, render_template, request, redirect, url_for
from StockFunctions import *
from StockTime import *
from ping import *
from RenderGraph import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def graph():
    graph_data = None
    start_time = None
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        chart_type = (request.form['chart_type'])
        time_series_option = int(request.form['time_series_option'])
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

        if time_series_option == 1:
            start_time = get_start_time()
            if start_time != None:
                start_date = datetime.combine(start_date, start_time)
                end_date = datetime.combine(end_date, start_time)

        data = pingAPI(time_series_option, stock_symbol, start_date, end_date)

        if start_time != None:
            start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
            end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            start_date_str = start_date.strftime("%Y-%m-%d")
            end_date_str = end_date.strftime("%Y-%m-%d")

        graph_data = render_graph(chart_type, start_date_str, end_date_str, data, stock_symbol)

    return render_template("graphing.html", graph_data=graph_data, stock_symbol=csv_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)