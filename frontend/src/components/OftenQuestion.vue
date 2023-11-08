<template>
    <div class="questions-block">
        <p class="brand_text">FAQ</p>
        <p class="header_text fs--50 fw--900 no-top align_center_text">Often questions</p>
        <template v-if="questions.length > 0">
            <question-model v-for="question in questions" :key="question.id" :question="question.title" :answear="question.text"/>
        </template>

        <template v-else>
            <p class="fs--20 white">No questions was asked.</p>
        </template>
    </div>
</template>

<script>
    import axios from "axios"
    import QuestionModel from "./UI/QuestionModel.vue";
    export default {
        components: {
            QuestionModel
        },
        data() {
            return {
                questions: []
            }
        },
        mounted() {
            axios.get(`${import.meta.env.VITE_BACKEND_DOMAIN}/api/v1/main/main_faqs/`)
            .then(res => {
                this.questions = res.data
            })
        }
    }
</script>

<style>
.questions-block {
    width: 70%;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

@media (min-width: 768px) and (max-width: 991px) {
    .questions-block {
        width: 75%;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .questions-block {
        width: 90%;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .questions-block {
        width: 90%;
    }
}

@media (max-width: 480px) {
    .questions-block {
        width: 90%;
    }
}
</style>