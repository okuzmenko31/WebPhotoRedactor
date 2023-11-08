<template>
    <navbar-comp />
    <div class="features-container">
        <div class="articles_arts_cont">
            <p class="brand_text">Features</p>
            <h1 class="fs--50 fw--700 header_text align_center_text no-top">FlexFI Upscale features:</h1>
            <div class="articles_container">
                <article-ui name="Upscaling" article="Upscaling increases the size or resolution of an image or video, enhancing its visual quality for larger displays." />
                <article-ui name="Background remove" article="Background Removal is the process of isolating the main subject in an image by eliminating the background." />
                <article-ui name="Remove JPEG Artifacts" article='"Remove Jpeg Artifacts" is the process of eliminating distortions from JPEG compression.' />
            </div>
        </div>

        <div class="more-features-block">
            <div class="flex_block column align_center_text">
                <p class="brand_text">More</p>
                <p class="header_text fs--50 fw--900 no-top">More about FlexFI Upscale Features</p>
            </div>
            <div class="more-features-block-block">
                <article id="upscale" class="width-100 flex-block center">
                    <div class="about-feature-block column">
                        <p class="fs--33 fw--900 width--100 align_center_text">Upscaling</p>
                        <div class="about-contain-all">

                            <div class="swiper-container">
                                <swiper
                                    :modules="modules"
                                    :slides-per-view="1"
                                    :space-between="50"
                                    navigation
                                    :allowTouchMove="false"
                                    :pagination="{ clickable: true }"
                                    @swiper="onSwiper"
                                    @slideChange="onSlideChange"
                                >
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Upscale</p>
                                                <p class="small_text no-margin">Enable users to upload images of any size without compromising photo quality.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="UpImg1" :after_img="UpImg1_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Ultra upscale</p>
                                                <p class="small_text no-margin">More than default upscale. Automatically identifies low-quality images and enhances their overall quality.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="UpImg2" :after_img="UpImg2_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Ultra enhance</p>
                                                <p class="small_text no-margin">Ultra Enhance employs advanced predictive and generative AI technology to upscale photos, filling in missing pixels for a superior smoothing and enhancement effect.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="UpImg3" :after_img="UpImg3_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                </swiper>
                            </div>

                            <div class="about-feature-info white">
                                <div @click="setNewImg($event, 1)" class="article_choose__btn UPSC" :class="upscaleBlock === 1 ? 'active' : '' ">
                                    <p class="fs--25 fw--900 white no-margin">Upscale</p>
                                    <p class="small_text no-margin">Enable users to upload images of any size without compromising photo quality.</p>
                                </div>
                                <div @click="setNewImg($event, 2)" class="article_choose__btn UPSC" :class="upscaleBlock === 2 ? 'active' : '' ">
                                    <p class="fs--25 fw--900 white no-margin">Ultra upscale</p>
                                    <p class="small_text no-margin">More than default upscale. Automatically identifies low-quality images and enhances their overall quality.</p>
                                </div>
                                <div @click="setNewImg($event, 3)" :class="upscaleBlock >= 3 || upscaleBlock < 1 ? 'active' : '' " class="article_choose__btn UPSC">
                                    <p class="fs--25 fw--900 white no-margin">Ultra enhance</p>
                                    <p class="small_text no-margin">Ultra Enhance employs advanced predictive and generative AI technology to upscale photos, filling in missing pixels for a superior smoothing and enhancement effect.</p>
                                </div>
                            </div>
                            <div class="about-feature-image-block">
                                <slider-comp v-if="upscaleBlock === 1" :before_img="UpImg1" :after_img="UpImg1_2" :div_class="sliderClass" />
                                <slider-comp v-else-if="upscaleBlock === 2" :before_img="UpImg2" :after_img="UpImg2_2" :div_class="sliderClass" />
                                <slider-comp v-else :before_img="UpImg3" :after_img="UpImg3_2" :div_class="sliderClass" />
                            </div>
                        </div>
                    </div>
                </article>

                <article id="backgroundremove" class="width-100 flex-block center">
                    <div class="about-feature-block column">
                        <p class="fs--33 fw--900 width--100 align_center_text">Background remove</p>
                        <div class="about-contain-all">

                            <div class="swiper-container">
                                <swiper
                                    :modules="modules"
                                    :slides-per-view="1"
                                    :space-between="50"
                                    navigation
                                    :allowTouchMove="false"
                                    :pagination="{ clickable: true }"
                                    @swiper="onSwiper"
                                    @slideChange="onSlideChange"
                                >
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Background remove</p>
                                                <p class="small_text no-margin">Effortlessly eliminate the background from your image using our Background Remove tool.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="BgImg1" :after_img="BgImg1_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Change background</p>
                                                <p class="small_text no-margin">You can add custom image or color on background. Also you can make it blurry.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="BgImg2" :after_img="BgImg2_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Output type</p>
                                                <p class="small_text no-margin">You can cleanly isolate image subject from background with "cutout". "Mask" output type produces a high-contrast black and white image.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="BgImg3" :after_img="BgImg3_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                </swiper>
                            </div>

                            <div class="about-feature-image-block">
                                <slider-comp v-if="bgBlock === 1" :before_img="BgImg1" :after_img="BgImg1_2" :div_class="sliderClass" />
                                <slider-comp v-else-if="bgBlock === 2" :before_img="BgImg2" :after_img="BgImg2_2" :div_class="sliderClass" />
                                <slider-comp v-else :before_img="BgImg3" :after_img="BgImg3_2" :div_class="sliderClass" />
                            </div>
                            <div class="about-feature-info white">
                                <div @click="setNewImgBg($event, 1)" class="article_choose__btn BGR" :class="bgBlock === 1 ? 'active' : '' ">
                                    <p class="fs--25 fw--900 white no-margin">Background remove</p>
                                    <p class="small_text no-margin">Effortlessly eliminate the background from your image using our Background Remove tool.</p></div>
                                <div @click="setNewImgBg($event, 2)" class="article_choose__btn BGR" :class="bgBlock === 2 ? 'active' : '' ">
                                    <p class="fs--25 fw--900 white no-margin">Change background</p>
                                    <p class="small_text no-margin">You can add custom image or color on background. Also you can make it blurry.</p></div>
                                <div @click="setNewImgBg($event, 3)" :class="bgBlock >= 3 || bgBlock < 1 ? 'active' : '' " class="article_choose__btn BGR">
                                    <p class="fs--25 fw--900 white no-margin">Output type</p>
                                    <p class="small_text no-margin">You can cleanly isolate image subject from background with "cutout". "Mask" output type produces a high-contrast black and white image.</p></div>
                            </div>
                        </div>
                    </div>
                </article>

                <article id="removejpegartifacts" class="width-100 flex-block center">
                    <div class="about-feature-block column">
                        <p class="fs--33 fw--900 width--100 align_center_text">Remove JPEG Artifacts</p>
                        <div class="about-contain-all">
                            <div class="swiper-container">
                                <swiper
                                    :modules="modules"
                                    :slides-per-view="1"
                                    :space-between="50"
                                    navigation
                                    :allowTouchMove="false"
                                    :pagination="{ clickable: true }"
                                    @swiper="onSwiper"
                                    @slideChange="onSlideChange"
                                >
                                    <swiper-slide>
                                        <div class="article_choose__btn active">
                                                <p class="fs--25 fw--900 white no-margin">Strength</p>
                                                <p class="small_text no-margin">Remove jpeg artifacts function improves image quality by reducing compression artifacts in JPEGs. It offers three levels of strength (normal, high, maximal) for tailored artifact removal.</p>
                                        </div>
                                        <div class="about-feature-image-block2">
                                            <slider-comp :before_img="JpegImg1" :after_img="JpegImg1_2" :div_class="sliderClass" />
                                        </div>
                                    </swiper-slide>
                                </swiper>
                            </div>
                            <div class="about-feature-info white">
                                <div @click="setNewImgJpeg($event, 1)" class="article_choose__btn RJPEGA" :class="jpegBlock === 1 ? 'active' : '' ">
                                    <p class="fs--25 fw--900 white no-margin">Strength</p>
                                    <p class="small_text no-margin">Remove jpeg artifacts function improves image quality by reducing compression artifacts in JPEGs. It offers three levels of strength (normal, high, maximal) for tailored artifact removal.</p>
                                </div>
                            </div>
                            <div class="about-feature-image-block">
                                <slider-comp v-if="jpegBlock === 1" :before_img="JpegImg1" :after_img="JpegImg1_2" :div_class="sliderClass" />
                            </div>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </div>
