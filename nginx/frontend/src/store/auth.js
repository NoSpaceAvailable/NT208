async function isAuthenticated() {
    const resp = await fetch("/api/auth/check", {
        method: "GET",
        credentials: "include"
    });
    const data = await resp.json();
    return data.status === "ok";
}

export default {
    isAuthenticated
}