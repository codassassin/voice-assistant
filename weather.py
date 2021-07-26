import requests
from ss import *
import geocoder
import pyttsx3


g = geocoder.ip('me')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def weather():
    api_address = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(g.latlng[0]) + "&lon=" + \
                                                        str(g.latlng[1]) + "&appid=" + api_store().key("openWeather")

    json_data = requests.get(api_address).json()

    temperature = round(json_data["current"]["temp"]-273, 1)
    wind_speed = json_data["current"]["wind_speed"]
    weather_desc = json_data["current"]["weather"][0]["description"]
    humidity = json_data["current"]["humidity"]

    print(str(g.latlng[0]) + ' latitude and ' + str(g.latlng[1]) + ' longitude')
    speak(str(g.latlng[0]) + 'latitude and ' + str(g.latlng[1]) + ' longitude')

    # print('Current location is ' + json_data['name'] + " " + json_data['sys']['country'] + 'dia')
    # speak('Current location is ' + json_data['name'] + " " + json_data['sys']['country'] + 'dia')

    print('weather type ' + weather_desc)
    speak('weather type ' + weather_desc)

    print('Wind speed is ' + str(wind_speed) + ' metre per second')
    speak('Wind speed is ' + str(wind_speed) + ' metre per second')

    print('Temperature is ' + str(temperature) + ' degree celcius')
    speak('Temperature is ' + str(temperature) + ' degree celcius')

    print('Humidity is ' + str(humidity) + ' percent')
    speak('Humidity is ' + str(humidity) + ' percent')


if __name__ == '__main__':
    weather()
