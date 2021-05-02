function checkPass() 
{
    originalPassword = document.getElementById('o_psw').value
    confirmPassword = document.getElementById('c_psw').value
    if(originalPassword == confirmPassword)
    {
        document.getElementById('res').innerHTML = ""
        return true
    }
    else
    {
        document.getElementById('res').innerHTML = "Passwords do not match! Try again"
        return false
    }
}   

function showPass() {
    var x = document.getElementById('o_psw');
    var y = document.getElementById('c_psw');
    if (x.type === "password") {
      x.type = "text";
      y.type = "text";
    } else {
      x.type = "password";
      y.type = "password";
    }
}
function show_pass() {
  var x = document.getElementById('o_psw');
  
  if (x.type === "password") {
    x.type = "text";
    
  } else {
    x.type = "password";
    
  }
}