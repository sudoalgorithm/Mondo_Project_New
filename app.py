from flask import Flask, render_template, url_for
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ca')
def ca():
	return render_template('ca.html')

@app.route('/customs')
def customs():
	return render_template('customs.html')

@app.route('/fa')
def fa():
	return render_template('fa.html')

@app.route('/ihc')
def ihc():
	return render_template('ihc.html')

@app.route('/mofa')
def mofa():
	return render_template('mofa.html')

@app.route('/moh')
def moh():
	return render_template('moh.html')

@app.route('/who')
def who():
	return render_template('who.html')

@app.route('/action')
def packinglist():
	json = {
		"$class": "org.acme.mondo.PackingList",
		"packingListId": "123",
		"to": "string",
		"from": "string",
		"shipDate": "string",
		"FOBShippingPoint": "string",
		"accountNumber": 0,
		"orderNumber": 0,
		"department": "string",
		"termsNoAnticipation": "string",
		"quantityOrdered": 0,
		"quantityShipped": 0,
		"description": "string",
		"unitWeight": 0,
		"totalWeight": 0,
		"totalCubicFeet": 0,
		"comments": "string",
		"date": "string"
	}
	response = requests.post('http://localhost:3000/api/PackingList', json)
	print(response)

if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP','0.0.0.0')
	port = int(os.environ.get('PORT','8080'))
	app.run(host=host, port=port)


