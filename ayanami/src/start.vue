<script>
import Header from './components/header.vue'

export default {
  data(){
    return{
      body_class:"body_div",
      body_style:{
        height:"100vh",
        width:"100%",
        backgroundColor:"#462a5b"
      }
    }
  },
  components: {
    Header,
}
}
</script>   

<template>
    <div :class="body_class" :style="body_style">
        <Header />
    </div>
</template>
<style>
</style>
