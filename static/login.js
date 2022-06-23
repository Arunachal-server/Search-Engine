var login = function () {
    var login = document.getElementById("login");
    var password = document.getElementById("password");
    const xhr = new XMLHttpRequest();
    payload = {
        "login": login.value,
        "password": password.value
    }
    console.log(payload);
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
    xhr.send(JSON.stringify(payload));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.message == "success") {
                window.location.href = "/search";
            }
            else{
                alert("Invalid Credentials");
            }
        }
    }
}