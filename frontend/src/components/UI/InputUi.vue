<template>
  <div class="input-container">
    <input v-if="passwordType && !numberType" :id="inputId" :maxlength="max" :type="showPassword ? 'text' : 'password'" :placeholder="pr" :value="modelValue" @input="updateValue" />
    <input v-else-if="!passwordType && !numberType" type="text" :id="inputId" :readonly="enableReadonly" :maxlength="max" :value="modelValue" @input="updateValue" :placeholder="pr" />
    <input v-else :id="inputId" :min="min" :max="max" type="number" :placeholder="pr" :value="modelValue" @input="updateValue" />
    <span v-if="passwordType" class="eye-icon" @click="toggleVisibility">{{ showPassword ? '👁️' : '👁️‍🗨️' }}</span>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: String,
    passwordType: Boolean,
    numberType: Boolean,
    pr: String,
    max: String,
    min: String,
    enableReadonly: Boolean,
    inputId: String
  },
  data() {
    return {
      showPassword: false
    };
  },
  methods: {
    updateValue(event) {
      const inputValue = event.target.value;
      this.$emit('update:modelValue', inputValue);
    },
    toggleVisibility() {
      this.showPassword = !this.showPassword;
    },
  }
};
</script>

<style>
.input-container {
  position: relative;
  width: 100%;
}

.input-container input {
  width: 100%;
  height: 35px;
  background: transparent;
  padding-left: 10px;
  box-sizing: border-box;
  border: 1px #2e2f35 solid;
  outline: none;
  border-radius: 10px;
  transition: .3s;
}

.input-container input:focus {
	scale: 110%;
}

.input-container input[readonly] {
  color: #808080 !important;
  transition: .3s;
}

.eye-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
}
</style>