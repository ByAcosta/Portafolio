var currentTab = 0; 
showTab(currentTab); 

function showTab(n) {
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Pagar";
  } else {
    document.getElementById("nextBtn").innerHTML = "Siguiente";
  }
  fixStepIndicator(n)
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");
  //if (n == 1 && !validateForm()) return false;
  x[currentTab].style.display = "none";
  currentTab = currentTab + n;
  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }
  showTab(currentTab);
}

// function validateForm() {
//   var x, y, i, valid = true;
//   x = document.getElementsByClassName("tab");
//   //y = x[currentTab].getElementsByTagName("input");
//   y = x[currentTab].document.querySelectorAll('input[type=date]')
//   for (i = 0; i < y.length; i++) {
//     if (y[i].value == "") {
//       y[i].className += " invalid";
//       valid = false;
//     }
//   }
//   if (valid) {
//     document.getElementsByClassName("step")[currentTab].className += " finish";
//   }
//   return valid; 
// }

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  x[n].className += " active";
}

function cancelar(){
  document.getElementById('estado_in').value = "Cancelado"
}


// $("#div_tour").hide();
// $("#switch_serv").click(function() {
//     if($(this).is(":checked")) {
//         $("#div_tour").show(300);
//     } else {
//         $("#div_tour").hide(200);
//     }
// });