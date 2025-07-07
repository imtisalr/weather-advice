# This project gives you a suggested course of action based on the weather in your city

from flask import Flask
from flask import request
import json
import requests
import math
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get("city")
    if city:
        suggestion = main(city)
    else:
        suggestion = "waiting for input"
    return ( """<h1>Today's Weather Suggestion</h1>
             <form action="" method="get">
                <input type="text" name="city">
                <input type="submit" value="Suggest!">
              </form>"""
              + "Suggestion: <br/>"
              + suggestion
    )

@app.route("/")
def main(city):
    load_dotenv()

    # ask user for location
    # city_name = input("Enter your city's name: ")
    city_name = city

    # base url
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},&appid={os.getenv('api_key')}&units=imperial"

    # send a get request
    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:
        # weather desctiption
        description = data["weather"][0]["description"]
        # temperature
        temp = data["main"]["temp"]
        # wind speeds
        wind = data["wind"]["speed"]
        
        # round to the nearest int
        temp = round(temp)
        
        # display data
        # print(f"The weather in {city_name} is currently {description} with a temperature of {temp}°F and wind speeds of {wind}mph.")

    else:
        print("error... check city name")
     
    # pass the keyword and the temperature into advice function
    a = advice(description, temp)
    # print the answer returned from advice
    #print(a)
    return a
    
def advice(descr, tmp):
    t = str(tmp)
    
    # create dictionary
    suggestions = {
        "clear" : "Clear skies today! ",
        "cloud" : "It's a bit cloudy today, I suggest a light jacket! ",
        "rain" : "Looks like it's going to rain, make sure to bring an umbrella! ",
        "thunderstorm" : "Watch out for thunderstorms — stay inside or wear a raincoat! ",
        "drizzle" : "It's going to be drizzling, bring a jacket — and an umbrella just in case! ",
        "snow" : "Dress warmly! It's going to snow today. ",
        "mist" : "It's misty today, drive carefully. ",
        "tornado" : "There's going to be a tornado, stay indoors and seek shelter. "
    }
    
    answer = None

    # loop through suggestions dictionary, if the key word is found based on today's weather, set answer to the matching value
    for keyword in suggestions:
        if keyword in descr:
            # key = keyword
            answer = suggestions[keyword]
            break
    
    # answer += "\n"  # doesn't work?
    answer += "<br/>"
        
    if tmp <= 10:
        answer += "The temperature is " + t + "°F. Make sure to bundle up with some gloves and a jacket."
    elif tmp <= 20:
        answer += "The temperature is " + t + "°F. Make sure to wear a jacket and warm clothes."
    elif tmp <= 30:
        answer += "The temperature is " + t + "°F. Make sure to wear warm clothes and layer up."
    elif tmp <= 50:
        answer += "The temperature is " + t + "°F. Wear a coat and some warm clothes."
    else:
        answer += "The temperature is " + t + "°F. Enjoy your day!"
        
    return answer


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    # main()