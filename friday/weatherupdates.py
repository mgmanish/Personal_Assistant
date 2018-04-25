from weather import Weather
import malespeaker
import transcribe
import gui


def fun(q):
	weather = Weather()
	malespeaker.speak("Please tell me the city you are interested in")
	#x=transcribe.transcribe_file()
	print("city: ")
	x=input()
	location = weather.lookup_by_location(x)
	condition = location.condition()
	#print(condition.text())

	# Get weather forecasts for the upcoming days.
	s=""
	forecasts = location.forecast()
	i=2
	for forecast in forecasts:
	    s += forecast.text()
	    s+="\n"+forecast.date()
	    s+="\n"+forecast.high()+"(max F)  "+forecast.low()+"(min F)"
	    s+="\n\n"
	    i+=1
	    if i>5:
	    	break
	print(s)

if __name__ == "__main__":
	fun("hello")
