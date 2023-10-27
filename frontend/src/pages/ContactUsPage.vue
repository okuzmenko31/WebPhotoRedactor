<template>
    <navbar-comp />
    <div class="contact-us-container">
        <div class="contact-us">
            <p class="brand_text align_center_text no-margin">Support</p>
            <p class="header_text fw--900 fs--50 align_center_text no-top">Contact Us</p>
            <div class="contact-us-form">
                <div class="contact-us-category-choose" style="z-index: 2;">
                    <p>Category:</p>
                    <div id="category-dropdown">
                        <div @click="openCategoryChoose" id="category-arrow"><svg height="15px" viewBox="0 0 5 9"><path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path></svg></div>
                        <span id="category-selected" @click="openCategoryChoose">
                            {{category}}
                        </span>
                        <div id="category-menu">
                            <li v-for="(category_, index) in categories" :key="index" v-bind:data-dd-value="category_" @click="categoryClick">
                                {{ category_ }}
                            </li>
                        </div>
                    </div>
                </div>
                <input-ui inputId="border_white_contact_us" max="50" v-model="email" pr="Email" />
                <textarea id="message-input-id" placeholder="Your message" required :maxlength="4000" v-model="text"></textarea>
                <div class="flex-block center width--100 column">
                    <button class="contact_us_btn" @click="sendMail">Send mail</button>
                    <p class='error_text_contact'>{{ message }}</p>
                </div>
            </div>
        </div>

        <p class="brand_text" style="margin-top: 120px;">Our contacts</p>
        <p class="header_text fw--900 fs--50 align_center_text no-top">If you need help contact us by email</p>
        <div class="support-alt-block">
            <img :src="supportImg" class="support-image" alt="support"/>
            <div class="support-sub-block">
                <div class="width--100 flex-block column white">
                    <p class="fs--50 fw--900 no-margin">Email us</p>
                    <p class="fs--15 no-margin">For any inqueries, data breaches, concerns, security practices, or any other information, kindly contact us on:</p>
                    <a class="contact_email fs--15" target="_blank" rel="noreferrer" href="mailto:koooilrekt@gmail.com?subject=Contact%20Us">koooilrekt@gmail.com</a>
                </div>
                <div class="width--100 flex-block column white">
                    <p class="fs--50 fw--900 no-margin">Reach us</p>
                    <p class="fs--15 no-margin">Shopsense Retail Technologies Limited</p>
                    <p class="fs--15 no-margin">1st Floor, Wework Vijay Diamond,</p>
                    <p class="fs--15 no-margin">Cross Rd B, Ajit Nagar,</p>
                    <p class="fs--15 no-margin">Kondivita, Andheri East,</p>
                    <p class="fs--15 no-margin">Mumbai, Maharashtra - 400069</p>
                    <p class="contact_email fs--15 no-margin">+3809629012424</p>
                </div>
            </div>
        </div>
    </div>
    <footer-comp />
</template>

<script>
    import axios from 'axios';
    import NavbarComp from "@/components/NavbarComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import InputUi from "@/components/UI/InputUi.vue";
    import handlePopState from "@/utils/index.js";

    export default {
        components: {
            NavbarComp,
            FooterComp,
            InputUi
        },
        created() {
            window.scrollTo(0, 0);
        },
        mounted() {
            handlePopState()
            axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/main/help_request_categories/`)
            .then(res => {
                this.categories = res.data
                this.category = this.categories[0]
            })
        },
        data() {
            return {
                email: "",
                text: "",
                category: "",
                categories: [],
                message: "",
                supportImg: require("@/assets/Support.png")
            }
        },
        methods: {
            sendMail() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/main/help_request/`, {
                    "request_type": this.category,
                    "email": this.email,
                    "text": this.text
                })
                .then(() => {
                    this.message = ""
                    this.message = "Mail was sent to support!"
                    const message = document.querySelector('.error_text_contact')
                    if (message) {
                        message.style.color = "#00FF00"
                    }
                })
                .catch(err => {
                    this.message = ""
                    const message = document.querySelector('.error_text_contact')
                    if (message) {
                        message.style.color = "#ff0000"
                    }
                    if (err.response.data.email || err.response.data.text || err.response.data.request_type) {
                        if (err.response.data.request_type) {
                            this.message = err.response.data.request_type[0]
                        } else if (err.response.data.email) {
                            this.message = err.response.data.email[0]
                            const email = document.getElementById('border_white_contact_us')
                            if (email) {
                                email.style.border = "2px #ff0000 solid"
                                setTimeout(() => {
                                    email.style.border = "2px #ffffff3d solid"
                                }, 2000)
                            }
                        } else if (err.response.data.text) {
                            this.message = err.response.data.text[0]
                            const text = document.getElementById('message-input-id')
                            if (text) {
                                text.style.border = "2px #ff0000 solid"
                                setTimeout(() => {
                                    text.style.border = "2px #ffffff3d solid"
                                }, 2000)
                            }
                        }
                    } else {
                        this.message = 'Something went wrong!'
                    }
                })
            },
            openCategoryChoose() {
                const dd = document.getElementById('category-arrow');
                const menu = document.getElementById('category-menu');
                dd.classList.toggle('active');
                menu.classList.toggle('visible');
            },
            categoryClick(event) {
                const dd = document.getElementById('category-arrow');
                const menu = document.getElementById('category-menu');
                if (event) {
                    const selectedСategory = event.target.getAttribute("data-dd-value");
                    this.category = selectedСategory;
                    const categoryItems = document.querySelectorAll('#category-menu li');
                    categoryItems.forEach(item => {
                        item.classList.remove('active');
                    });
                    event.target.classList.add('active');
                    dd.classList.remove('active');
                    menu.classList.remove('visible');
                }
            },
        }
    }
