import csv

from flask import Flask
from flask import request
from flask import render_template

import requests

app = Flask(__name__)   #load all the packages


@app.route("/") #this says if the search bar shows /with nothing following insert the info form api
def index():     #defining function that will get my info for profile page from github
   response = requests.get("https://api.github.com/users/glaxur") #this is going to load my profile page
   data = response.json()
   basic = data["results"]
   print(basic)


   # planet_html = []
   #
   # for planet in planets:
   #     planet_html.append('<li>{} :: {}</li>'.format(planet['name'], planet['climate']))
   #
   # planet_html = ''.join(planet_html)
   #


   return render_template('index.html', planet_list=planets)




@app.route('/repos/', methods=["GET", "POST"]) #if query string has repos included it will GET (using get mehtod)info
                                               # from api and will use the method POST to pass in info that user types
                                               # in search bar
def repository():
   response = requests.get("https://api.github.com/users/glaxur/repos")
   data = response.json
   repos = data["results"]
   print(repos)





   return render_template('index.html', planet_list=planets)


# @app.route('/repos/', methods=['GET', 'POST'])
# def book_now():
#     # Book now is configured to accept POST requests, so we can access the form data as a dictionary:
#     print(request.form['1-tickets'])
#     return 'Booking your trip!'