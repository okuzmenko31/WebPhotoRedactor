<template>
    <navbar-comp />
    <div class="therms-container">
        <div class="therms-of-use-content">
            <p class="header_text fs--50 fw--900">FlexFi Upscale Privacy Policy</p>
            <div class="hor-line"></div>
            <div class="therms-of-use-text">
                <p class="white fs--25 fw--900">1. Introduction</p>
                <p class="white fs--20">FlexFi Upscale is committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our website.</p>
                <p class="white fs--25 fw--900">2. Information We Collect</p>
                <p class="white fs--20">We may collect personal and non-personal information when you visit our website. Personal information includes your name, email address, and payment details. Non-personal information includes your IP address and images.</p>
                <p class="white fs--25 fw--900">3. How We Use Your Information</p>
                <p class="white fs--20">We use the collected information to provide and improve our services, personalize your experience, process payments, and communicate with you. We do not sell, trade, or rent your personal information to third parties.</p>
                <p class="white fs--25 fw--900">4. Cookies and Similar Technologies</p>
                <p class="white fs--20">We use cookies and similar technologies to enhance your experience on our website. You can control cookies through your browser settings, but disabling them may limit your access to certain features of the site.</p>
                <p class="white fs--25 fw--900">5. Data Security</p>
                <p class="white fs--20">We employ industry-standard security measures to protect your information from unauthorized access, disclosure, alteration, and destruction.</p>
                <p class="white fs--25 fw--900">6. Third-Party Links</p>
                <p class="white fs--20">Our website may contain links to third-party websites. We are not responsible for the privacy practices or content of these sites. We encourage you to review the privacy policies of any third-party sites you visit.</p>
                <p class="white fs--25 fw--900">7. Changes to This Privacy Policy</p>
                <p class="white fs--20">FlexFi Upscale reserves the right to update or change this Privacy Policy at any time. Any changes will be effective immediately upon posting the updated policy on the website.</p>
                <p class="white fs--25 fw--900">8. Contact Us</p>
                <p class="white fs--20">If you have any questions about this Privacy Policy, please contact us at <a class="contact_email fs--20 no-top align_center_text" target="_blank" rel="noreferrer" href="mailto:koooilrekt@gmail.com?subject=Contact%20Us">koooilrekt@gmail.com</a></p>
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