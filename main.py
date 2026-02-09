from pyscript import document, display

def password_authenticator(e):
    password = document.getElementById('input2').value
    output = document.getElementById("output")

    output.innerHTML = ""

    count = 0
    for char in password:
        count += 1

    if not password.isalpha():
        if password.isdigit():
            display("Must contain at least one letter", target="output")
        else:
            if count < 10:
                display("Must be 10 characters long", target="output")
            else:
                display("Thank you for submitting!", target="output")
    else:
        display("Must contain at least one number", target="output")
