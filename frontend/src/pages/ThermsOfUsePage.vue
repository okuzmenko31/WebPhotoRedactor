<template>
    <navbar-comp />
    <div class="therms-container">
        <div class="therms-of-use-content">
            <p class="header_text fs--50 fw--900">FlexFi Upscale Terms of Use</p>
            <div class="hor-line"></div>
            <div class="therms-of-use-text">
                <p class="white fs--25 fw--900">1. Introduction</p>
                <p class="white fs--20">Welcome to FlexFi Upscale! These Terms of Use ("Terms") govern your use of our website and services. Please read them carefully.</p>
                <p class="white fs--20">These Terms outline the rules and regulations for the use of FlexFi Upscale's website.</p>
                <p class="white fs--20">By accessing this website, you agree to these Terms. If you disagree with any part of these terms, please do not use our website.</p>
                <p class="white fs--25 fw--900">2. Services</p>
                <p class="white fs--20">FlexFi Upscale provides image upscaling, JPEG artifact removal, background removal, and related services ("Services"). Users can enjoy free credits without registration and explore our features. Registered users receive additional free credits, and have the option to purchase more through paid plans.</p>
                <p class="white fs--25 fw--900">3. User Accounts</p>
                <p class="white fs--20">To access certain features of our Services, you may be required to create an account. You must provide accurate and complete information. It is your responsibility to keep your account secure and confidential. FlexFi Upscale is not liable for any loss or damage arising from your failure to comply with this obligation.</p>
                <p class="white fs--25 fw--900">4. Intellectual Property</p>
                <p class="white fs--20">The content on FlexFi Upscale, unless otherwise stated, is owned or licensed by us. This includes, but is not limited to, text, graphics, logos, and software. You are not permitted to use or reproduce any part of our content without prior written consent.</p>
                <p class="white fs--25 fw--900">5. User Content</p>
                <p class="white fs--20">By submitting content to FlexFi Upscale, you grant us the right to use, modify, adapt, and display that content for the purpose of providing our Services. You are solely responsible for the content you submit, and you must have the necessary rights to do so.</p>
                <p class="white fs--25 fw--900">6. Prohibited Activities</p>
                <p class="white fs--20">While using FlexFi Upscale, you agree not to:</p>
                <p class="white fs--20">Violate any applicable laws or regulations.</p>
                <p class="white fs--20">Infringe upon any intellectual property rights.</p>
                <p class="white fs--20">Distribute malware or engage in any malicious activity.</p>
                <p class="white fs--20">Attempt to gain unauthorized access to our systems.</p>
                <p class="white fs--20">Engage in any activity that disrupts or interferes with our Services.</p>
                <p class="white fs--25 fw--900">7. Termination</p>
                <p class="white fs--20">We reserve the right to terminate your access to FlexFi Upscale, without prior notice or liability, for any reason. Upon termination, your right to use our Services will cease immediately.</p>
                <p class="white fs--25 fw--900">8. Limitation of Liability</p>
                <p class="white fs--20">To the fullest extent permitted by law, FlexFi Upscale and its affiliates shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including but not limited to, damages for loss of profits, goodwill, use, data, or other intangible losses resulting from:</p>
                <p class="white fs--20">Your access to or use of our Services. Any conduct or content of any third party.</p>
                <p class="white fs--25 fw--900">9. Changes to Terms</p>
                <p class="white fs--20">FlexFi Upscale may revise these Terms at any time. By using this website, you are expected to review these Terms periodically.</p>
            </div>
        </div>
    </div>
    <footer-comp />
</template>

<script>
    import NavbarComp from "@/components/NavbarComp.vue";
    import handlePopState from "@/utils/index.js";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        components: {
            NavbarComp,
            FooterComp
        },
        mounted() {
            handlePopState()
        }
    }
</script>

<style>
.therms-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    z-index: 1;
    padding: 50px;
}

.therms-of-use-content {
    width: 60%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    z-index: 1;
    padding: 50px;
}

.therms-of-use-content .fs--50 {
    text-align: center;
}

.therms-of-use-text {
    width: 100%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: flex-start;
}

.therms-of-use-content .hor-line {
    width: 100%;
}

@media (min-width: 768px) and (max-width: 991px) {
    .therms-container {
        padding: 0;
    }

    .therms-of-use-content {
        padding: 0;
        width: 80%
    }

    .therms-of-use-content .fs--50 {
        font-size: 33px;
    }

    .therms-of-use-content .fs--25 {
        font-size: 20px;
    }

    .therms-of-use-content .fs--20 {
        font-size: 15px;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .therms-container {
        padding: 0;
    }

    .therms-of-use-content {
        padding: 0;
        width: 90%
    }

    .therms-of-use-content .fs--50 {
        font-size: 33px;
    }

    .therms-of-use-content .fs--25 {
        font-size: 20px;
    }

    .therms-of-use-content .fs--20 {
        font-size: 15px;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .therms-container {
        padding: 0;
    }

    .therms-of-use-content {
        padding: 0;
        width: 90%
    }

    .therms-of-use-content .fs--50 {
        font-size: 33px;
    }

    .therms-of-use-content .fs--25 {
        font-size: 20px;
    }

    .therms-of-use-content .fs--20 {
        font-size: 15px;
    }
}

@media (max-width: 480px) {
    .therms-container {
        padding: 0;
    }

    .therms-of-use-content {
        padding: 0;
        width: 90%
    }

    .therms-of-use-content .fs--50 {
        font-size: 33px;
    }

    .therms-of-use-content .fs--25 {
        font-size: 20px;
    }

    .therms-of-use-content .fs--20 {
        font-size: 15px;
    }
}
</style>