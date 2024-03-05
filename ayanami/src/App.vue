<script>
import Start from './start.vue'


export default {
  data(){
    return{
      body_class:"body_div",
      color:{
        background:"#462a5b",
        background_b:"#260a3b",
        font:"#27801B",
        head:"#181818"
      }
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
</style>
