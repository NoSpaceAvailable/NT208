<script setup>
import { ref, onMounted } from "vue";

const user = ref(null);

onMounted(() => {
    google.accounts.id.initialize({
        client_id: "YOUR_GOOGLE_CLIENT_ID",
        callback: handleCredentialResponse,
    });

    google.accounts.id.renderButton(document.getElementById("google-login"), {
        theme: "outline",
        size: "large",
    });
});

const handleCredentialResponse = (response) => {
    const credential = response.credential;
    console.log("Google JWT Token:", credential);
    user.value = JSON.parse(atob(credential.split(".")[1])); // Decode JWT payload
};
</script>

<template>
    <div>
        <div id="google-login"></div>
        <div v-if="user">
            <p>Welcome, {{ user.name }}</p>
            <img :src="user.picture" alt="User Image" width="50" />
        </div>
    </div>
</template>
