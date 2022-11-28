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
    document.getElementById("nextBtn").style.display = "none";
  } else {
    document.getElementById("nextBtn").style.display = "inline";
    document.getElementById("nextBtn").innerHTML = "Siguiente";
  }
  fixStepIndicator(n)
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");
  x[currentTab].style.display = "none";
  currentTab = currentTab + n;
  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }
  showTab(currentTab);
}

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  x[n].className += " active";
}

function fechas(){
  fecha1 = document.getElementById('check_in').value
  fecha2 = document.getElementById('check_out').value
  let mili = 24 * 60 * 60 * 1000;
  f1 = Date.parse(fecha1)
  f2 = Date.parse(fecha2)
  let miliT = Math.abs(f1 - f2);
  let cantdias = Math.round(miliT/mili);
  document.getElementById('dias').value = cantdias
  console.log(cantdias)
}