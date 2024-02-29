 、
  6、
  <!-- 该文件用于构建主页的头部导航栏 -->
<template>
    <div :style="root_div_style">
        <div :class="header" :style=header_style>
            <Logo />
        </div>
        <div :style="index_style">
            <Index />
        </div>
        <div class="header_web_style" :style="style_style">
            <web_Style />
        </div>
    </div>
</template>
<script>
    import Logo from './head/logo.vue'
    import Index from './head/index.vue'
    import web_Style from './head/web_style.vue'
import Head from './head/index.vue';
    export default{
        data(){
            return{
                header:"header",
                index:"index",
                root_div_style:{
                    display:"flex",
                    backgroundColor:"#181818",
                    alignItems:"flex-start"
                },
                header_style:{
                    height: "64px",
                    width: "100%",
                    padding:"8px"
                },
                index_style:{
                    display:"flex",
                    height:"80px",
                    marginRight: "40px"
                },
                style_style:{
                    position:"absolute",
                    top:"80px",
                    right:"0px"
                }
            }
        },
        components:{
            Logo,
            Index,
            Head,
            web_Style
        }
    }
</script>
<style>
    div{
        justify-content:center;
        align-items:center;
    }
</style>