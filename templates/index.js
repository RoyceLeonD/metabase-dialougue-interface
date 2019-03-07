function login(form) {
    var username = form.username.value;
    var password = form.password.value;

    const url='http://localhost:3000/api/session';
    fetch(url)
        .then(function(response){
            return response.json();
        })
        .then(function(jsonResponse) {
            var public = jsonResponse.id
        })
}