<template>
  <navbar-comp />
  <div class="main-container">
    <div class="main-page">
      <div class="whatis-block white">
        <p class="brand_text">About us</p>
        <p class="fs--50 fw--700 header_text align_center_text no-top few-padding">What is FlexFi Upscale?</p>
        <div class="whatis-about">
          <h1 class="fs--25 fw--400 whatis-text-desc small_text">It's a website where you have all tools in your hand. From upscaling to removing bacgkrounds.</h1>
          <div class="whatis-block-block">
            <router-link v-if="!isAuthenticated" class="main_signup_btn" to="/signup">Start upscaling</router-link>
            <router-link v-else class="main_signup_btn" to="/pricing">Buy plan</router-link>
          </div>
        </div>
      </div>
      <div class="tools-usage-block">
        <p class="brand_text">Our tools</p>
        <p class="fs--50 fw--700 header_text no-top align_center_text few-padding">We have many tools for your usage</p>
        <div class="tools-cards-block">
          <tool-card name="Upscaling" description="
          Upscale your image resolution and quality just in one click
          "
          :before_img="Img"
          :after_img="Img2"
          />
          <tool-card name="Background remove" description="
          Remove background instantly from your photo
          "
          :before_img="Bg"
          :after_img="Bg2"
          />
          <tool-card name="Remove JPEG Artifacts" description="
          Remove JPEG artifacts from your photo and forget about them
          "
          :before_img="JPEG"
          :after_img="JPEG2"
          />
        </div>
      </div>
      <div class="why-us-block">
          <p class="brand_text">Preferences</p>
          <p class="fs--50 fw--700 header_text no-top align_center_text few-padding">Why would you choose us?</p>
          <div class="why-us-block">
            <div class="why-us-table-features">
              <div class="why-item">
                <p class="fs--33 fw--700 white width--100">Transforming Cities: Unique FlexFi Upscale</p>
                <p class="fs--15 fw--400 small_text width--100">FlexFi Upscale - your gateway to transforming urban landscapes! We remove building backgrounds from your pictures, allowing you to enhance and enlarge them effortlessly. Rediscover the beauty of your cityscapes with FlexFi Upscale.</p>
              </div>
              <div class="line-vertical-1"></div>
              <div class="why-item">
                <p class="fs--33 fw--700 white width--100">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text width--100">s</p>
              </div>
            </div>
            <div class="horizontal-line"></div>
            <div class="why-us-table-features">
              <div class="why-item">
                <p class="fs--33 fw--700 white width--100">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text width--100">s</p>
              </div>
              <div class="line-vertical-2"></div>
              <div class="why-item">
                <p class="fs--33 fw--700 white width--100">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text width--100">s</p>
              </div>
            </div>
          </div>
      </div>
      <use-cases-block />
      <often-questions />
      <div class="get-started-main-block payment_info_block flex-block column center white gp--50">
        <img style="width: 100px; height: 100px;" :src="Logo">
        <p class="no-margin fw--900 fs--50 align_center_text">Get started</p>
        <p v-if="!isAuthenticated" class="no-margin fw--400 fs--15 width--30 align_center_text">Sign up for a free attemps, you can upgrade to a plan that suits your needs.</p>
        <p v-else class="no-margin fw--400 fs--15 width--30 align_center_text">Buy plan to get more attemps.</p>
        <router-link v-if="!isAuthenticated" class="main_signup_btn" to="/signup">Get started</router-link>
        <router-link v-else class="main_signup_btn" to="/pricing">Buy plan</router-link>
      </div>
    </div>
  </div>
  <footer-comp />
</template>

