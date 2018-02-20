from flask import Flask, render_template, url_for, request, jsonify, redirect
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

@app.route('/packingList', methods=['GET','POST'])
def packinglist():
	packingListId = request.form['packingListID']
	sender = request.form['from']
	receiver = request.form['to']
	shipdate = request.form['shipdate']
	fob = request.form['fob']
	accountNumber = request.form['accountnumber']
	orderNumber = request.form['ordernumber']
	department = request.form['department']
	terms = request.form['terms']
	quantityOrdered = request.form['qtyorder']
	quantityShipped = request.form['qtyshipped']
	description = request.form['description']
	unitweight = request.form['unitweight']
	totalWeight = request.form['totalweight']
	totalcubicft = request.form['totalcubicft']
	comment = request.form['comment']
	todaydate = request.form['todaydate']
	jsonPA = {
		"$class": "org.acme.mondo.PackingList",
		"packingListId": packingListId,
		"to": sender,
		"from": receiver,
		"shipDate": shipdate,
		"FOBShippingPoint": fob,
		"accountNumber": accountNumber,
		"orderNumber": orderNumber,
		"department": department,
		"termsNoAnticipation": terms,
		"quantityOrdered": quantityOrdered,
		"quantityShipped": quantityShipped,
		"description": description,
		"unitWeight": unitweight,
		"totalWeight": totalWeight,
		"totalCubicFeet": totalcubicft,
		"comments": comment,
		"date": todaydate
	}
	url = 'http://localhost:3000/api/PackingList'
	responsePA = requests.post(url, data=jsonPA)
	print(responsePA.text)
	return redirect(url_for('fa'))


@app.route('/invoice', methods=['GET','POST'])
def invoice():
	invoiceID = request.form['invoiceID']
	sender = request.form['fromif']
	receiver = request.form['toif']
	shipdate = request.form['shipdateif']
	fob = request.form['fobif']
	accountNumber = request.form['accountnumberif']
	orderNumber = request.form['ordernumberif']
	department = request.form['departmentif']
	terms = request.form['termsif']
	quantityOrdered = request.form['qtyorderif']
	quantityShipped = request.form['qtyshippedif']
	description = request.form['descriptionif']
	unitweight = request.form['unitweightif']
	totalWeight = request.form['totalweightif']
	totalcubicft = request.form['totalcubicftif']
	comment = request.form['commentif']
	todaydate = request.form['todaydateif']
	unitPriceEverything = request.form['unitpriceeverythingif']
	jsonInvoice = {
		"$class": "org.acme.mondo.Invoice",
		"invoiceId": invoiceID,
		"to": sender,
		"form": receiver,
		"shipDate": shipdate,
		"FOBShippingPoint": fob,
		"accountNumber": accountNumber,
		"orderNumber": orderNumber,
		"department": department,
		"termsNoAnticipation": terms,
		"quantityOrdered": quantityOrdered,
		"quantityShipped": quantityShipped,
		"description": description,
		"unitWeight": unitweight,
		"totalWeight": totalWeight,
		"totalCubicFeet": totalcubicft,
		"comments": comment,
		"date": todaydate,
		"unitPriceForEverythingOrdered": unitPriceEverything
	}
	url = 'http://localhost:3000/api/Invoice'
	response = requests.post(url, json=jsonInvoice)
	response.json
	return redirect(url_for('fa'))

@app.route('/medicineDetails', methods=['POST'])
def medicineDetails(): 
	jsonMedicineDetails = {
		"$class": "org.acme.mondo.MedicineDetails",
		"medicineDetailsId": "string",
		"doseStrength": 0,
		"dosageForm": "string",
		"quantity": 0
	}
	response = requests.post('http://localhost:3000/api/MedicineDetails', params=jsonMedicineDetails)
	return response.text

@app.route('/InitiateImportProcess', methods=['POST'])
def initiateImportProcess():
	jsonImportProcess = {
		 "$class": "org.acme.mondo.InitiateImportProcess",
    	"packingList": "resource:org.acme.mondo.PackingList#123",
    	"invoice": "resource:org.acme.mondo.Invoice#123",
    	"medicineDetails": "resource:org.acme.mondo.MedicineDetails#123",
    	"ISODocument": "resource:org.acme.mondo.ISODocument#123"
	}
	response = requests.post('http://localhost:3000/api/InitiateImportProcess', params=jsonImportProcess)
	return response.text


if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP','0.0.0.0')
	port = int(os.environ.get('PORT','8080'))
	app.run(host=host, port=port)


