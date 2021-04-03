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

{/* <script src="https://www.gstatic.com/firebasejs/8.3.1/firebase-app.js"></script>
        <script src="https://www.gstatic.com/firebasejs/8.3.1/firebase-analytics.js"></script>
        <script>
            email = document.getElementById("email").value
            password = document.getElementById("psw").value
            var firebaseConfig = {
                apiKey: "AIzaSyDhaOjFCuvGvfiavpNsBJ64OUcW4PUCPmg",
                authDomain: "jeevan-naksha.firebaseapp.com",
                databaseURL: "https://jeevan-naksha-default-rtdb.firebaseio.com",
                projectId: "jeevan-naksha",
                storageBucket: "jeevan-naksha.appspot.com",
                messagingSenderId: "283736840553",
                appId: "1:283736840553:web:2448f0845323a8fb5b05f8",
                measurementId: "G-TZ00CV5RM6"
            };
            firebase.initializeApp(firebaseConfig);
            firebase.auth().createUserWithEmailAndPassword(email, password).catch(
                function(error) 
                {
                    var errorCode = error.code;
                    var errorMessage = error.message;
                    console.log(errorCode)
                    console.log(errorMessage)
                }
            );
        </script> */}