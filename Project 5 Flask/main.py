# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Valeriy/Desktop/projects/Project 5 Flask/pb_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    isactive=db.Column(db.Boolean,default=True)
    text=db.Column(db.Text,nullable=False)
    
    def __repr__(self):
        return self.title
@app.route('/')
def index():
    items=Item.query.order_by(Item.price).all()
    return render_template('index.html',data=items)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buy/<int:id>')
def item_buy(id):
    item=Item.query.get(id)
    api = Api(merchant_id=1396424,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
         "currency": "USD",
         "amount": item.price*100
           }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method=='POST':
      title = request.form['title']
      price = request.form['price']
      text = request.form['text']
      item=Item(title=title,price=price,text=text)
      
           
      try:
       db.session.add(item)
       db.session.commit()
       return redirect('/')
      
      except:
          return "Error in data"
    else:
      return render_template('create.html')

if __name__=="__main__":
 app.run(debug=True)