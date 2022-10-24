var eye = document.getElementById('Eye');
var input = document.getElementById('Input');
eye.addEventListener("click", function(){
    if (input.type === "password") {
        input.type = "text";
        eye.style.opacity = 0.8;
    } else {
        input.type = "password";
        eye.style.opacity = 0.2;
    }
})

function formateoRut(rut)
    {rut.value=rut.value.replace(/[.-]/g, '')
    .replace( /^(\d{1,2})(\d{3})(\d{3})(\w{1})$/, '$1.$2.$3-$4')}