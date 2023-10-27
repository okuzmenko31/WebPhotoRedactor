<template>
    <div class="interim-container">
        <div v-show="error" id="success" class="white">
            <p class="align_center_text">{{ message }}</p>
            <p style="color: yellow" class="align_center_text">You'll be automaticly redirected</p>
        </div>
        <page-loader v-show="!error"/>
    </div>
</template>

<script>
    import axios from 'axios'
    import PageLoader from "@/components/UI/PageLoader.vue";
    import handlePopState from "@/utils/index.js";
    import { getHeaders, fetchToken, getLocalEmail, getLocalFullName } from '@/Auth';
    import router from '@/router/router';

    export default {
        components: {
            PageLoader
        },
        async mounted() {
            handlePopState()
            if (await fetchToken() === true) {
                this.createPaypalOrder()
            } else {
                this.createPaypalOrder(getLocalEmail(), getLocalFullName())
            }
            if (this.$route.query.sub_id === undefined)  {
                router.push({ path: "/pricing" })
            }
        },
        created() {
            window.scrollTo(0, 0);
        },
        data() {
            return {
                paypalCreateOrderLink: `/api/v1/payments/paypal/create_order/${this.$route.query.sub_id}/`,
                message: "",
                error: false
            }
        },
        methods: {
            createPaypalOrder(email, name) {
                if (name === undefined && email === undefined) {
                    axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.paypalCreateOrderLink}`, {}, { headers: getHeaders() })
                    .then(res => {
                        window.location.href = res.data.payment_link
                    })
                    .catch(err => {
                        console.log(err);
                        this.error = true
                        let errorMsg
                        if (err.response.data.error) {
                            errorMsg = err.response.data.error
                        } else if (err.response.data.detail) {
                            errorMsg = err.response.data.detail
                        }

                        this.message = 'Transaction failure. ' + errorMsg
                        const success_window = document.getElementById('success');
                        const loader = document.querySelector('.preload');
                        if (success_window) {
                            success_window.style.backgroundColor = 'rgb(255, 000, 100)'
                            success_window.classList.add('visible');
                            loader.classList.add('hide');
                            setTimeout(() => {
                                success_window.classList.remove('visible');
                                loader.classList.remove('hide');
                                router.back(err.response.data.email)
                            }, 3000);
                        }
                    })
                } else {
                    axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.paypalCreateOrderLink}`, {
                        'email': email,
                        'full_name': name
                    })
                        .then(res => {
                            window.location.href = res.data.payment_link
                        })
                        .catch(err => {
                            console.log(err);
                            this.error = true
                            let errorMsg
                            if (err.response.data.error) {
                                errorMsg = err.response.data.error
                            } else if (err.response.data.detail) {
                                errorMsg = err.response.data.detail
                            } else if (err.response.data.email) {
                                errorMsg = err.response.data.email[0]
                            }

                            this.message = 'Transaction failure. ' + errorMsg
                            const success_window = document.getElementById('success');
                            const loader = document.querySelector('.preload');
                            if (success_window) {
                                success_window.style.backgroundColor = 'rgb(255, 000, 100)'
                                success_window.classList.add('visible');
                                loader.classList.add('hide');
                                setTimeout(() => {
                                    success_window.classList.remove('visible');
                                    loader.classList.remove('hide');
                                    router.back(err.response.data.email)
                                    
                                }, 3000);
                        }
                    })
                }
            }
        }
    }
</script>

<style>
.interim-container {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center
}
</style>