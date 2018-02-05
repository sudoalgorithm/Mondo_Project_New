$(document).ready(function(){
    $('.collapsible').collapsible();
  });
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

  function toastMe(value)
  {
    if(value=='yes')
    {
  var toastHTML = 'Request Approved';
    }
    else
    {
      var toastHTML = 'Request Rejected';
    }
    M.toast({html: toastHTML, classes: 'rounded',displayLength: 3000});
    setTimeout(function (){
      $('#modal1').modal('close');
    }, 3000);
  }

  function approve(command, value, index)
  {
    if(value=='yes')
    {
      var toastHTML = command+' Approved';
    }
    else
    {
      var toastHTML = command+ ' Rejected';
    }
    M.toast({html: toastHTML, classes: 'rounded',displayLength: 3000});
    $('.collapsible').collapsible('close', index);
  }