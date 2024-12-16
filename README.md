<h1> Stock Market Screener</h1>
<p> This project is a Python-based Stock Market Screener that allows users to analyze historical stock price data and visualize it through interactive graphs. The application integrates a Flask web interface for user interaction and modern aesthetics for ease of use.</p>

<h2> Features </h2>

<ul >
    <li>Fetches historical stock data for any company.</li>
    <li>Computes key financial metrics:</li>
    <li>Daily Returns</li>
    <li>Volatility</li>
    <li>Moving Averages</li>
    <li>Supports multiple graph types:</li>
    <li>Line Graph</li>
    <li>Candlestick Graph</li>
    <li>Interactive UI built using Flask and Plotly.</li>
</ul>
<h2> File Structure </h2>

<h4> The file structure is as follows:</h4>

```plaintext
.
├── app.py                # Main Python application
├── templates/
│   └── index.html        # HTML template for the app 
└── README.md             # Project documentation

Installation

Follow these steps to set up the project on your local machine:

Clone the Repository

Run the following command to clone the project:

Bash

git clone <repository-URL>
Navigate into the project folder:

Bash

cd project-folder
Set Up a Virtual Environment

Create a virtual environment:

Bash

python3 -m venv venv
Activate the virtual environment:

On Linux/macOS:
Bash

source venv/bin/activate
On Windows:
Bash

venv\Scripts\activate
Install Dependencies

Run the following command to install all required Python packages:

Bash

pip install -r requirements.txt
Run the Application

Start the application by running:

Bash

python app.py
Open your browser and visit: http://127.0.0.1:5000.

Usage

Open the web application in your browser.
Enter the company's ticker symbol (e.g., TATA, AAPL, GOOGL).
Select the type of graph (Line or Candlestick).
View the stock's historical data, financial metrics, and visualizations.
Dependencies

The following Python libraries are required for the project:

Flask
yfinance
Plotly
Matplotlib
pandas
Install all dependencies using this command:

Bash

pip install -r requirements.txt
Known Issues

Ensure that the stock ticker symbol entered is correct.
Plotly graphs may require an active internet connection.
Future Enhancements

Here are some features that can be added in future updates:

Add more financial metrics like the Sharpe Ratio and Beta.
Include user authentication for personalized stock analysis.
Expand support for global markets, such as the Shanghai Stock Exchange (SSE).
Contribution

Contributions are welcome! Follow these steps to contribute:

Fork the repository.

Create a new branch:

Bash

git checkout -b feature-name
Commit your changes:

Bash

git commit -m "Add feature-name"
Push your changes:

Bash

git push origin feature-name
Create a pull request.

Contact

For any questions or issues, contact us at: youremail@example.com