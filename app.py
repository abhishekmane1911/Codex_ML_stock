import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from flask import Flask, render_template, request, redirect, url_for, flash
import yfinance as yf
import numpy as np
import pandas as pd 

app = Flask(__name__)
app.secret_key = "your_secret_key"  

def fetch_stock_data(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if stock_data.empty:
            return None, "No data found for the given stock ticker or date range."
        return stock_data, None
    except Exception as e:
        return None, f"Error fetching data: {str(e)}"

def calculate_metrics(stock_data):
    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
    stock_data['50-day MA'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['200-day MA'] = stock_data['Adj Close'].rolling(window=200).mean()
    return stock_data

def visualize_data(stock_data, ticker, graph_type):
    if graph_type == 'candlestick':
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                             open=stock_data['Open'],
                                             high=stock_data['High'],
                                             low=stock_data['Low'],
                                             close=stock_data['Adj Close'],
                                             name=f'{ticker} Candlestick')])
        fig.update_layout(title=f'{ticker} Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
        
        graph_path = f"static/{ticker}_candlestick.html"
        fig.write_html(graph_path)
        return graph_path
    else:
        plt.figure(figsize=(12, 6))
        plt.plot(stock_data['Adj Close'], label=f'{ticker} Price')
        plt.plot(stock_data['50-day MA'], label='50-day Moving Average', linestyle='--')
        plt.plot(stock_data['200-day MA'], label='200-day Moving Average', linestyle='--')
        plt.title(f'{ticker} Stock Price and Moving Averages')
        plt.legend(loc="upper left")
        
        img_path = f"static/{ticker}_stock_analysis.png"
        plt.savefig(img_path)
        plt.close()  
        return img_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       
        ticker = request.form.get('ticker')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        graph_type = request.form.get('graph_type')  

        
        stock_data, error = fetch_stock_data(ticker, start_date, end_date)
        
        if error:
            flash(error, 'error')
            return redirect(url_for('index'))
        
        
        stock_data = calculate_metrics(stock_data)
        
       
        graph_path = visualize_data(stock_data, ticker, graph_type)
        
        return render_template('index.html', ticker=ticker, graph_path=graph_path, stock_data=stock_data.to_html(classes='table table-striped'))
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)