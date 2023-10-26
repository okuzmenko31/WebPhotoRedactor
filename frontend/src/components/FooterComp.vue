<template>
    <footer class="white">
        <div class="footer-content">
            <h1>FlexFi Upscale</h1>
            <p class="fs--15 fw--100">Upgrade your images with
                with our powerful tools in just a few clicks.
                Join a mass of Users Using FlexFi Upscale to Save
                time and get great results!
            </p>
            <router-link class="link" style="text-decoration: underline" to="/terms_of_use">Terms of use</router-link>
            <router-link class="link" style="text-decoration: underline" to="/privacy_policy">Privacy Policy</router-link>
            <router-link class="link" style="text-decoration: underline" to="/contact_us">Contact Us</router-link>
            <p class="fs--12 fw--100">Copyright | ©2023 FlexFi Upscale</p>
        </div>
    </footer>
</template>

<script>
    export default {
        
    }
</script>

<style>
footer {
    position: relative;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
    height: auto;
    padding: 20px 0;
    background-color: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(25px);
    margin-top: 100px;
    z-index: 1;
}
.footer-content {
    width: 40%;
    height: auto;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

@media (max-width: 767px) {
    .footer-content {
        width: 60%;
    }
}
</style>