async function fetchProfile(username) {
    const res = await fetch(`/profile/${username}`);
    const data = await res.json();
    console.log("Profile:", data);
}