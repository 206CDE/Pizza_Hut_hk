import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  user = "1llzix",
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  password = "ea6e56e89f75cacd0eb809342c74765f",
)
CUR = DB.cursor() 
