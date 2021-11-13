import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  user = "cpses_xsjc4cya10",
)
CUR = DB.cursor() 


