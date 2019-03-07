#imports
from lxml import html
from json import dump, loads
from requests import post,get
import requests
import json
from re import sub
from flask import Flask, request, render_template, url_for
import os

# login
def login(usr, passw):
    username = usr
    password = passw

    payload = {"username":str(username), "password":str(password)}

    login_post = requests.post("http://localhost:3000/api/session", data=json.dumps(payload))
    print(login_post.headers['content-type'])

    return login_post.json()


