function checkPass() 
{
    originalPassword = document.getElementById('o_psw').value
    confirmPassword = document.getElementById('c_psw').value
    if(originalPassword == confirmPassword)
    {
        document.getElementById('res').innerHTML = "Correct"
        return true
    }
    else
    {
        document.getElementById('res').innerHTML = "Wrong"
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