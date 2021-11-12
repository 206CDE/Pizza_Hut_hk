import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  user = "cpses_xsklfh54mh",
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  password = "",
  database = "information_schema"
)
CUR = DB.cursor() 