<script>
    import NavbarComp from "@/components/NavbarComp.vue";
    import OftenQuestions from "@/components/OftenQuestion.vue";
    import UseCasesBlock from "@/components/UseCasesBlock.vue";
    import ToolCard from "@/components/UI/ToolCard.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import handlePopState from "@/utils/index.js";
    import { fetchToken } from '@/Auth.js';

    export default {
        components: {
          NavbarComp,
          ToolCard,
          OftenQuestions,
          FooterComp,
          UseCasesBlock
        },
        data() {
          return {
            Img: require('@/assets/car.jpg'),
            Img2: require('@/assets/car2.png'),
            Bg: require('@/assets/car.jpg'),
            Bg2: require('@/assets/car.jpg'),
            JPEG: require('@/assets/car.jpg'),
            JPEG2: require('@/assets/car.jpg'),
            Logo: require('@/assets/Logo.jpg'),
            isAuthenticated: false
          }
        },
        async created() {
          const result = await fetchToken();
          this.isAuthenticated = result;
        },
        mounted() {
          handlePopState()
          document.title = `FlexFi Upscale - Main`
          const scrollElement = document.documentElement
          if (scrollElement) {
            scrollElement.style.overflow = 'hidden';
            scrollElement.scrollTop = 0;
            setTimeout(function() {
              scrollElement.style.overflow = '';
            }, 10);
          }
        }
    }
</script>

<style>
.main-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.main-page {
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 250px;
  z-index: 1;
}

.tools-usage-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  gap: 10px;
}

.whatis-about h1 {
  width: 90%;
}

.tools-cards-block {
  display: flex;
  gap: 20px;
}

.whatis-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  gap: 10px;
}

.whatis-about {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  gap: 30px;
}

.whatis-img {
  width: 90%;
  background: linear-gradient(white, white) padding-box,
  linear-gradient(to right, #abadff, #d091fa) border-box;
  border-radius: 20px;
  border: 4px solid transparent;
}

.whatis-text-desc {
  width: 45%;
}

.whatis-block-block {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50%;
}


.check-pricing {
  width: auto;
  height: 35px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  text-decoration: 0;
  background: transparent;
  border-radius: 10px;
  cursor: pointer;
  background: #d091fa;
  border: 0;
  transition: .3s;
}

.check-pricing:hover {
    background: #9069aa;
}

.whatis__btn {
  width: 100%;
}

.why-us-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.why-us-table-features {
  display: flex;
  justify-content: space-between;
  width: 80%;
  max-width: 80%;
}

.line-vertical-1 {
    width: 2px;
    opacity: 0.3;
    background: linear-gradient(0deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.line-vertical-2 {
    width: 2px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.horizontal-line {
    height: 2px;
    width: 100%;
    opacity: 0.3;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 50%, rgba(255, 255, 255, 0) 100%);
}

.why-item {
  padding: 24px;
  width: 50%;
  overflow-wrap: anywhere;
  align-items: center;
  justify-content: center;
}

.main_signup_btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-decoration: 0;
    background: transparent;
    padding: 0 10px;
    width: 50%;
    height: 35px;
    border-radius: 10px;
    cursor: pointer;
    background: #d091fa;
    border: 0;
    transition: .3s;
}

.main_signup_btn:hover {
    background: #9069aa;
}

.get-started-main-block {
  width: 90% !important;
}

@media (min-width: 768px) and (max-width: 991px) {
  .tools-cards-block {
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 100%;
  }

  .why-item {
    width: auto;
    align-items: center;
  }

  .why-us-block {
    width: 100%;
  }
}

@media (min-width: 651px) and (max-width: 767px) {
  .tools-cards-block {
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 100%;
  }

  .why-item {
    width: auto;
    align-items: center;
  }

  .why-us-block {
    width: 100%;
  }
}

@media (min-width: 481px) and (max-width: 650px) {
  .whatis-block h1 {
    margin: 0;
  }

  .tools-cards-block {
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 100%;
  }

  .why-item {
    width: auto;
    align-items: center;
  }

  .why-us-block {
    width: 100%;
  }

  .get-started-main-block .width--30 {
    width: 70%
  }
}

@media (max-width: 480px) {
  .main-page {
    padding: 20px
  }

  .whatis-block h1 {
    margin: 0;
  }

  .whatis-text-desc {
    font-size: 15px;
  }

  .whatis-block-block {
    width: 100%;
  }

  .tools-cards-block {
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 100%;
  }

  .why-item {
    width: auto;
    align-items: center;
  }

  .why-us-block {
    width: 100%;
  }

  .get-started-main-block .width--30 {
    width: 70%
  }
}
</style>