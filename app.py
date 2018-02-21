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
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('ca.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('ca.html')
	

@app.route('/customs')
def customs():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('customs.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('customs.html')	

@app.route('/fa')
def fa():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('fa.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('fa.html')

@app.route('/ihc')
def ihc():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('ihc.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('ich.html')	

@app.route('/mofa')
def mofa():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('mofa.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('mofa.html')

@app.route('/moh')
def moh():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None:
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('moh.html', json_val=json_val, json_val1=json_val1)
	
	return render_template('moh.html')	

@app.route('/who')
def who():
	url = 'http://localhost:3000/api/InitiateImportProcess'
	responsefa = requests.get(url)
	if responsefa.json() is not None: 
		json_val = responsefa.json()[0]['transactionId']
		json_val1 = responsefa.json()[0]['timestamp']
		return render_template('who.html', json_val=json_val, json_val1=json_val1)
	
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

@app.route('/whoLetter', methods=['POST','GET'])
def whoLetter():
	filepath = request.form['filepathwho']
	jsonWhoLetter = {
		"$class": "org.acme.mondo.WHOLetter",
		"letterHash": filepath
	}
	url = 'http://localhost:3000/api/WHOLetter'
	respone = requests.post(url, json=jsonWhoLetter)
	respone.text
	return redirect(url_for('ihc'))

@app.route('/airwayBillLanding', methods=['POST','GET'])
def airwayBillLanding():
	fromID = request.form['fromID']
	datelading = request.form['datelading']
	senderfirst = request.form['senderfirst']
	senderlast = request.form['senderlast']
	phonenum = request.form['phonenum']
	deladdress = request.form['deladdress']
	zipcode = request.form['zipcode']
	toID = request.form['toID']
	recipientfirst = request.form['recipientfirst']
	recipientlast = request.form['recipientlast']
	fax = request.form['fax']
	receiverDeliveryAddress = request.form['receiverDeliveryAddress']
	zipcode = request.form['zipcode']
	taxnumber = request.form['taxnumber']
	shipmentInfo = request.form['shipmentInfo']
	desc = request.form['desc']
	countryofmanufacture = request.form['countryofmanufacture']
	totalValOfCustoms = request.form['totalValOfCustoms']
	acceptanceDate = request.form['acceptanceDate']
	acceptanceTime = request.form['acceptanceTime']
	deliveryDate = request.form['deliveryDate']
	acceptancezip = request.form['acceptancezip']
	empinitials = request.form['empinitials']
	dimension = request.form['dimension']
	weightofshipment = request.form['weightofshipment']
	postage = request.form['postage']
	insurancefee = request.form['insurancefee']
	postageandfees = request.form['postageandfees']
	packagingtype = request.form['packagingtype']
	
	jsonValue = {
		"$class": "org.acme.mondo.AirwayBill",
		"airwayBillId": fromID,
		"date": datelading,
		"senderFirstName": senderfirst,
		"senderLastName": senderlast,
		"senderPhoneNumber": phonenum,
		"senderDeliveryAddress": deladdress,
		"senderZipCode": zipcode,
		"recipientFirstName": toID,
		"recipientLastName": recipientfirst,
		"receiverPhoneNumber": recipientlast,
		"fax": fax,
		"receiverDeliveryAddress": receiverDeliveryAddress,
		"receiverZipCode": zipcode,
		"taxIDNumber": taxnumber,
		"shipmentInformation": shipmentInfo,
		"description": desc,
		"countryOfManufacture": countryofmanufacture,
		"totalValueofCustoms": totalValOfCustoms,
		"acceptanceDateIn": acceptanceDate,
		"acceptanceTimeIn": acceptanceTime,
		"scheduledDeliveryDate": deliveryDate,
		"acceptanceZipAnd4Code": acceptancezip,
		"employeeInitials": empinitials,
		"dimensionInInches": dimension,
		"weightOfShipment": weightofshipment,
		"postageInUSDollars": postage,
		"insuranceFee": insurancefee,
		"totalPostageAndFees": postageandfees,
		"packagingType": packagingtype,
		"isApproved": 'false'	
	}
	jsonICL = {
		"$class": "org.acme.mondo.IssueCoverLetter",
		"MoFALetter": "resource:org.acme.mondo.MoFALetter#123",
		"WHOLetter": "resource:org.acme.mondo.WHOLetter#123",
		"airwayBill": "resource:org.acme.mondo.AirwayBill#123"
	}
	url = 'http://localhost:3000/api/AirwayBill'
	url1 = 'http://localhost:3000/api/IssueCoverLetter'
	response = requests.post(url, json=jsonValue)
	response.text
	response1 = requests.post(url1, json=jsonICL)
	response1.text
	return redirect(url_for('ihc'))

@app.route('/perImportPermit', methods=['POST','GET'])
def perImportPermit():
	moduleID = request.form['moduleID']
	typeID = request.form['type']
	importmodule = request.form['importmodule']
	MOHNumber = request.form['MOHNumber']
	importer = request.form['importer']
	country = request.form['country']
	city = request.form['city']
	address = request.form['address']
	pobox = request.form['pobox']
	phone = request.form['phone']
	fax = request.form['Fax']
	email = request.form['email']
	website = request.form['website']
	productclass = request.form['productclass']
	product = request.form['product']
	productform = request.form['productform']
	packsize = request.form['packsize']
	shelflife = request.form['shelflife']
	batchnumber = request.form['batchnumber']
	cifuprice = request.form['cifuprice']
	invoiceuprice = request.form['invoiceuprice']
	quantity = request.form['quantity']
	batchmanufdate = request.form['batchmanufdate']
	batchexpdate = request.form['batchexpdate']
	manufacturer = request.form['manufacturer']
	countryoforigin = request.form['countryoforigin']
	documentName = request.form['documentName']
	documentType = request.form['documentType']
	filepathvalidate = request.form['filepathvalidate']
	jsonPIP = {
			"$class": "org.acme.mondo.PreImportPermit",
			"preImportPermitId": moduleID,
			"type": typeID,
			"importModule": importmodule,
			"MOHLicenseNumber": MOHNumber, 
			"importer": importer,
			"country": country,
			"city": city,
			"address": address,
			"POBox": pobox,
			"phone": phone,
			"fax": fax,
			"email": email,
			"website": website,
			"registerProduct": 'true',
			"unregisterProduct": 'true',
			"productClass": productclass,
			"product": product,
			"productForm": productform,
			"packSize": packsize,
			"shelfLife": shelflife,
			"batchNumber": batchnumber,
			"CIFUnitPrice": cifuprice,
			"invoiceUnitPrice": invoiceuprice,
			"quantity": quantity,
			"batchManufacturingDate": batchmanufdate,
			"batchExpireDate": batchexpdate,
			"manufacturer": manufacturer,
			"countryOfOrigin": countryoforigin,
			"documentName": documentName,
			"documentType": documentType,
			"documentHash": filepathvalidate,
			"isApproved": 'true'
	}
	jsonPIPTranx = {
			"$class": "org.acme.mondo.IssuePermitRequest",
			"preImportPermit": "resource:org.acme.mondo.PreImportPermit#123"
	}
	url = 'http://localhost:3000/api/PreImportPermit'
	url1 = 'http://localhost:3000/api/IssuePermitRequest'
	responsePIP = requests.post(url, json=jsonPIP)
	responsePIP.text
	responsePIPTranx = requests.post(url1, json=jsonPIPTranx)
	responsePIPTranx.text
	return redirect(url_for('who'))



if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP','0.0.0.0')
	port = int(os.environ.get('PORT','8080'))
	app.run(host=host, port=port)


   