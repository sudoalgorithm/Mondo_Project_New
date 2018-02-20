from flask import Flask, render_template, url_for, request, redirect, json
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ca')
def ca():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('ca.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('ca.html', json_val=json_val, json_val1=json_val1)
	
	

@app.route('/customs')
def customs():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('customs.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('customs.html', json_val=json_val, json_val1=json_val1)
	

@app.route('/fa')
def fa():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('fa.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('fa.html', json_val=json_val, json_val1=json_val1)
	

@app.route('/ihc')
def ihc():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('ich.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('ihc.html', json_val=json_val, json_val1=json_val1)
		

@app.route('/mofa')
def mofa():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('mofa.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('mofa.html', json_val=json_val, json_val1=json_val1)
	

@app.route('/moh')
def moh():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('moh.html')
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('moh.html', json_val=json_val, json_val1=json_val1)
		

@app.route('/who')
def who():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is None:
		return render_template('who.html')
	if responsefa.json() is not None: 
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('who.html', json_val=json_val, json_val1=json_val1)
		

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
	responsePA.text
	return redirect(url_for('fa'))


@app.route('/invoice', methods=['GET','POST'])
def invoice():
	invoiceID = request.form['invoiceID']
	sender = request.form['toif']
	receiver = request.form['fromif']
	shipdate = request.form['shipdateif']
	fob = request.form['fobif']
	accountNumber = request.form['accountnumberif']
	orderNumber = request.form['ordernumberif']
	department = request.form['departmentif']
	terms = request.form['termsif']
	quantityOrdered = request.form['qtyorderif']
	quantityShipped = request.form['qtyshippedif']
	description = request.form['descif']
	unitweight = request.form['unitweightif']
	totalWeight = request.form['totalweightif']
	totalcubicft = request.form['totalcubicftif']
	comment = request.form['commentsif']
	todaydate = request.form['todaydateif']
	unitPriceEverything = request.form['unitpriceeverythingif']
	jsonInvoice = {
		"$class": "org.acme.mondo.Invoice",
		"invoiceId": invoiceID,
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
		"date": todaydate,
		"unitPriceForEverythingOrdered": unitPriceEverything
	}
	url = 'http://localhost:3000/api/Invoice'
	response = requests.post(url, json=jsonInvoice)
	response.text
	return redirect(url_for('fa'))

@app.route('/medicineDetails', methods=['GET','POST'])
def medicineDetails():
	medicineDetailsID = request.form['medicineDetailsID']
	doseStrength = request.form['dosestrength']
	dosageForm = request.form['dosageform']
	quantity = request.form['qtymdf']  
	jsonMedicineDetails = {
		"$class": "org.acme.mondo.MedicineDetails",
		"medicineDetailsId": medicineDetailsID,
		"doseStrength": doseStrength,
		"dosageForm": dosageForm,
		"quantity": quantity
	}
	url = 'http://localhost:3000/api/MedicineDetails'
	response = requests.post(url, json=jsonMedicineDetails)
	response.text
	return redirect(url_for('fa'))

@app.route('/iosDocument', methods=['POST','GET'])
def iosDocument():
	iosDocumentID = request.form['isodocumentID']
	filepath = request.form['filepath']
	jsonISODoc = {
		"$class": "org.acme.mondo.ISODocument",
 		"ISODocumentId": iosDocumentID,
 		"Hash": filepath
	}
	jsonTransaction = {
		"$class": "org.acme.mondo.InitiateImportProcess",
		"packingList": "resource:org.acme.mondo.PackingList#123",
		"invoice": "resource:org.acme.mondo.Invoice#123",
		"medicineDetails": "resource:org.acme.mondo.MedicineDetails#123",
		"ISODocument": "resource:org.acme.mondo.ISODocument#123"
	}
	url1 = 'http://localhost:3000/api/ISODocument'
	url2 = 'http://localhost:3000/api/InitiateImportProcess'
	response = requests.post(url1, json=jsonISODoc)
	response.text
	response1 = requests.post(url2, json=jsonTransaction)
	response1.text
	return redirect(url_for('fa'))

@app.route('/customsTrans', methods=['POST'])
def customsTrans(): 
	jsonTranx = {
 		"$class": "org.acme.mondo.IssueBillOfEntry"
	}
	url = 'http://localhost:3000/api/IssueBillOfEntry'
	response = requests.post(url, json=jsonTranx)
	response.text
	return redirect(url_for('customs'))

@app.route('/mofaLetter', methods=['POST','GET'])
def mofaLetter():
	filepath = request.form['filepath']
	jsonMofaLetter = {
		"$class": "org.acme.mondo.MoFALetter",
		"letterHash": filepath
	}
	url = 'http://localhost:3000/api/MoFALetter'
	respone = requests.post(url, json=jsonMofaLetter)
	respone.text
	return redirect(url_for('ihc'))


if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP','0.0.0.0')
	port = int(os.environ.get('PORT','8080'))
	app.run(host=host, port=port)


   