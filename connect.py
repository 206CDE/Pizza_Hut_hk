import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  user = "206cde_Pizza_Hut",
  password = "%}Me?CAQX.I!",  
  database = "Delivery_Information"
)
CUR = DB.cursor() 


