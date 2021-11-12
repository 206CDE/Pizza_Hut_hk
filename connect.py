import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "Localhost via UNIX socket",
  user = "xs1cdlbk6b7o",
  password = "4QHWqXT{2XHAEU#",  
  database = "information_schema"
)
CUR = DB.cursor() 
