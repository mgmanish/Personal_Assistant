import requests
import malespeaker
import json

def need(s):
	if "news" in s:
		url = "http://127.0.0.1:5000/webhook"
		data = {'result':{"action":"news.search"}}
		s="Here are some news for you..\n"
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url, data=json.dumps(data), headers=headers)
		req = r.json()['speech']
		s+=req
		print(s)
		malespeaker.speak(s)
	elif "weather" in s:
		url = "http://127.0.0.1:5000/webhook"
		data = {'result':{"action":"weather.search"}}
		s="Here is weather report in Delhi for next 2 days\n"
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url, data=json.dumps(data), headers=headers)
		req = r.json()['speech']
		s+=req
		print(s)
		malespeaker.speak(s)



if __name__ == '__main__':
	need("weather")
