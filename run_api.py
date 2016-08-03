from flask import Flask, render_template, redirect, url_for, request
from API import *
from flask import jsonify


app = Flask(__name__)


@app.route('/<hotel_id>')
def test2(hotel_id):
	offer_data = API_run(hotel_id)
	
	try:
		
		return jsonify(offer_data)
		
	except:
		print ('API failed')
		return ('API failed')

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug='true')





