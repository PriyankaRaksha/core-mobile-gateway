function dashboard(user) {
    document.getElementById("app").innerHTML = `
        <h2>Welcome ${user.name}</h2>
    `;
}