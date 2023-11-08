import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "../pages/MainPage.vue";
import PricingPage from "../pages/PricingPage.vue";
import FeaturesPage from "../pages/FeaturesPage.vue";
import LoginPage from "../pages/LoginPage.vue";
import SignupPage from "../pages/SignupPage.vue";
import ProfilePage from "../pages/ProfilePage.vue";
import PaymentPage from "../pages/PaymentPage.vue";
import ConfirmPage from "../pages/ConfirmPage.vue";
import ChangePassword from "../pages/ChangePassword.vue";
import ChangePasswordEmail from "../pages/ChangePasswordEmail.vue";
import ChangeEmail from "../pages/ChangeEmail.vue";
import ImagePage from "../pages/ImagePage.vue";
import paypalSuccess from "../pages/SuccessPaypalPage.vue";
import stripeSuccess from "../pages/SuccessStripePage.vue";
import paypalCancel from "../pages/CancelPaypalPage.vue";
import stripeCancel from "../pages/CancelStripePage.vue";
import IPP from "../pages/InterimPaymentPaypal.vue";
import IPS from "../pages/InterimPaymentStripe.vue";
import ThermsOfUsePage from "../pages/ThermsOfUsePage.vue";
import PrivacyPolicyPage from "../pages/PrivacyPolicyPage.vue";
import ContactUs from "../pages/ContactUsPage.vue";

import NotifiedPaymentPage from "../pages/NotifiedPaymentPage.vue";
import NIPP from "../pages/NotifiedInterimPaymentPaypal.vue";
import NIPS from "../pages/NotifiedInterimPaymentStripe.vue";
import notifiedPaypalSuccess from "../pages/NotifiedSuccessPaypalPage.vue";
import notifiedStripeSuccess from "../pages/NotifiedSuccessStripePage.vue";
import notifiedPaypalCancel from "../pages/NotifiedCancelPaypalPage.vue";
import notifiedStripeCancel from "../pages/NotifiedCancelStripePage.vue";


const routes = [
    {
        path: '/',
        name: 'Main',
        component: MainPage
    },
    {
        path: '/pricing',
        name: 'Pricing',
        component: PricingPage
    },
    {
        path: '/features',
        name: 'Features',
        component: FeaturesPage
    },
    {
        path: '/login',
        name: 'Log in',
        component: LoginPage
    },
    {
        path: '/signup',
        name: 'Sign Up',
        component: SignupPage
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfilePage
    },
    {
        path: '/payment',
        name: 'Payment',
        component: PaymentPage
    },
    {
        path: '/email_confirmation',
        name: 'Email confirmation',
        component: ConfirmPage
    },
    {
        path: '/reset_password',
        name: 'Resseting password',
        component: ChangePasswordEmail
    },
    {
        path: '/reset_password_confirmation',
        name: 'Resseting password confirmation',
        component: ChangePassword
    },
    {
        path: '/change_email_confirmation',
        name: 'Change email confirmation',
        component: ChangeEmail
    },
    {
        path: '/image_upload',
        name: 'Image upload',
        component: ImagePage
    },
    {
        path: '/payment/paypal/success',
        name: 'Paypal success',
        component: paypalSuccess
    },
    {
        path: '/payment/paypal/cancel',
        name: 'Paypal cancel',
        component: paypalCancel
    },
    {
        path: '/payment/stripe/success',
        name: 'Stripe success',
        component: stripeSuccess
    },
    {
        path: '/payment/stripe/cancel',
        name: 'Stripe cancel',
        component: stripeCancel
    },
    {
        path: '/payment/paypal/creating_order',
        name: 'Creating Paypal order',
        component: IPP
    },
    {
        path: '/payment/stripe/creating_order',
        name: 'Creating Stripe order',
        component: IPS
    },
    {
        path: '/payment/notified',
        name: 'Notified payment',
        component: NotifiedPaymentPage
    },
    {
        path: '/payment/paypal/creating_notified_order',
        name: 'Creating Notified Paypal order',
        component: NIPP
    },
    {
        path: '/payment/stripe/creating_notified_order',
        name: 'Creating Notified Stripe order',
        component: NIPS
    },
    {
        path: '/payment/paypal/notified_success',
        name: 'Notified Paypal success',
        component: notifiedPaypalSuccess
    },
    {
        path: '/payment/paypal/notified_cancel',
        name: 'Notified Paypal cancel',
        component: notifiedPaypalCancel
    },
    {
        path: '/payment/stripe/notified_success',
        name: 'Notified Stripe success',
        component: notifiedStripeSuccess
    },
    {
        path: '/payment/stripe/notified_cancel',
        name: 'Notified Stripe cancel',
        component: notifiedStripeCancel
    },
    {
        path: '/privacy_policy',
        name: 'Privacy policy',
        component: PrivacyPolicyPage
    },
    {
        path: '/terms_of_use',
        name: 'Terms of Use',
        component: ThermsOfUsePage
    },
    {
        path: '/contact_us',
        name: 'Contact Us',
        component: ContactUs
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(import.meta.env.BASE_URL)
})

export default router