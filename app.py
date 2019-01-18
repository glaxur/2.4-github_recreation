"""use this for main page info // response = requests.get("https://api.github.com/users/glaxur")
use this for repository page //response = requests.get("https://api.github.com/users/glaxur/repos")"""


import csv

from flask import Flask
from flask import request
from flask import render_template

import requests

app = Flask(__name__)   #load all the packages


@app.route("/")  #this says if the search bar shows / insert the info from this function
def index():      #defining function that will get my info for page from github
    response = requests.get("https://api.github.com/users/glaxur")
    response2 = requests.get("https://api.github.com/users/glaxur/repos")
    data = response.json()
    data2 = response2.json()

    # print(data)  # list of dict
    # print(data[1])

    info_repo = {
        'repos': data2, 'general': data
    }

    return render_template('index.html', **info_repo)


######## how to make tab sent tp followers  ############

#############################################################################

@app.route('/followers/', methods=["GET", "POST"]) #if query string has repos included it will GET (using get mehtod)info
                                                # from api and will use the method POST to pass in info that user types
                                                # in search bar
def following_people():
    response = requests.get("https://api.github.com/users/glaxur/followers")
    data_followers = response.json()

    info_followers = {
        "followers" : data_followers}

    return render_template('followers.html', **info_followers)


