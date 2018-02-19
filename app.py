from flask import Flask, render_template, url_for, request, jsonify
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

def packinglist():
	packingListId = request.form['packingListID']
	sender = request.form['to']
	receiver = request.form['form']
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
		"date": todaydate
	}
	if request.method == 'POST':
		response = requests.post('http://localhost:3000/api/PackingList', params=jsonPA)
		return response.get_json()


@app.route('/invoice', methods=['POST'])
def invoice():
	jsonInvoice = {
		"$class": "org.acme.mondo.Invoice",
		"invoiceId": "123",
		"to": "string",
		"form": "string",
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
		"date": "string",
		"unitPriceForEverythingOrdered": 0
	}
	response = requests.post('http://localhost:3000/api/Invoice', params=jsonInvoice)
	return response.text

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