<footer-comp />
</template>

<script>
    import { Navigation, Pagination, A11y } from 'swiper/modules';
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import 'swiper/css';
    import 'swiper/css/navigation';
    import 'swiper/css/pagination';

    import NavbarComp from "../components/NavbarComp.vue";
    import FooterComp from "../components/FooterComp.vue";
    import ArticleUi from "../components/UI/ArticleUi.vue";
    import handlePopState from "../utils/index.js";
    import SliderComp from "../components/SliderComp.vue";

    import UpImg1 from "../assets/car2.png"
    import UpImg1_2 from "../assets/car.jpg"
    import UpImg2 from "../assets/flower2.png"
    import UpImg2_2 from "../assets/flower.png"
    import UpImg3 from "../assets/crystal2.png"
    import UpImg3_2 from "../assets/crystal.png"
    import BgImg1 from "../assets/woman.jpg"
    import BgImg1_2 from "../assets/woman_bg.png"
    import BgImg2 from "../assets/dog.jpg"
    import BgImg2_2 from "../assets/dog2.png"
    import BgImg3 from "../assets/people.jpg"
    import BgImg3_2 from "../assets/people2.png"
    import JpegImg1 from "../assets/jpeg_sun.jpg"
    import JpegImg1_2 from "../assets/jpeg_sun2.png"

    export default {
        components: {
            Swiper,
            SwiperSlide,
            NavbarComp,
            FooterComp,
            ArticleUi,
            SliderComp
        },
        setup() {
            return {
                modules: [Navigation, Pagination, A11y],
            };
        },
        data() {
            return {
                upscaleBlock: 1,
                bgBlock: 1,
                jpegBlock: 1,

                sliderClass: "slider-features",

                UpImg1: UpImg1,
                UpImg1_2: UpImg1_2,
                UpImg2: UpImg2,
                UpImg2_2: UpImg2_2,
                UpImg3: UpImg3,
                UpImg3_2: UpImg3_2,

                BgImg1: BgImg1,
                BgImg1_2: BgImg1_2,
                BgImg2: BgImg2,
                BgImg2_2: BgImg2_2,
                BgImg3: BgImg3,
                BgImg3_2: BgImg3_2,

                JpegImg1: JpegImg1,
                JpegImg1_2: JpegImg1_2

            }
        },
        created() {
            window.scrollTo(0, 0);
        },
        mounted() {
            handlePopState()
            document.title = `FlexFi Upscale - Features`
        },
        methods: {
            setNewImg(e, value) {
                if (this.upscaleBlock !== value) {
                    document.querySelectorAll(".UPSC").forEach(elem => elem.classList.remove('active'))
                    this.upscaleBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
                }
            },
            setNewImgBg(e, value) {
                if (this.bgBlock !== value) {
                    document.querySelectorAll(".BGR").forEach(elem => elem.classList.remove('active'))
                    this.bgBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
                }
            },
            setNewImgJpeg(e, value) {
                if (this.jpegBlock !== value) {
                    document.querySelectorAll(".RJPEGA").forEach(elem => elem.classList.remove('active'))
                    this.jpegBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
                }
            },
        }
    }
