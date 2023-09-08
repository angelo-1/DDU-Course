function regn(){
    let a=document.getElementById("password").value;
    let b=document.getElementById("confirmPassword").value;
    let pass= /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    let valid= pass.test(a);
    if (!valid){
        window.alert("password is not valid!")
        a.focus;
        return false;
    }
    else{
    if (a!=b){
        window.alert("Password does not match");
        b.focus;
        return false;
    }
}

}

function calculateAge() {
        var birthdate = new Date(document.getElementById('dob').value);
        var today = new Date();
        var age = today.getFullYear() - birthdate.getFullYear();
        
        if (today.getMonth() < birthdate.getMonth() || (today.getMonth() === birthdate.getMonth() && today.getDate() < birthdate.getDate())) {
          age--;
        }
        document.getElementById('age').textContent = age;
      }
