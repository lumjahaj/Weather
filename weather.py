from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=5802ad3591f068c58a65e854786e5d23')
    temp = json.loads(r.text)['main']['temp']

    return render_template('weather.html', temp=temp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
