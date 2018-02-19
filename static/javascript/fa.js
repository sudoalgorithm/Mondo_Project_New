$(document).ready(function(){
    $('.datepicker').datepicker({
      container: 'body'
    });
  });
  $(document).ready(function(){
    $('select').select();
  });
  $(document).ready(function(){
    $('.modal').modal();
  });



  function ifsubmit(){
    var invoiceID = document.getElementById("invoiceID").value;
    var sender = document.getElementById("toif").value;
    var receiver = document.getElementById("fromif").value;
    var shipDate = document.getElementById("shipdateif").value;
    var shippingPoint = document.getElementById("fobif").value;
    var accountNumber = document.getElementById("accountnumberif").value;
    var orderNumber = document.getElementById("ordernumberif").value;
    var department = document.getElementById("departmentif").value;
    var terms = document.getElementById("termsif").value;
    var quantityOrdered = document.getElementById("qtyorderif").value;
    var quantityShipped = document.getElementById("qtyshippedif").value;
    var description = document.getElementById("descif").value;
    var unitWeight = document.getElementById("unitweightif").value;
    var totalWeight = document.getElementById("totalweightif").value;
    var totalCubicFT = document.getElementById("totalcubicftif").value;
    var comments = document.getElementById("commentsif").value;
    var date = document.getElementById("todaydateif").value;
    var unitPriceForEverythingOrdered = document.getElementById("unitpriceeverythingif").value
    var dataif = {
      "$class": "org.acme.mondo.Invoice",
      "invoiceId": invoiceID,
      "to": sender,
      "from": receiver,
      "shipDate": shipDate,
      "FOBShippingPoint": shippingPoint,
      "accountNumber": accountNumber,
      "orderNumber": orderNumber,
      "department": department,
      "termsNoAnticipation": terms,
      "quantityOrdered": quantityOrdered,
      "quantityShipped": quantityShipped,
      "description": description,
      "unitWeight": unitWeight,
      "totalWeight": totalWeight,
      "totalCubicFeet": totalCubicFT,
      "comments": comments,
      "date": date,
      "unitPriceForEverythingOrdered": unitPriceForEverythingOrdered
    }

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST","http://localhost:3000/api/Invoice", true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send(JSON.stringify(dataif));
  }

  function mdsubmit(){
    var medicineDetailsID = document.getElementById("medicineDetailsID").value;
    var doseStrength = document.getElementById("dosestrength").value;
    var dosageForm = document.getElementById("dosageform").value;
    var qty = document.getElementById("qty").value;
    var datamd = {
      "$class": "org.acme.mondo.MedicineDetails",
      "medicineDetailsId": mdsubmit,
      "doseStrength": doseStrength,
      "dosageForm": dosageForm,
      "quantity": qty
    }

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://localhost:3000/api/MedicineDetails", true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send(JSON.stringify(datamd));
  }