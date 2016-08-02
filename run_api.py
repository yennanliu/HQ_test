from flask import Flask, render_template, redirect, url_for, request
from API import *
from flask import jsonify


app = Flask(__name__)




@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username='user.username',
                   email='g.user.email',
                   id='g.user.id')

@app.route('/')
def test1():
	print (API_test())
	return render_template('test1.html') 


@app.route('/<offerId>')
def test2(offerId):
	offer_data = API_run(offerId)
	print (offerId)
	print ('==============')
	try:
		print (API_run(offerId))
		return jsonify(checkinDate=str(offer_data.checkinDate),
                   checkoutDate=str(offer_data.checkoutDate),
                   currencyCode=str(offer_data.currencyCode))
		#return jsonify(a=1,b=2)
		#return flask.jsonify({'hello': 'world'})
		#return Response(API_run(offerId))
		#return render_template('test1.html') 	
	except:
		print ('API failed')

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug='true')