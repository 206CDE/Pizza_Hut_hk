import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "184.168.114.22",
  user = "cpses_xsjc4cya10",
)
CUR = DB.cursor() 


