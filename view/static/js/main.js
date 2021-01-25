function validate() {
    let email = document.sign_up_form.email;
    let username = document.sign_up_form.username;
    let password1 = document.sign_up_form.password1;
    let password2 = document.sign_up_form.password2;

    let email_error = document.getElementById("email_error");
    let username_error = document.getElementById("username_error");
    let password1_error = document.getElementById("password1_error");
    let password2_error = document.getElementById("password2_error");

    // Clear earlier error messages
    email_error.innerHTML = "";
    username_error.innerHTML = "";
    password1_error.innerHTML = "";
    password2_error.innerHTML = "";

    //Email check
    if (!/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email.value)) {
            email_error.innerHTML = 'Ange email i formatet namn@email.se.'
            return false;
        }

    // Username check
    if(username.value.length < 4) {
        username_error.innerHTML = 'Användarnamnet måste vara minst 4 tecken långt.';
        return false;
    }

    // Password checks
    if(password1.value.length < 8) {
        password1_error.innerHTML = 'Lösenordet ska vara minst 8 tecken långt.';
        return false;
    }

    if(password1.value !== password2.value) {
        password2_error.innerHTML = 'Lösenorden machar inte.';
        return false;
    }
    return true;
}

