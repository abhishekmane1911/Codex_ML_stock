# Stock Market Screener

This project is a Python-based Stock Market Screener that allows users to analyze historical stock price data and visualize it through interactive graphs. The application integrates a Flask web interface for user interaction and modern aesthetics for ease of use. The generated images of stock screener get saved in static folder

## Features

- Fetches historical stock data for any company.
- Computes key financial metrics:
  - Daily Returns
  - Volatility
  - Moving Averages
- Supports multiple graph types:
  - Line Graph
  - Candlestick Graph
- Interactive UI built using Flask and Plotly.

## File Structure

The file structure is as follows:

- `app.py`: The main Python application (Flask backend).
- `templates/`: Contains HTML templates.
  - `index.html`: The main UI for the stock screener.
- `static/`: Contains static files like stylesheets and images.
- `README.md`: Documentation file for the project.

## Installation

Follow these steps to set up the project on your local machine:

### Clone the Repository

Run the following command to clone the project:

```bash
 git clone https://github.com/abhishekmane1911/Codex_ML_stock
 cd project-folder
```
### Run the Application

Start the application by running:
 ```bash
 python app.py
```
Open your browser and visit: http://127.0.0.1:5001.

## Usage

1. Open the web application in your browser.
2. Enter the company's ticker symbol (e.g., TATAMOTORS.NS, AAPL, GOOGL).
3. Select the type of graph (Line or Candlestick).
4. View the stock's historical data, financial metrics, and visualizations.

## Dependencies

The following Python libraries are required for the project:

- Flask
- yfinance
- Plotly
- Matplotlib
- pandas

Install all dependencies using this command:

```bash
pip install -r requirements.txt
```
## Known Issues

- Ensure that the stock ticker symbol entered is correct.
- Plotly graphs may require an active internet connection.

## Future Enhancements

Here are some features that can be added in future updates:

- Add more financial metrics like the Sharpe Ratio and Beta.
- Include user authentication for personalized stock analysis.


## Contact

For any questions or issues, contact us at: abhishekmane1911@gmail.com