</script>

<style>
.features-container {
    width: 100%;
    height: auto;
    display: flex;
    padding-top: 200px;
    box-sizing: border-box;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 200px;
    z-index: 1;
}

.swiper-container {
    display: none;
    min-height: 0;
    min-width: 0;
    width: 100vw; 
    overflow: hidden;
}

.swiper-slide {
    width: auto;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 20px;
}

.swiper-wrapper {
    display: flex;
}

.swiper-pagination-bullet {
    background-color: rgba(0, 0, 0, 0.5);
    opacity: 1;
}

.swiper-pagination-bullet-active {
    opacity: 1;
    background: var(--swiper-pagination-color, var(--swiper-theme-color));
    background-color: #d091fa;
}

.swiper-button-next,
.swiper-button-prev {
    scale: 70%;
    top: 50%;
    color: #d091fa;
    fill: black !important;
    stroke: black !important;
}

.articles_arts_cont {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.articles_container {
    width: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
}

.more-features-block {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: #fff;
}

.more-features-block-block {
    width: 80%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 20px 50px;
    border-radius: 20px;
    gap: 50px;
}

.about-features-blocks-container {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.slider-features {
    width: 100% !important;
    height: 100% !important;
}

.about-feature-block {
    width: 70%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 20px;
    padding: 50px;
    overflow: hidden;
}

.about-feature-info {
    width: 40%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    gap: 20px;
}

.about-contain-all {
    display: flex;
    justify-content: space-between;
    width: 100%;
    align-items: center;
}

.article_choose__btn {
    width: 100%;
    height: 150px;
    display: flex;
    overflow-y: auto;
    align-items: flex-start;
    flex-direction: column;
    color: #fff;
    padding: 20px 50px;
    border-radius: 20px;
    cursor: pointer;
    gap: 20px;
    transition: .3s;
}

.article_choose__btn.active {
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
}

.article_choose__btn:hover {
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
}

.about-feature-image-block {
    width: 400px;
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.about-feature-image {
    width: 100%;
    height: 100%;
    border-radius: 20px;
}

.v-1 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(0deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.v-2 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.v-3 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, #fff 100%);
}

.hl {
    height: 2px;
    width: 100%;
    opacity: 0.3;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 50%, rgba(255, 255, 255, 0) 100%);
}

@media (min-width: 1400px) and (max-width: 1599px) {
    .about-feature-block {
        width: 80%;
    }
}

@media (min-width: 1200px) and (max-width: 1399px) {
    .about-feature-block {
        width: 90%;
    }

    .about-feature-image-block {
        width: 350px;
        height: 350px;
    }
}

@media (min-width: 992px) and (max-width: 1199px) {
    .about-feature-block {
        width: 90%;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 350px;
        height: 350px;
    }
}

@media (min-width: 768px) and (max-width: 991px) {
    .about-feature-block {
        width: 80%;
        flex-direction: column;
    }

    .about-contain-all {
        width: 100%;
    }

    .article_choose__btn {
        width: 70%;
        height: 150px;
    }

    .about-feature-image-block2 {
        width: 300px;
        height: 300px;
    }

    .swiper-container {
        display: flex;
        max-width: 90vw; 
    }

    .about-feature-info {
        display: none
    }

    .about-feature-image-block {
        display: none
    }

    .slider-features {
        display: flex;
        align-items: center
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .about-feature-block {
        width: 80%;
        flex-direction: column;
    }

    .about-contain-all {
        width: 90%;
        flex-direction: column;
    }
    .article_choose__btn {
        width: 70%;
        height: 150px;
    }

    .about-feature-image-block2 {
        width: 300px;
        height: 300px;
    }

    .swiper-container {
        display: flex;
        max-width: 90vw; 
    }

    .about-feature-info {
        display: none
    }

    .about-feature-image-block {
        display: none
    }

    .slider-features {
        display: flex;
        align-items: center
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .about-feature-block {
        width: 70%;
        flex-direction: column;
    }

    .about-feature-block .fs-33 {
        font-size: 20px
    }

    .about-contain-all {
        width: 100%;
        flex-direction: column;
    }

    .more-features-block-block {
        width: 70%
    }

    .article_choose__btn {
        width: 70%;
        height: 150px;
    }

    .about-feature-image-block2 {
        width: 200px;
        height: 200px;
    }

    .swiper-container {
        display: flex;
        max-width: 90vw; 
    }

    .about-feature-info {
        display: none
    }

    .about-feature-image-block {
        display: none
    }

    .slider-features {
        display: flex;
        align-items: center
    }
}

@media (max-width: 480px) {
    .more-features-block-block {
        width: 60%;
    }

    .about-feature-block {
        width: 50%;
        flex-direction: column;
    }

    .about-feature-block .align_center_text {
        font-size: 20px
    }

    .about-contain-all {
        width: 90%;
        flex-direction: column;
    }

    .article_choose__btn {
        width: 40%;
        height: 150px;
    }

    .about-feature-image-block2 {
        width: 150px;
        height: 150px;
    }

    .article_choose__btn .fs--25 {
        font-size: 15px
    }

    .article_choose__btn .small_text {
        font-size: 11px
    }

    .swiper-container {
        display: flex;
        max-width: 90vw; 
    }

    .about-feature-info {
        display: none
    }

    .about-feature-image-block {
        display: none
    }
}
</style>