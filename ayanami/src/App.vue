<script>
import Start from './start.vue'

export default {
  data(){
    return{
      body_class:"body_div",
    }
  },
  components: {
    Start
  }
}
</script>

<template>
  <Start />
</template>
<style>
  .app{
    background-color: red;
  }
</style>
