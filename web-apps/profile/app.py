from flask import Flask,render_template,request,redirect,url_for
import pyowm
import tweepy

app = Flask(__name__)

images = {"https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-09-100135_1440x900_scrot.png":
          "Generate rsa ssh key with ssh-keygen on Raspberry Pi",
          "https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-09-102402_1440x900_scrot.png":
          "Using rsa ssh key to secure information exchange over the networks connected",
          }
showcase = {"https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-09-100135_1440x900_scrot.png":
          "Generate rsa ssh key with ssh-keygen on Raspberry Pi",
          "https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-09-102402_1440x900_scrot.png":
          "Using rsa ssh key to secure information exchange over the networks connected",
           "https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-10-155103_1440x900_scrot.png":
            "Push souce code to GitHub.com",
            "https://raw.githubusercontent.com/idawud/GlobalCode-18/dawud/miscellaneous/2018-07-10-140042_1440x900_scrot.png":
            "Using 'pip' utility to download and manage packages and libraries. eg pip freeze list all installed modules",
            "https://raw.githubusercontent.com/idawud/GlobalCode-18/master/flask%20server.png":
            "Running flask web servers from the bash shell"
            }

@app.route('/')
def index():
    return render_template('index.html',images = images)


@app.route('/weather/', methods = ['POST','GET'])
def weather():
    if request.method =='POST':
        place = request.form['location']
        owm = pyowm.OWM("bc2ab34b16719508a9ba53b2ffbaa4f8")
        obs = owm.weather_at_place(place)
        w = obs.get_weather()
        temp = w.get_temperature('celsius')
        data = [ temp['temp'], w.get_humidity() ,place]
        return render_template('weather.html',data=data)
    elif request.method == "GET":
        return render_template('weather.html')

@app.route('/showcase')
def screenshots():
    return render_template('showcase.html',showcase = showcase)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tweet')
def tweets():
    try:
        consumer_key = 'UkzbSCI3JxtZnUMh3gqDZwtul'
        consumer_secret = 'WbxTQqfN6fvJMqbmVGCm6lAjogKimXfz5Efbsmbm0prY1vlGx8'
        access_token = '200545877-BowytW4loVLGB5Tk0eGNe6y3v1boD1suWwznVurs'
        access_token_secret = '	ihqHSFiVOYx2GJBPu9h6JMrOyHeqFKgFDbd5PYSoaAikp'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        return render_template('tweet.html',public_tweets = public_tweets)
    except:
        return render_template('tweet.html')

if __name__ == "__main__":
    app.run(debug =True, host='0.0.0.0')