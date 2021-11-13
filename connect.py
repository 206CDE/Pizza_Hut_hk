import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  user = "Pizza_Hut_Manager",
  password = "4QHWqXT{2XHAEU#",  
  database = "Delivery_Information"
)
CUR = DB.cursor() 


