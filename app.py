from flask import Flask,jsonify
import requests
import os
from bs4 import BeautifulSoup
    

from flask import Flask, request, \
render_template, redirect, url_for, \
session, send_file
from flask import (Flask,request,redirect,session)


app = Flask(__name__)

@app.route('/',  methods=["GET", "POST"])
def scrape_url():
    try:
        req = request.form
        compurl=req.get('url')
        reqs = requests.get(compurl)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        lst2 = []
        for link in soup.find_all('a'):
            j = link.get('href')
            lst2.append(j)
        print(lst2)
        k = " ".join(str(x) for x in lst2)
        return render_template("home.html", value=k)
    except Exception as e:
        reqs = requests.get("https://google.com")
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        lst2 = []
        for link in soup.find_all('a'):
            j = link.get('href')
            lst2.append(j)
        print(lst2)
        k = " ".join(str(x) for x in lst2)
        
        return render_template("home.html", value=k)



if __name__ == "__main__":
    app.run(debug=True)