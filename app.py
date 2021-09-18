import requests
from  flask import  Flask,render_template,request

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=ff126d38ab3a4c8abd524f51e164795c'
    city=""
    weather={}
    if request.method == 'POST':
        city = request.form.get('city')
        resp = requests.get(url.format(city)).json()
        weather={
            'city':city,
            'temperature':resp['main']['temp'],
            'pressure' : resp['main']['pressure'],
            'feels like' : resp['main']['feels_like'],
            'humidity' : resp['main']['humidity'],
            'icon': resp['weather'][0]['icon']
        }
      
    return render_template('index.html',weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
