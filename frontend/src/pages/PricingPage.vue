<template>
  <navbar-comp />
  <div class="pricing-container">

    <div class="pricing-block">
      <p class="brand_text">Our plans</p>
    <p class="fs--50 fw--700 header_text align_center_text no-top">Pricing</p>
        <div class="tarrifs-row">
          <card v-for="plan in plans"
              :key="plan.id"
              :sub_id="plan.id"
              :Upcount="plan.up_scales_count"
              :BgRemcount="plan.bg_deletions_count"
              :JPEGcount="plan.jpg_artifacts_deletions_count"
              :name="plan.name"
              :price="plan.price + '$'"
              :PayPal="plan.paypal_plan_id"
          />
        </div>
    </div>

    <div class="plans-contain-block">
      <div class="flex-block gp--15" :key="index" v-for="(contain, index) in plansContain">
        <img :src="checkmark" style="width: 15px; height: 15px;" alt="checkmark"/>
        <p>{{ contain }}</p>
      </div>
    </div>

    <pricing-questions />
  </div>
  <footer-comp />
</template>

<script>
  import PricingQuestions from "@/components/PricingQuestions.vue";
  import Card from "@/components/UI/TarrifCard.vue";
  import NavbarComp from "@/components/NavbarComp.vue";
  import FooterComp from "@/components/FooterComp.vue";
  import handlePopState from "@/utils/index.js";
  import axios from 'axios';
  export default {
    components: {
      Card,
      NavbarComp,
      FooterComp,
      PricingQuestions
    },
    mounted() {
      handlePopState(),
      axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/plans`)
      .then(res => {
        this.plans = res.data
      })
      document.title = `FlexFi Upscale - Pricing`
    },
    data() {
      return {
          plans: [],
          plansContain: ['Custom backgrounds', 'Images without watermark', 'Credits for usage'],
          checkmark: require("@/assets/checkmark.png")
      };
    }
  }
</script>

<style>
.pricing-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  z-index: 1;
  gap: 200px;
}

.pricing-block {
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.plans-contain-block {
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap
}

.tarrifs-row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 40px;
}
</style>