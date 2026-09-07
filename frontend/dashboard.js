function dashboard(user) {
    document.getElementById("app").innerHTML = `
        <h2>Welcome ${user.name}</h2>
        <p>Authenticated</p>
    `;
}

function clearSessionUI() {
    document.getElementById("session").innerHTML =
        "<p>Logged out</p>";
}

function showSessionExpiry(time) {
  const sessionElement = document.getElementById("session");
  if (sessionElement) {
    sessionElement.textContent = `Session expires in ${time} sec`;
  }
}