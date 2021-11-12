import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "127.0.0.1",
  user = "",
  password = "",  
  database = ""
)
CUR = DB.cursor() 
