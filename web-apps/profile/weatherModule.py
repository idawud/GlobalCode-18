 #!/usr/bin/env python3
#api from openweathermap.org
import pyowm
def weather(place):
    owm = pyowm.OWM("bc2ab34b16719508a9ba53b2ffbaa4f8")
    obs = owm.weather_at_place(place)
    w = obs.get_weather()
    temp = w.get_temperature('celsius')
    return [ temp['temp'], w.get_humidity() ]


if __name__ == "__main__":
    print(weather("Accra, GH"))




