import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  user = "xs1cdlbk6b7o",
  password = "4QHWqXT{2XHAEU#",  
  database = "information_schema"
)
CUR = DB.cursor() 
