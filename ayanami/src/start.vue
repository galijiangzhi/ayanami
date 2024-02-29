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
<!-- 初号机
紫色是#462A5B
绿色网格是#1B1C1C 图案颜色#27801B
黑色是#181818 -->