</script>

<style>
.contact-us-container {
    width: 100%;
    display: flex;
    padding-top: 200px;
    box-sizing: border;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 1;
}

.contact-us {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.contact-us-form {
    width: 80%;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    gap: 20px;
}

.contact-us-category-choose {
    display: flex;
    align-items: center;
    color: #ffffff;
    border-radius: 20px;
    gap: 20px;
    width: 100% !important;
}

#message-input-id {
    width: 100%;
    height: 200px !important;
    resize: none;
    background: transparent;
    box-sizing: border-box;
    border: 2px #ffffff3d solid;
    outline: none;
    padding-left: 10px;
    color: #ffffff;
    border-radius: 10px;
    transition: .3s;
}

#border_white_contact_us {
    border: 2px #ffffff3d solid;
}

#width--200 {
    width: 200px !important;
}

#message-input-id:focus {
    scale: 110%
}

#category-dropdown {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

#category-arrow {
    position: absolute;
    cursor: pointer;
    right: 10px;
    transform: rotate(90deg) translateX(130%);
    stroke: #fff;
}

#category-arrow.active {
    transform: rotate(270deg) translateX(-90%) translateY(2px);
}

#category-selected {
    background: #3b3f4d;
    padding: 10px 25px 10px 10px;
    border-radius: 15px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: .3s;
}

#category-selected:hover {
    background: #4a4e5d;
}

#category-menu {
    position: absolute;
    display: none;
    flex-direction: column;
    align-items: center;
    right: 50%;
    transform: translateX(50%);
    top: 50px;
    background: #3b3f4d;
    padding: 20px;
    border-radius: 20px;
    gap: 20px;
    list-style: none;
    color: #fff;
    max-height: 200px;
    overflow-y: auto;
    z-index: 2;
    overflow-x: hidden
}

#category-menu li {
    padding: 10px 25px;
    border-radius: 10px;
    cursor: pointer;
    transition: .3s;
}

#category-menu li:hover {
    background-color: #0000006b;
    scale: 110%
}

#category-menu li.active {
    background-color: #0000006b;
    scale: 110%
}

.contact_us_btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-decoration: 0;
    background: transparent;
    width: 130px;
    height: 35px;
    border-radius: 10px;
    cursor: pointer;
    background: #d091fa;
    border: 0;
    transition: .3s;
}

.contact_us_btn:hover {
    background: #9069aa;
}

.support-alt-block {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 80%;
    padding: 60px;
    box-sizing: border-box;
    background: linear-gradient(rgba(45, 47, 70, 0.08) 0%, rgba(255, 255, 255, 0) 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
}

.support-sub-block {
    display: flex;
    flex-direction: column;
    color: #ffffff;
    width: 40%;
    gap: 40px;
}

.support-image {
    width: 40%
}

@media (min-width: 992px) and (max-width: 1199px) {
    .support-alt-block {
        flex-direction: column
    }

    .support-sub-block {
        width: 80%;
    }

    .support-image {
        width: 60%
    }
}

@media (min-width: 768px) and (max-width: 991px) {
    .support-alt-block {
        flex-direction: column
    }

    .support-sub-block {
        width: 80%;
    }

    .support-image {
        width: 60%
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .support-alt-block {
        flex-direction: column
    }

    .support-sub-block {
        width: 80%;
    }

    .support-image {
        width: 60%
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .support-alt-block {
        flex-direction: column
    }

    .support-sub-block {
        width: 80%;
    }

    .support-image {
        width: 60%
    }
}

@media (max-width: 480px) {
    .contact-us-category-choose {
        flex-direction: column
    }

    .support-alt-block {
        flex-direction: column;
        padding: 30px 0;
    }

    .support-sub-block {
        width: 90%;
    }

    .support-sub-block .fs--50 {
        font-size: 25px;
    }

    .support-sub-block .fs--15 {
        font-size: 12px;
    }

    .support-image {
        width: 90%
    }
}
</style>