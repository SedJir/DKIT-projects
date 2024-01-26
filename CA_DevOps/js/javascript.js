function readLocalStorage(){
    document.getElementById('nameLocal').innerHTML = localStorage.getItem("name")
    document.getElementById('surnameLocal').innerHTML = localStorage.getItem("surname")
    document.getElementById('genderLocal').innerHTML = localStorage.getItem("gender")
    document.getElementById('emailLocal').innerHTML = localStorage.getItem("email")
    document.getElementById('telLocal').innerHTML = localStorage.getItem("tel")
    document.getElementById('dateOfBirthLocal').innerHTML = localStorage.getItem("dateOfBirth")
    document.getElementById('passwordLocal').innerHTML = localStorage.getItem("password")
}

function  saveToLocalStorage(){
    let name = document.getElementById("name").value;
    let surname = document.getElementById("surname").value;
    let genderMale = document.getElementById('male').checked;
    let genderFemale = document.getElementById('female').checked;
    let email = document.getElementById("email").value;
    let tel = document.getElementById('tel').value;
    let dateOfBirth = document.getElementById('dateOfBirth').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirmPassword').value;
    if (password !== confirmPassword) {
        alert("confirm password is incorrect")
        return;
    }
    if (!name || !surname || !(genderMale || genderFemale) || !email || !tel || !dateOfBirth || !password || !confirmPassword) {
        alert("Please fill in all fields");
        return;
    }

    // write into local storage
    localStorage.setItem('name',name)
    localStorage.setItem('surname',surname)
    if (document.getElementById('male').checked){
        localStorage.setItem('gender', document.getElementById('male').value)
    }
    else if (document.getElementById('female').checked) {
        localStorage.setItem('gender', document.getElementById('female').value)
    }
    localStorage.setItem('email',email)
    localStorage.setItem('tel', tel)
    localStorage.setItem('dateOfBirth', dateOfBirth)
    localStorage.setItem('password', password)
}