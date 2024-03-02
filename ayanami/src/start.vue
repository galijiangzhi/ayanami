<script>
import Header from './components/header.vue'
import Item from './components/item.vue'
export default {
  data(){
    return{
      header_class:"body_div",
      header_style:{
        height:"100vh",
        width:"100%",
        backgroundColor:"#462a5b"
      }
    }
  },
  components: {
    Header,
    Item,
}
}
</script>   

<template>
  <div :class="header_class" :style="header_style">
    <Header />
  </div>
  <div :class="item_class" :style="item_style">
    <Item />
  </div>
</template>
<style>
</style>
<!-- 初号机
紫色是#462A5B
绿色网格是#1B1C1C 图案颜色#27801B
黑色是#181818 -->
