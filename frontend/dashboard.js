function dashboard(user) {
    document.getElementById("app").innerHTML = `
        <h2>Welcome ${user.name}</h2>
        <p>Authenticated</p>
    `;
}

function showSessionExpiry(time) {
    document.getElementById("session").innerHTML =
        `<p>Session expires in ${time} sec</p>`;
}