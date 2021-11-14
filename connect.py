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

@app.route("/send_order", methods = ['POST'])
def send_order():
  CUR.execute("""SELECT COUNT(Order_ID) FROM `Delivery_Information`""")
  order_id = CUR.fetchone()
  order_id = str(order_id).replace('(', '')
  order_id = str(order_id).replace(')', '')
  order_id = str(order_id).replace(',', '')
  order_id = str(int(order_id) + 1)
  DB.commit()

  order_product  = str(request.form['product_list'])
  title          = str(request.form['title'])
  nickname       = str(request.form['nickname'])
  phone_number   = str(request.form['phone_number'])
  address_name   = str(request.form['address_name'])
  floor          = str(request.form['floor'])
  flat           = str(request.form['flat'])
  block_building = str(request.form['block_building'])
  estate_street  = str(request.form['estate_street'])
  district       = str(request.form['district'])
  region         = str(request.form['region'])
  pay_method     = str(request.form['pay_method'])
  
  try:
    credit_card  = str(request.form['credit_card'])
  except:
    credit_card  = ""

  product_price  = str(request.form['product_price_input'])
  shipping_price = str(request.form['shipping_price_input'])
  total_price    = str(request.form['total_price_input'])
  
  try:
    #Send order to database
    CUR.execute("""INSERT INTO `Delivery_Information`
               (Order_ID, Order_Product, Title, Name, Phone_No, Address_Name, Floor, Flat ,`Block/Building`,
                `Estate/Street`, District, Region, Payment_Method, Credit_C_Type,
                Product_Price, Shipping_Price, Discount, Total_Price)
                VALUES ('""" + order_id + """','""" + order_product + """','""" 
                + title + """','""" + nickname + """','"""
                + phone_number + """','""" + address_name + """','"""
                + floor + """','""" + flat + """','"""
                + block_building + """','""" + estate_street + """','"""
                + district + """','""" + region + """','"""
                + pay_method + """','""" + credit_card + """','"""
                + product_price + """','""" + shipping_price + """','"""
                + total_price + """')""")
    DB.commit()

    #Change Product_Stock and Total_Sale data base on Product_Name in database
    for a in range(len(product_list)):
      product_name = product_list[a]
      
      CUR.execute("""SELECT Product_Stock FROM `product` WHERE Product_Name = '""" + product_name + """'""")
      old_product_quantity = CUR.fetchone()
      old_product_quantity = str(old_product_quantity).replace('(', '')
      old_product_quantity = str(old_product_quantity).replace(')', '')
      old_product_quantity = str(old_product_quantity).replace(',', '')
      new_product_quantity = str(int(old_product_quantity) - int(quantity_list[a]))
      DB.commit()
           
      CUR.execute("""UPDATE product SET Product_Stock = '""" + new_product_quantity + """' WHERE Product_Name = '""" + product_name + """'""")
      DB.commit()

      CUR.execute("""SELECT Product_Total_Sale FROM `product` WHERE Product_Name = '""" + product_name + """'""")
      old_total_sale = CUR.fetchone()
      old_total_sale = str(old_total_sale).replace('(', '')
      old_total_sale = str(old_total_sale).replace(')', '')
      old_total_sale = str(old_total_sale).replace(',', '')
      new_total_sale = str(int(old_total_sale) + int(quantity_list[a]))
      DB.commit()
      
      CUR.execute("""UPDATE product SET Product_Total_Sale = '""" + new_total_sale + """' WHERE Product_Name = '""" + product_name + """'""")
      DB.commit()
      
    #Once data send to database, go back to the main html page
    return """<html><body>
                <script>
                  //Remove all product in shopping cart once the order has sent
                  alert("Your order has been successfully sent!");
                  window.history.go(-3);
                </script>
              </body></html>"""
  
  except:
    return """<html><body>
                <script>
                  alert('Sorry, we have some problem sending your order!');
                  window.history.go(-3);
                </script>
              </body></html>"""

if __name__=='__main__':
  app.run(host="localhost", port=8000, debug = True)

DB.close()
