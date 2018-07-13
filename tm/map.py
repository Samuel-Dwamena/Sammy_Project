import pyowm
 
owm = pyowm.OWM('d37998eec5775d4dcf2ea1e34fe319fb')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()
