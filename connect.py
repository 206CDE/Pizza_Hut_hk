import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  user = "xs1cdlbk6b7o",
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  password = "4QHWqXT{2XHAEU#",
  database = "information_schema"
)
CUR = DB.cursor() 

app = Flask(__name__)

@app.route("/send_order", methods = ['GET', 'POST'])
def send_order():
 
    #Once data send to database, go back to the main html page
    return """<html><body>
                <script>
                  //Remove all product in shopping cart once the order has sent
                  alert("Your order has been successfully sent!");
                  window.history.go(-3);
                </script>
              </body></html>"""

if __name__=='__main__':
  app.run(host="221.124.209.137", port=8000, debug = True)

DB.close()
