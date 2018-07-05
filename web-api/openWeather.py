 #!/usr/bin/env python3
#api from openweathermap.org
import pyowm
 
owm = pyowm.OWM("bc2ab34b16719508a9ba53b2ffbaa4f8")
obs = owm.weather_at_place('Kumasi,GH')
# alternatives
##obs = owm.weather_at_id(2643741)                           # City ID
##obs = owm.weather_at_coords(-0.107331,51.503614)           # lat/lon
w = obs.get_weather()

print("The Wind is: ", w.get_wind())
temp = w.get_temperature('celsius')
print(temp)
print("The Temp is: ",temp['temp'] )
print("The Humidity is: ",w.get_humidity(),"\n")

##reg = owm.city_id_registry()
##print(reg.ids_for('London'))



