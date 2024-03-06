from flask import Flask, request, jsonify
import tvDatafeed as tv
from config import app_config

app = Flask(__name__)

@app.route('/')
def default():
    return 'UP'

@app.route('/get_hist', methods=['POST'])
def get_hist():
    data = request.json
    username = app_config["USERNAME"]
    password = app_config["PASSWORD"]
    stock_symbol = data.get('stock_symbol', 'AOT')
    tvx = tv.TvDatafeed(username, password)
    hist_data = tvx.get_hist(stock_symbol, 'SET', interval=tv.Interval.in_daily, n_bars=5000)
    
    # Get the last row of the DataFrame
    last_row = hist_data.iloc[-1:].to_dict(orient='records')[0]

    return last_row

if __name__ == "__main__":
    app.run(debug=app_config["DEBUG"])